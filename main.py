import database
import analytics
import validation

def main():
    
    database.initialize_db()
    
    while True:
        print("\n💰 PERSONAL EXPENSE TRACKER 💰")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Analytics")
        print("4. Delete Expense")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("\n--- Add New Expense ---")
            amt = validation.get_valid_amount("Enter Amount: ₹")
            cat = input("Enter Category (Food, Travel, Bills): ")
            desc = input("Enter Description: ")
            date = validation.get_valid_date("Enter Date (YYYY-MM-DD): ")
            
            database.add_expense(amt, cat, desc, date)
            print("✅ Expense Saved!")

        elif choice == '2':
            print("\n--- Expense History ---")
            expenses = database.get_all_expenses()
            
            print(f"{'ID':<5} {'Date':<12} {'Category':<15} {'Amount':<10} {'Description'}")
            print("-" * 65)
            for exp in expenses:
                print(f"{exp[0]:<5} {exp[4]:<12} {exp[2]:<15} ₹{exp[1]:<10} {exp[3]}")

        elif choice == '3':
            print("\n📊 --- Spending Analytics ---")
            total = analytics.get_total_expenses()
            print(f"💰 TOTAL SPENT: ₹{total:.2f}")
            
            print("\nCategory Breakdown:")
            cats = analytics.get_expenses_by_category()
            for c, amt in cats.items():
                print(f"   - {c}: ₹{amt:.2f}")

        elif choice == '4':
            try:
                ex_id = int(input("Enter Expense ID to delete: "))
                database.delete_expense(ex_id)
                print("🗑️ Expense Deleted.")
            except ValueError:
                print("❌ Invalid ID.")

        elif choice == '5':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()