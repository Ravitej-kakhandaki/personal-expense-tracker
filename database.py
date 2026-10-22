 
import sqlite3


def connect_db():
    return sqlite3.connect("expenses.db")


def create_table():
    connection = connect_db()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            month TEXT NOT NULL,
            year TEXT NOT NULL,
            amount REAL NOT NULL,
            PRIMARY KEY (month, year)
        )
    """)

    connection.commit()
    connection.close()


def add_expense(amount, category, date, description):
    connection = connect_db()

    connection.execute("""
        INSERT INTO expenses (amount, category, date, description)
        VALUES (?, ?, ?, ?)
    """, (amount, category, date, description))

    connection.commit()
    connection.close()


def get_all_expenses():
    connection = connect_db()

    cursor = connection.execute("""
        SELECT id, amount, category, date, description
        FROM expenses
        ORDER BY id
    """)

    records = cursor.fetchall()
    connection.close()

    return records

def search_expenses(category):
    connection = connect_db()

    cursor = connection.execute("""
        SELECT id, amount, category, date, description
        FROM expenses
        WHERE LOWER(category) = LOWER(?)
        ORDER BY id
    """, (category.strip(),))

    records = cursor.fetchall()
    connection.close()

    return records

def get_spending_summary():
    connection = connect_db()

    cursor = connection.execute("""
        SELECT COUNT(*), COALESCE(SUM(amount), 0)
        FROM expenses
    """)

    result = cursor.fetchone()
    connection.close()

    return result


def delete_expense(expense_id):
    connection = connect_db()

    cursor = connection.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    connection.commit()
    deleted = cursor.rowcount > 0
    connection.close()

    return deleted


def update_expense(expense_id, amount, category, date, description):
    connection = connect_db()

    cursor = connection.execute("""
        UPDATE expenses
        SET amount = ?, category = ?, date = ?, description = ?
        WHERE id = ?
    """, (amount, category, date, description, expense_id))

    connection.commit()
    updated = cursor.rowcount > 0
    connection.close()

    return updated


def get_monthly_summary(month, year):
    connection = connect_db()

    cursor = connection.execute("""
        SELECT COUNT(*), COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE SUBSTR(date, 4, 2) = ?
          AND SUBSTR(date, 7, 4) = ?
    """, (month, year))

    result = cursor.fetchone()
    connection.close()

    return result


def get_category_summary():
    connection = connect_db()

    cursor = connection.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
        ORDER BY SUM(amount) DESC
    """)

    records = cursor.fetchall()
    connection.close()

    return records


def set_monthly_budget(month, year, amount):
    connection = connect_db()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            month TEXT NOT NULL,
            year TEXT NOT NULL,
            amount REAL NOT NULL,
            PRIMARY KEY (month, year)
        )
    """)

    connection.execute("""
        INSERT INTO budgets (month, year, amount)
        VALUES (?, ?, ?)
        ON CONFLICT(month, year)
        DO UPDATE SET amount = excluded.amount
    """, (month, year, amount))

    connection.commit()
    connection.close()


def get_monthly_budget(month, year):
    connection = connect_db()

    cursor = connection.execute("""
        SELECT amount FROM budgets
        WHERE month = ? AND year = ?
    """, (month, year))

    result = cursor.fetchone()
    connection.close()

    return result[0] if result else None



def export_expenses():
    connection = connect_db()

    cursor = connection.execute("""
        SELECT id, amount, category, date, description
        FROM expenses
        ORDER BY id
    """)

    records = cursor.fetchall()
    connection.close()

    return records








if __name__ == "__main__":
    create_table()
    print("Database and expenses table created successfully!")
