import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv,
    "%": operator.mod
}

operator = input("Enter an operator (+, -, *, /, //, %): ")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if operator in ops:
    selectedOp = ops[operator]
    result = selectedOp(num1, num2)
    print(f"Result: {result}")
else:
    print("Invalid operator.")