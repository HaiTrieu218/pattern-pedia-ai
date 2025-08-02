# PatternPedia: Your AI Design Pattern Advisor

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Framework](https://img.shields.io/badge/Streamlit-App-orange?style=for-the-badge&logo=streamlit)
![Status](https://img.shields.io/badge/Status-In%20Progress-green?style=for-the-badge)

An AI-powered assistant for discovering Software Design Patterns through semantic search.

<!-- TODO: Add a GIF demo of the final app here -->
<!-- ![PatternPedia Demo](link_to_your_demo.gif) -->

## ✨ Features

- **Natural Language Queries:** Forget keywords. Ask questions like you would to a senior developer.
- **Semantic Understanding:** The AI understands the _intent_ behind your problem, not just the words you use.
- **Relevant Suggestions:** Get a ranked list of design patterns that are most likely to solve your architectural issue.
- **Direct Links to Knowledge:** Each suggestion links directly to the detailed explanation on [Refactoring.Guru](https://refactoring.guru/).

## 💡 The Problem It Solves

Software design patterns are fundamental concepts, but learning and applying them is challenging. Traditional keyword-based search fails when a developer can describe a design problem but doesn't know the name of the corresponding pattern. For example, searching "how to let objects communicate without knowing each other" won't easily lead to the Observer or Mediator patterns. PatternPedia bridges this gap.

## 🛠️ Tech Stack

- **Data Crawling:** Scrapy & BeautifulSoup
- **AI & Semantic Search:**
  - Sentence-Transformers (`all-MiniLM-L6-v2`) for text embeddings.
  - ChromaDB as the Vector Database.
- **Application Backend & Frontend:** Python & Streamlit
- **Environment:** Poetry (or venv) for dependency management.

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### 1. Prerequisites

- Python 3.10+
- Git

### 2. Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/pattern-pedia-ai.git
    cd pattern-pedia-ai
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # Create venv
    python -m venv venv

    # Activate venv (macOS/Linux)
    source venv/bin/activate

    # Activate venv (Windows - Git Bash)
    source venv/Scripts/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    _(Note: You will need to create the `requirements.txt` file as you add packages)._

### 3. Running the Data Pipeline

You must run this pipeline once to populate the vector database.

1.  **Crawl the data:**

    ```bash
    # (Navigate to the scrapy project directory first)
    cd src/guru_scraper
    scrapy crawl patterns -o ../../data/raw_patterns.json
    cd ../..
    ```

2.  **Process and index the data:**
    ```bash
    python src/run_indexing.py
    ```

### 4. Running the Web App

Once the data is indexed, you can start the Streamlit application.

```bash
```
python -m streamlit run app/app.py
