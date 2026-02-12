![Python](https://img.shields.io/badge/python-3.13-blue)
![GitHub repo size](https://img.shields.io/github/repo-size/jeversonluis/google-sheets-automation)

# 🚀 Google Sheets Automation – Bitcoin Price Integration

This project demonstrates how to consume a public API using Python and prepare the data for automation workflows such as Google Sheets integration.

It fetches real-time Bitcoin price data from the CoinGecko API and processes it using clean project structure and error handling best practices.

---

## 📌 Project Objective

The goal of this project is to build a scalable automation foundation that can:

- Fetch external API data
- Handle errors properly
- Maintain clean architecture
- Prepare data for integration with tools like Google Sheets
- Serve as a base for workflow automation projects

---

## 🛠 Tech Stack

- Python 3.13
- Requests
- Virtual Environment (venv)
- Git / GitHub

---

## 📂 Project Structure

```
google-sheets-automation/
│
├── main.py
├── services/
│   └── crypto_service.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/jeversonluis/google-sheets-automation.git
cd google-sheets-automation
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

---

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac / Linux:**

```bash
source venv/bin/activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the script

```bash
python main.py
```

---

## ✅ Current Features

- Fetches real-time Bitcoin price from CoinGecko API
- Implements structured service separation
- Includes basic error handling
- Clean and scalable project organization

---

## 🔮 Future Improvements

- Integrate with Google Sheets API
- Automate updates to spreadsheets
- Add logging system
- Add scheduling (cron / task scheduler)
- Expand to support multiple cryptocurrencies

---

## 💡 Use Case

This project can serve as a foundation for:

- Financial data automation
- Report automation
- API-to-Sheets workflows
- Business data pipelines
- Automation freelancing projects

---

## 👨‍💻 Author

Jeverson Luis S
Python Automation & API Integration  

---

## 📌 License

This project is for educational and portfolio purposes.
