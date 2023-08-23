from curses.ascii import isdigit
from utils import add_to_expenses, list_expenses, delete_expense, find_expense

print(
    'What would you like to do?\nEnter "a" to add an expensen\nEnter "v" to view expenses\nEnter "d" to delete an expense\nEnter "s" to search for an expense'
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

elif operation == "v":
    print("Catagory? (press 'enter' for all)")
    catagory = input().lower()
    list_expenses(catagory)

elif operation == "d":
    expenses = list_expenses("", summarize=False)
    if len(expenses) == 0:
        exit()

    print("Please enter the number of the expense you would like to delete")
    num = input()
    if not num or not isdigit(num):
        print("You must enter a valid number")
        exit()
    delete_expense(int(num))

elif operation == "s":
    print("Please enter a description")
    description = input()
    find_expense(description)

else:
    print("Please input a valid operation")
