import database

def get_total_expenses():
    
    expenses = database.get_all_expenses()
    total = 0
    for expense in expenses:
        total += expense[1] 
    return total

def get_expenses_by_category():
    
    expenses = database.get_all_expenses()
    category_totals = {}
    
    for expense in expenses:
        amount = expense[1]
        category = expense[2]
        
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
            
    return category_totals