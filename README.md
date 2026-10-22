# 💸 Personal Expense Tracker

<p align="center">
  A simple, database-powered expense management application built with Python and SQLite.
  <br />
  Track spending, manage monthly budgets, and understand where your money goes.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white" alt="Python 3.12" />
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Interface-CLI-lightgrey" alt="Command Line Interface" />
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Project Status" />
</p>

---

## 📌 Overview

**Personal Expense Tracker** is a command-line application that helps users record and organize expenses using a local SQLite database.

It supports expense management, monthly spending reports, category-wise summaries, budget tracking, and CSV export through an interactive menu.

## ✨ Features

| Feature              | Description                                     |
| -------------------- | ----------------------------------------------- |
| ➕ Add Expenses      | Record amount, category, date, and description  |
| 📋 View Expenses     | Display saved expense records                   |
| 🔍 Search            | Find expenses by category                       |
| 📊 Spending Summary  | Calculate total expenses and spending           |
| ✏️ Update & Delete   | Modify or remove existing records               |
| 📅 Monthly Reports   | Review spending for a selected month            |
| 🗂️ Category Analysis | Summarize spending by category                  |
| 🎯 Budget Management | Set monthly budgets and receive warnings        |
| 📁 CSV Export        | Export expense records for spreadsheet analysis |
| ✅ Input Validation  | Handle invalid amounts, dates, and other inputs |

## 🛠️ Tech Stack

- **Language:** Python 3
- **Database:** SQLite
- **Queries:** SQL
- **Data Export:** Python CSV module
- **Tools:** Visual Studio Code, Git, GitHub

## 📂 Project Structure

```text
expense-tracker-python/
├── main.py              # Menu and application logic
├── database.py          # Database operations and SQL queries
├── README.md            # Project documentation
└── .gitignore           # Excludes local data and generated files
```

The SQLite database and CSV export are created locally when needed and are excluded from version control.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or later
- Git (optional, for cloning the repository)

### Installation

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Open the project directory**

```bash
cd expense-tracker-python
```

**3. Run the application**

```bash
python main.py
```

Follow the interactive menu to manage your expenses.

## 🧠 Key Learnings

- Applied Python fundamentals to build a complete application.
- Used SQLite to persist data between program runs.
- Implemented CRUD operations: Create, Read, Update, and Delete.
- Wrote SQL queries for filtering and aggregating expense data.
- Added input validation and exception handling.
- Organized database logic separately from the main application.
- Implemented CSV export and monthly budget calculations.

## 🔮 Future Enhancements

- Build a web interface using Flask or FastAPI.
- Visualize spending with charts and graphs.
- Add user authentication and personalized accounts.
- Introduce automated unit tests.

---

<p align="center">
  Built with 🐍 Python and 🗄️ SQLite
</p>
