from utils import add_to_expenses, print_expenses

print(
    'What would you like to do?\nEnter "a" to add an expensen\nEnter "v" to view expenses\nEnter "d" to delete an expense'
)
operation = input().lower()
if operation == "a":
    print("Enter a catagory")
    catagory = input()
    print("Enter an amount")
    amount = input()
    try:
        amount = float(amount)
    except ValueError:
        print("Please enter a valid number")
        exit()
    print("Enter a description")
    description = input()
    add_to_expenses(catagory, amount, description)
    print("Expense added successfully")
elif operation == "v":
    print("Catagory? (press 'enter' for all)")
    catagory = input().lower()
    print_expenses(catagory)
elif operation == "d":
    print()
else:
    print("Please input a valid operation")
