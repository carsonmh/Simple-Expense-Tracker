from collections import defaultdict


def add_to_expenses(catagory, amount, description):
    with open("./src/expenses.txt", "a") as file:
        file.write(f"{catagory};{amount};{description}\n")
    print("Expense added!")


def list_expenses(catagory, summarize=True):
    data = defaultdict(list)
    with open("./src/expenses.txt", "r") as file:
        for line in file:
            elements = line.strip().split(";")
            data[elements[0]].append([elements[1], elements[2]])

    if catagory and catagory != "":
        if not data[catagory]:
            print(f"\nNo expenses for {catagory} catagory")
            return []
        print(f"\nExpenses for {catagory} catagory")
        for i, expense in enumerate(data[catagory]):
            print(f"{i + 1}. Price: {expense[0]} Description: {expense[1]}")

        return data[catagory]

    if len(data.keys()) == 0:
        print("No expenses")
        return []
    all_expenses = []
    print("All expenses")
    i = 1
    for catagory in data.keys():
        for expense in data[catagory]:
            all_expenses.append([catagory] + expense)
            print(
                f"{i}. Catagory: {catagory} Price: {expense[0]} Description: {expense[1]}"
            )
            i += 1
    if summarize:
        print("\nSummary:")
        for catagory in data.keys():
            total = 0
            for expense in data[catagory]:
                total += float(expense[0])
            print(f"Catagory: {catagory}; Total: {total}")
    return all_expenses


def delete_expense(num):
    with open("src/expenses.txt", "r") as file:
        lines = file.readlines()

    if num < 1 or num > len(lines):
        print("Invalid line")
        return

    lines.pop(num - 1)
    with open("src/expenses.txt", "w") as file:
        file.writelines(lines)
    print(f"Expense {num} deleted!")
