import statistics as stats

exit = False
numbers = []

while not exit:
    numberStr = input("Enter a number or continue with 'q': ")

    if numberStr == 'q':
        exit = True
        break

    numbers.append(int(numberStr))

print(f"Largest number: {max(numbers)}")
print(f"Lowerst number: {min(numbers)}")
print(f"Average: {stats.mean(numbers)}")
print(f"Sample standard deviation: {stats.stdev(numbers)}")
    
