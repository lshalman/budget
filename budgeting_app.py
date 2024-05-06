#Budgeting app that balances income and expenses. Include error handling and data saving in v1, interface in v2.


class Category:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount
    def summary(self):
        return self.description + ' - ' + str(self.amount)

class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category
    def summary(self):
            return 'Expense - ' + str(self.amount)
        
class Income: 
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount
    def summary(self):
            return 'Earning - ' + str(self.amount)
        
def summarize_categories():
    str = "Budget Categories"
    for cats in budget_categories:
        str += ' : ' + cats.summary()
    return str
def update_categories():
    for entries in expense_entries:
        for cats in budget_categories:
            if cats.description == entries.category:
                cats.amount = cats.amount - entries.amount

'''
march_salary = Income('march salary', 10000)
new_shoes = Expense('new shoes', 00, 'misc')
birthday_gift = Income('bday gift', 50)
flat_tire = Expense('flat tire', 80, 'car')

rent = Category('rent', 3000)
groceries = Category('groceries', 1000)
car = Category('car', 250)
misc = Category('misc', 1000)


budget_categories = []
income_entries = []
expense_entries = []

budget_categories.append(rent)
budget_categories.append(groceries)
budget_categories.append(car)
budget_categories.append(misc)

income_entries.append(march_salary)
expense_entries.append(new_shoes)
income_entries.append(birthday_gift)
expense_entries.append(flat_tire)
                    
print(summarize_categories())
update_categories()
print(summarize_categories())
'''
    
budget_categories = []
income_entries = []
expense_entries = []

def summarize_categories():
    str = "Budget Categories"
    for cats in budget_categories:
        str += ' : ' + cats.summary()
    return str
def update_categories():
    for entries in expense_entries:
        for cats in budget_categories:
            if cats.description == entries.category:
                cats.amount = int(cats.amount) - int(entries.amount)
def summarize_spending():
    for entry in expense_entries:
        print(entry.description +': ' + str(entry.amount))

def summarize_earning():
    for entry in income_entries:
        print(entry.description +': ' + str(entry.amount))
    

value = 0
print('''Type 1 to enter a new category. Type 2 to log an expense entry. Type 3 to log an income entry. Type 4 to see your spending. Type 5 to see your income. Type 6 to see how much you have left in your budget. Type 7 to exit the program.''')
print()
    
while value!= 7:
    try:
        value = int(input("Enter a value "))
    except:
        print("Error: Please re-enter a value ")

    if value == 1:
        cat_description = input('Enter a description: ')
        cat_amount = input('What is the budget amount? ')
        budget_categories.append(Category(cat_description, cat_amount))
    elif value == 2:
        exp_description = input('Enter a description: ')
        exp_amount = input('What is the amount? ')
        exp_category = input('What category does this expense fall into? ')
        expense_entries.append(Expense(exp_description, exp_amount, exp_category))
        update_categories()
    elif value == 3:
        inc_description = input('Enter a description: ')
        inc_amount = input('What is the amount? ')
        income_entries.append(Income(inc_description, inc_amount))
    elif value == 4:
        summarize_spending()
    elif value == 5:
        summarize_earning()
    elif value == 6:
        print(summarize_categories())
    elif value == 7:
        pass
    
    else:
        print("That value does not correspond to any action, sorry!")
        
        
    print()


    
