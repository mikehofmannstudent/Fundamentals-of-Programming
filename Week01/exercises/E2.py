from datetime import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))
today = datetime.now()

year = today.year + (100 - age)

print(f"Hello {name}, you will turn 100 in the year {year}.")
