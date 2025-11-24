def mean(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    mean = sum / len(array)
    return mean


numArray = []

for i in range(3):
    num = int(input(f"Enter number ({i}/3): "))
    numArray.append(num)

print(mean(numArray))
