gender = input("Enter your gender (M-Male, F-Female): ")
age = int(input("Enter your age: "))

if((gender == "M" and age >= 15) or (gender == "F" and age >= 16)):
    print("You may enter the sports competition.")
else:
    print("You are too young and may NOT enter the sports competition.")