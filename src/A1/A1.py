# name: str = input("Enter your name: ")
# print(f"Hello, {name}!") #possible error here with incorrect types. Type annotations used for that

print("Welcome to the Personal Finance Calculator!")
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))
savings_goal = float(input("Enter your desired monthly savings goal: "))
savings = income - expenses
print(f"Your monthly savings is: ${savings}")