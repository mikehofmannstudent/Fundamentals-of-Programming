try:
    dividend = int(input("Please entere the divident: "))
except ValueError:
    print("The divident has to be a number!")

try:
    divisor = int(input("Please entere the divisor: "))
except ValueError:
    print("The divisor has to be a number!")

try:
    print("%d / %d = %f" % (dividend, divisor, dividend / divisor))
except ZeroDivisionError:
    print("The divisor cannot be zero!")
except NameError:
    print("The divident/divisor has to be a number!")
