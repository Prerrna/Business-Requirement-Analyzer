from flask import Flask, request, jsonify, render_template
import spacy
import sqlite3

app = Flask(__name__)
nlp = spacy.load('en_core_web_sm')

# Connect to SQLite
conn = sqlite3.connect('requirements.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS requirements (
    id INTEGER PRIMARY KEY,
    raw_text TEXT,
    category TEXT,
    keywords TEXT
)
''')
conn.commit()

CATEGORIES = {
    'Functional': ['feature', 'function', 'requirement', 'process', 'workflow', 'action'],
    'Technical': ['database', 'api', 'interface', 'performance', 'security', 'system'],
    'Data': ['data', 'report', 'analytics', 'model', 'query', 'storage']
}

def categorize_requirement(text):
    text_lower = text.lower()
    for category, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in text_lower:
                return category
    return 'Other'

def extract_keywords(text):
    doc = nlp(text)
    keywords = [token.text for token in doc if token.pos_ in ('NOUN', 'PROPN')]
    return ', '.join(keywords)

def save_requirement(raw_text, category, keywords):
    cursor.execute('''
    INSERT INTO requirements (raw_text, category, keywords) VALUES (?, ?, ?)
    ''', (raw_text, category, keywords))
    conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('requirement', '')
    category = categorize_requirement(text)
    keywords = extract_keywords(text)
    save_requirement(text, category, keywords)
    return jsonify({'category': category, 'keywords': keywords})

@app.route('/list')
def list_requirements():
    cursor.execute('SELECT id, raw_text, category, keywords FROM requirements')
    rows = cursor.fetchall()
    all_reqs = [{'id': row[0], 'text': row[1], 'category': row[2], 'keywords': row[3]} for row in rows]
    return jsonify(all_reqs)

@app.route('/clear', methods=['POST'])
def clear_requirements():
    cursor.execute('DELETE FROM requirements')
    conn.commit()
    return jsonify({'status': 'cleared'})

if __name__ == "__main__":
    app.run(debug=True)
