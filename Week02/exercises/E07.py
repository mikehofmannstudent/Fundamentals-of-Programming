import statistics as stats

numbers = []

for i in range(5): 
    number = int(input(f"Enter numer {i + 1}/5: "))
    numbers.append(number)

print(f"Lowest number: {min(numbers)}")
print(f"Largest number: {max(numbers)}")
print(F"Average: {stats.mean(numbers)}")

