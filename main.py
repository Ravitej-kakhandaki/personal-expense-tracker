 
import csv
from datetime import datetime

from database import (
    create_table,
    add_expense,
    delete_expense,
    export_expenses,
    get_all_expenses,
    get_category_summary,
    get_monthly_budget,
    get_monthly_summary,
    get_spending_summary,
    search_expenses,
    set_monthly_budget,
    update_expense,
)

# Create the database table when the program starts
create_table()


def get_valid_month_year():
    """Get and validate a month and year from the user."""
    month = input("Enter month (MM): ").strip()
    year = input("Enter year (YYYY): ").strip()

    if (
        len(month) != 2
        or not month.isdigit()
        or not 1 <= int(month) <= 12
    ):
        print("Invalid month. Enter a value from 01 to 12.")
        return None

    if len(year) != 4 or not year.isdigit():
        print("Invalid year. Enter a four-digit year.")
        return None

    return month, year


def get_valid_date(prompt="Enter date (DD-MM-YYYY): "):
    """Get a valid calendar date in DD-MM-YYYY format."""
    date = input(prompt).strip()

    try:
        datetime.strptime(date, "%d-%m-%Y")
        return date
    except ValueError:
        print("Invalid date. Please use DD-MM-YYYY, e.g. 22-10-2026.")
        return None


