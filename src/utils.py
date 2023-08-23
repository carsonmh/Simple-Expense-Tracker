from collections import defaultdict


def add_to_expenses(catagory, amount, description):
    with open("./src/expenses.txt", "a") as file:
        file.write(f"{catagory};{amount};{description}")


def print_expenses(catagory):
    data = defaultdict(list)
    with open("./src/expenses.txt", "r") as file:
        for line in file:
            elements = line.strip().split(";")
            data[elements[0]].append([elements[1], elements[2]])

    if catagory and catagory != "":
        print(f"Expenses for {catagory} catagory")
        for expense in data[catagory]:
            print(f"Price: {expense[0]} Description: {expense[1]}")
    else:
        print("All expenses")
        for catagory in data.keys():
            for expense in data[catagory]:
                print(
                    f"Catagory: {catagory} Price: {expense[0]} Description: {expense[1]}"
                )
