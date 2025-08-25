# Business Requirement Analyzer 📝

## Overview
The **Business Requirement Analyzer** is a web-based tool that automates the initial analysis of business requirements using Natural Language Processing (NLP). It helps to quickly categorize requirements and extract key information, reducing the time and potential for error associated with manual analysis.

This project was developed as a practical training report and leverages a rule-based NLP approach for simplicity and efficiency.

## Features
-   **Requirement Categorization:** Automatically classifies requirements into predefined categories like `Functional`, `Technical`, and `Data`.
-   **Keyword Extraction:** Identifies and extracts important nouns and proper nouns from the text to provide a quick summary.
-   **Data Persistence:** Saves all analyzed requirements, their categories, and keywords in a local SQLite database.
-   **User-Friendly Interface:** A simple web interface for inputting requirements and viewing instant, categorized results.

## Technologies Used
-   **Python:** The core backend logic.
-   **Flask:** A lightweight web framework to create the server and handle requests.
-   **SpaCy:** An industrial-strength NLP library for tasks like tokenization and part-of-speech tagging (used for keyword extraction).
-   **SQLite:** A file-based database used to store project data.
-   **HTML/CSS/JavaScript:** For the web-based user interface.

## System Architecture
The application follows a simple client-server model:
1.  **Client (index.html):** The web interface where users input requirements.
2.  **Server (app.py):** A Flask application that handles the NLP analysis and database interactions.
3.  **Database (requirements.db):** An SQLite database that stores all saved requirements.

## How to Run the Project
1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/YourUsername/Business-Requirement-Analyzer.git](https://github.com/YourUsername/Business-Requirement-Analyzer.git)
    cd Business-Requirement-Analyzer
    ```
2.  **Install dependencies:**
    You will need to install Flask and SpaCy. It's recommended to use a virtual environment.
    ```sh
    pip install Flask spacy
    python -m spacy download en_core_web_sm
    ```
3.  **Run the application:**
    ```sh
    python app.py
    ```
4.  Open your web browser and navigate to `http://127.0.0.1:5000` to use the tool.

## Project Structure