def main():
    while True:
        print("\n================================")
        print("     PERSONAL EXPENSE TRACKER")
        print("================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. View Total Spending")
        print("5. Update Expense")
        print("6. Delete Expense")
        print("7. Monthly Expense Report")
        print("8. Category-wise Spending Report")
        print("9. Set or View Monthly Budget")
        print("10. Export Expenses to CSV")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ").strip()

        # 1. Add Expense
        if choice == "1":
            try:
                amount = float(input("Enter amount: ₹"))

                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue

                category = input("Enter category: ").strip()

                if not category:
                    print("Category cannot be empty.")
                    continue

                date = get_valid_date()
                if date is None:
                    continue

                description = input("Enter description: ").strip()

                add_expense(amount, category, date, description)
                print("Expense saved to database successfully!")

            except ValueError:
                print("Invalid amount. Enter a number such as 150 or 150.50.")

        # 2. View Expenses
        elif choice == "2":
            records = get_all_expenses()

            if not records:
                print("No expenses recorded yet.")
            else:
                print("\n========== ALL EXPENSES ==========")

                for record in records:
                    print(f"\nExpense ID: {record[0]}")
                    print(f"Amount: ₹{record[1]:.2f}")
                    print(f"Category: {record[2]}")
                    print(f"Date: {record[3]}")
                    print(f"Description: {record[4] or ''}")

        # 3. Search Expenses
        elif choice == "3":
            search_category = input("Enter category to search: ").strip()

            if not search_category:
                print("Category cannot be empty.")
                continue

            records = search_expenses(search_category)

            if not records:
                print("No expenses found in this category.")
            else:
                print("\n========== SEARCH RESULTS ==========")

                for record in records:
                    print(f"\nExpense ID: {record[0]}")
                    print(f"Amount: ₹{record[1]:.2f}")
                    print(f"Category: {record[2]}")
                    print(f"Date: {record[3]}")
                    print(f"Description: {record[4] or ''}")

        # 4. View Total Spending
        elif choice == "4":
            total_count, total_amount = get_spending_summary()

            print("\n========== SPENDING SUMMARY ==========")
            print(f"Total expenses: {total_count}")
            print(f"Total spending: ₹{total_amount:.2f}")

        # 5. Update Expense
        elif choice == "5":
            try:
                expense_id = int(input("Enter Expense ID to update: "))

                if expense_id <= 0:
                    print("Expense ID must be positive.")
                    continue

                # Check whether the expense exists before requesting changes.
                records = get_all_expenses()
                if not any(record[0] == expense_id for record in records):
                    print("Expense ID not found.")
                    continue

                amount = float(input("Enter new amount: ₹"))

                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue

                category = input("Enter new category: ").strip()

                if not category:
                    print("Category cannot be empty.")
                    continue

                date = get_valid_date("Enter new date (DD-MM-YYYY): ")
                if date is None:
                    continue

                description = input("Enter new description: ").strip()

                updated = update_expense(
                    expense_id, amount, category, date, description
                )

                if updated:
                    print("Expense updated successfully!")
                else:
                    print("Expense ID not found.")

            except ValueError:
                print("Please enter valid numeric values.")

        # 6. Delete Expense
        elif choice == "6":
            try:
                expense_id = int(input("Enter Expense ID to delete: "))

                if expense_id <= 0:
                    print("Expense ID must be positive.")
                    continue

                if delete_expense(expense_id):
                    print("Expense deleted successfully!")
                else:
                    print("Expense ID not found.")

            except ValueError:
                print("Please enter a valid numeric ID.")

        # 7. Monthly Expense Report + Budget Warning
        elif choice == "7":
            month_year = get_valid_month_year()

            if month_year is None:
                continue

            month, year = month_year
            total_count, total_amount = get_monthly_summary(month, year)

            print("\n========== MONTHLY EXPENSE REPORT ==========")
            print(f"Month: {month}-{year}")
            print(f"Number of expenses: {total_count}")
            print(f"Total spending: ₹{total_amount:.2f}")

            budget = get_monthly_budget(month, year)

            if budget is not None:
                percentage = (total_amount / budget) * 100
                remaining = budget - total_amount

                print(f"Monthly budget: ₹{budget:.2f}")
                print(f"Budget used: {percentage:.1f}%")

                if total_amount > budget:
                    print("WARNING: You have exceeded your monthly budget!")
                    print(f"Amount over budget: ₹{abs(remaining):.2f}")
                elif percentage >= 80:
                    print("WARNING: You have used at least 80% of your budget!")
                    print(f"Remaining budget: ₹{remaining:.2f}")
                else:
                    print(f"Remaining budget: ₹{remaining:.2f}")
            else:
                print("No budget set for this month.")

        # 8. Category-wise Spending
        elif choice == "8":
            records = get_category_summary()

            print("\n========== CATEGORY-WISE SPENDING ==========")

            if not records:
                print("No expenses recorded yet.")
            else:
                for category, total in records:
                    print(f"{category}: ₹{total:.2f}")

        # 9. Set or View Monthly Budget
        elif choice == "9":
            month_year = get_valid_month_year()

            if month_year is None:
                continue

            month, year = month_year
            existing_budget = get_monthly_budget(month, year)

            if existing_budget is not None:
                print(f"Current budget: ₹{existing_budget:.2f}")
            else:
                print("No budget set for this month.")

            answer = input(
                "Would you like to set or update it? (y/n): "
            ).strip().lower()

            if answer == "y":
                try:
                    amount = float(input("Enter monthly budget: ₹"))

                    if amount <= 0:
                        print("Budget must be greater than zero.")
                        continue

                    set_monthly_budget(month, year, amount)
                    print("Monthly budget saved successfully!")

                except ValueError:
                    print("Please enter a valid numeric budget.")

            elif answer != "n":
                print("Please enter y or n.")

        # 10. Export Expenses to CSV
        elif choice == "10":
            records = export_expenses()

            if not records:
                print("No expenses available to export.")
            else:
                try:
                    with open(
                        "expenses_export.csv",
                        "w",
                        newline="",
                        encoding="utf-8-sig",
                    ) as file:
                        writer = csv.writer(file)
                        writer.writerow(
                            ["ID", "Amount", "Category", "Date", "Description"]
                        )
                        writer.writerows(records)

                    print("Expenses exported successfully!")
                    print("File: expenses_export.csv")

                except OSError as error:
                    print(f"Could not export expenses: {error}")

        # 11. Exit
        elif choice == "11":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 11.")


if __name__ == "__main__":
    main()
