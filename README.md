# 💰 Personal Expense Tracker

## 📌 Project Overview
The **Personal Expense Tracker** is a Python-based Command Line Interface (CLI) application designed to help users track their daily spending. Unlike simple spreadsheets, this application uses a persistent **SQLite database** to store financial records securely. It features modular architecture, grouping logic into separate files for database management, analytics, and validation.

This project was built to demonstrate **CRUD operations**, **Database Integration**, and **Modular Software Design**.

## ✨ Key Features
* **Add Expenses:** Record transactions with Amount, Category (e.g., Food, Travel), and Date.
* **View History:** Display a formatted table of all past expenses, sorted by date.
* **Analytics Module:** Automatically calculates:
    * Total money spent.
    * Breakdown of spending by Category (e.g., "You spent ₹500 on Food").
* **Crash-Proof Validation:** Prevents invalid inputs (e.g., entering text for price or wrong date formats) using the `validation.py` module.
* **Persistent Storage:** Data is saved in `expenses.db` and remains available after closing the app.

## 🛠️ Technologies Used
* **Language:** Python 3.x
* **Database:** SQLite3 (Embedded)
* **Modules:** `datetime` (for date handling), `sqlite3` (for storage)

## ⚙️ Installation & Execution
Follow these steps to run the project on your local machine:

1.  **Prerequisites:** Ensure you have Python installed.
    ```bash
    python --version
    ```
2.  **Download the Code:** Clone this repository or download the ZIP file.
3.  **Navigate to the Folder:**
    ```bash
    cd Personal-Expense-Tracker
    ```
4.  **Run the Application:**
    ```bash
    python main.py
    ```
5.  **Database Creation:** The app will automatically create a file named `expenses.db` on the first run.

## 🧪 Testing Instructions
To verify the application works as expected, follow these test cases:

**Test Case 1: Add Valid Expense (Positive Testing)**
1.  Select Option `1` (Add Expense).
2.  Enter Amount: `150.00`.
3.  Enter Category: `Food`.
4.  Enter Date: `2023-10-15`.
5.  **Result:** System should print "✅ Expense Saved!".

**Test Case 2: Invalid Input Handling (Negative Testing)**
1.  Select Option `1`.
2.  Enter Amount: `abc` (Text instead of number).
3.  **Result:** System should show "❌ Error: Please enter a numeric value" and ask again.

**Test Case 3: Analytics Check**
1.  Add two expenses: ₹100 for Food and ₹200 for Travel.
2.  Select Option `3` (View Analytics).
3.  **Result:** Total should display **₹300.00** and break down the categories correctly.

## 📂 Project Structure
```text
Personal-Expense-Tracker/
├── main.py          # Entry point & User Interface
├── database.py      # Handles SQLite connections & CRUD
├── analytics.py     # Logic for calculating totals
├── validation.py    # Error handling functions
├── expenses.db      # Database file (Auto-generated)
├── requirements.txt # List of dependencies
├── statement.md     # Project Problem Statement
└── README.md        # Documentation
