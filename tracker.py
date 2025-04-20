import csv

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        date = input("Enter date: ")
        category = input("Enter category: ")
        amount = input("Enter amount: ")
        self.expenses.append([date, category, amount])
        print("Expense added")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded")
        else:
            for i, expense in enumerate(self.expenses, 1):
                print(f"{i}. Date: {expense[0]}, Category: {expense[1]}, Amount: ₹{expense[2]}")

    def delete_expense(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            for i, expense in enumerate(self.expenses, 1):
                print(f"{i}. Date: {expense[0]}, Category: {expense[1]}, Amount: ₹{expense[2]}")
            index = int(input("Enter index to delete: ")) - 1
            if 0 <= index < len(self.expenses):
                del self.expenses[index]
                print("Expense deleted")
            else:
                print("Invalid index")

def main():
    tracker = ExpenseTracker()
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.delete_expense()
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    main()
