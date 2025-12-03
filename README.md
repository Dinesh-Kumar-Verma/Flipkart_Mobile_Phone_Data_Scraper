# Flipkart Mobile Phone Data Scraper (Production-Grade Pipeline)

A modular, production-ready data pipeline designed to **extract, clean, and standardize mobile phone listings from Flipkart**.

This project is built to handle real-world scraping challenges such as:

- Request throttling and anti-bot protections  
- Messy and changing HTML structure  
- Multi-page navigation and inconsistent pagination  
- Converting unstructured text into clean, numerical, analysis-ready data  

It reflects real data-engineering workflows used in:

- E-commerce and product intelligence  
- Procurement / tender data platforms  
- Market research and analytics pipelines  
- ETL/ELT data pipelines feeding ML and BI systems  

---

## ✨ Key Features

### ✔️ Reliable HTTP Fetching (Anti-Bot + Anti-Throttle)

- Uses `curl_cffi` with **browser-level TLS impersonation** to mimic real Chrome traffic.
- Implements **retry logic** with backoff when requests fail or return throttling responses.
- Adds **randomized delays** between requests to reduce the chance of blocking.
- Uses configurable headers to keep the scraper resilient over time.

---

### ✔️ Robust Parsing Layer

- Built with **BeautifulSoup4** for HTML parsing.
- **Index-safe extraction** to handle missing/optional fields without crashing.
- Modular parsing functions to keep logic clear and maintainable.
- Resistant to minor structural changes in the page HTML.

---

### ✔️ Smart Pagination Engine

- Automatically discovers and follows the **"Next"** page link on Flipkart search results.
- Stops scraping when:
  - No "Next" link is available, or  
  - Pages return no product data (blank/throttled pages), even after a retry.
- Handles multi-page scraping in a controlled, predictable way.

---

### ✔️ Production-Grade Logging

- Uses Python’s built-in `logging` module with a dedicated utility.
- **Console + file logging** for real-time monitoring and historical analysis.
- Module-specific loggers:
  - `fetcher` – HTTP requests & anti-throttle handling  
  - `parser` – HTML parsing & extraction  
  - `pipeline` – orchestration, pagination, and control flow  
  - `cleaners` – data cleaning & regex extraction
- Timestamped, consistently formatted log messages.

---

### ✔️ Data Cleaning & Standardization

Includes utility functions that transform messy text into clean, typed fields:

- **Price** → removes currency symbols and formatting, returns integer  
- **Ratings & Reviews** → extracts numeric counts from strings like `"12,345 Ratings & 1,234 Reviews"`  
- **Camera** → extracts rear and front camera megapixels from spec strings  
- **Memory** → parses RAM, ROM, and expandable storage (e.g., `"8 GB RAM | 128 GB ROM | Expandable Upto 1 TB"`)  
- **Battery** → extracts capacity in mAh  
- **Display** → parses screen size in inches and cm, plus display type (HD+, AMOLED, etc.)

This results in a **clean, consistent schema** that is ready for analytics or machine learning.

---

### ✔️ Structured, Integration-Ready Output

The final output is a **CSV file** with a well-defined schema, ideal for:

- Loading into **PostgreSQL** or other relational databases  
- Feeding into **ML pipelines** as structured features  
- Building **dashboards** in Power BI, Tableau, or Streamlit  
- Further data analysis in Python, R, or SQL  

---

## 🛠 Tech Stack

- **HTTP & Anti-Bot:** `curl_cffi`
- **HTML Parsing:** `BeautifulSoup4`
- **Data Processing:** `pandas`
- **Logging:** Python `logging` module
- **Environment / Packaging:** `venv`, `uv`, `pyproject.toml`

---

## 📁 Project Structure

```text
.
├── .gitignore
├── .python-version
├── LICENSE
├── main.py                 # Multi-page scraper entry point
├── single_page_main.py     # Single-page scraper (for quick tests)
├── pyproject.toml
├── uv.lock
├── README.md
│
├── data/
│   ├── raw/                # Optional: for raw dumps (if used)
│   └── processed/          # Final cleaned CSV output
│
├── scraper/
│   ├── fetcher.py          # HTTP requests + soup creation
│   ├── pagination.py       # Next-page discovery logic
│   ├── parser.py           # HTML parsing and field extraction
│   └── pipeline.py         # Orchestration: loop pages, aggregate data
│
└── utils/
    ├── cleaners.py         # Regex-based text → numeric field cleaners
    ├── path.py            
    └── logger.py           # Console + file logging configuration

```

## ⚙️ Setup & Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Dinesh-Kumar-Verma/Flipkart_Mobile_Phone_Data_Scraper.git
    cd Flipkart_Mobile_Phone_Data_Scraper
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv .venv
    uv venv
    ```

3.  **Activate the virtual environment:**

    -   On Windows:

        ```bash
        .venv\Scripts\activate
        ```

    -   On macOS/Linux:

        ```bash
        source .venv/bin/activate
        ```

4.  **Install the dependencies:**

    This project uses `uv` for package management.

    ```bash
    pip install uv
    uv sync          
    uv pip install -r requirements.txt
    ```

## How to Run

### Scraping Multiple Pages

To scrape data from multiple pages, run the `main.py` script:

```bash
python main.py
```

### Scraping a Single Page

To scrape data from only the first page, run the `single_page_main.py` script:

```bash
python single_page_main.py
```
