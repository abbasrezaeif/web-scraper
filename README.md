# 🌐 Web Scraper

A Python web scraper that automatically extracts quotes, authors, and tags from https://quotes.toscrape.com and exports the data to both CSV and Excel files.

---

## 📸 Demo

> *(Add a screenshot of the terminal output or the generated Excel file in `/assets` later.)*

---

## ✨ Features

- 🌍 Crawl multiple pages automatically (Pagination)
- 📝 Extract quotes
- 👤 Extract authors
- 🏷️ Extract tags
- 📄 Export to CSV
- 📊 Export to Excel (.xlsx)
- ⚡ Clean and lightweight implementation
- 🐍 Beginner-friendly Python project

---

## 📂 Project Structure

```
web-scraper/
│
├── assets/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Example Output

After running the program:

```
Enter URL:
https://quotes.toscrape.com

Scraping: https://quotes.toscrape.com
...
Scraping: https://quotes.toscrape.com/page/10/

Done. 100 quotes saved to quotes.csv and quotes.xlsx
```

Generated files:

```
quotes.csv
quotes.xlsx
```

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/abbasrezaeif/web-scraper.git
```

Go to the project folder:

```bash
cd web-scraper
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

macOS / Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run:

```bash
python main.py
```

Enter:

```
https://quotes.toscrape.com
```

The program automatically follows every page and exports the collected data.

---

## 🛠 Technologies

- Python
- Requests
- BeautifulSoup4
- OpenPyXL
- CSV
- Git
- GitHub

---

## 📌 Future Improvements

- Export to JSON
- Export to SQLite
- Export to PostgreSQL
- Multi-website support
- Config file support
- Logging
- Error handling & retries
- Async scraping for higher performance

---

## 👨‍💻 Author

**Abbas Rezaei**

Building practical Python projects while learning backend development and automation.