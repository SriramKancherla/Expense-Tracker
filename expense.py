import csv
import os

expenses = []
budget = 0

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    description = input("Enter description: ")
    expenses.append({'date': date, 'category': category, 'amount': amount, 'description': description})
    print("Expense added successfully.")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    for e in expenses:
        if e.get('date') and e.get('category') and e.get('description') and e.get('amount') is not None:
            print(f"Date: {e['date']} | Category: {e['category']} | Amount: {e['amount']} | Description: {e['description']}")
        else:
            print("Incomplete expense entry found and skipped.")

def set_budget():
    global budget
    try:
        budget = float(input("Enter your monthly budget: "))
        print(f"Monthly budget set to {budget}")
    except ValueError:
        print("Invalid input.")

def track_budget():
    if budget == 0:
        print("Please set your budget first.")
        return
    total_expenses = sum(e['amount'] for e in expenses if 'amount' in e)
    if total_expenses > budget:
        print(f"You have exceeded your budget by {total_expenses - budget}")
    else:
        print(f"You have {budget - total_expenses} left for the month.")

def save_expenses():
    with open('expenses.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        writer.writerows(expenses)
    print("Expenses saved to expenses.csv")

def load_expenses():
    if os.path.exists('expenses.csv'):
        with open('expenses.csv', 'r') as file:
            reader = csv.DictReader(file)
            loaded = 0
            for row in reader:
                if all(row.values()):
                    row['amount'] = float(row['amount'])
                    expenses.append(row)
                    loaded += 1
            if loaded > 0:
                print(f"\n{loaded} expenses loaded from file:\n")
                for e in expenses:
                    print(f"Date: {e['date']} | Category: {e['category']} | Amount: {e['amount']} | Description: {e['description']}")
            else:
                print("No data found in expenses.csv.")
    else:
        print("No data found. Starting with empty records.")

def menu():
    load_expenses()
    while True:
        print("\n1. Add expense\n2. View expenses\n3. Track budget\n4. Save expenses\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            if budget == 0:
                set_budget()
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

menu()
