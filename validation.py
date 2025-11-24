from datetime import datetime

def get_valid_amount(prompt):
   
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("❌ Error: Amount must be positive.")
            else:
                return value
        except ValueError:
            print("❌ Error: Please enter a numeric value (e.g., 50.00).")

def get_valid_date(prompt):
    
    while True:
        date_str = input(prompt)
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("❌ Error: Invalid format. Use YYYY-MM-DD (e.g., 2025-11-24).")