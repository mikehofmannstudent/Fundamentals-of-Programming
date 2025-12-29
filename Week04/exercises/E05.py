def numberRange(list):
    list.sort()
    min = list[0]
    max = list[-1]
    return (min, max)

numList = []
for i in range(1, 6):
    num = int(input(f"Enter a number ({i}/5): "))
    numList.append(num)

min, max = numberRange(numList)

print("Min: ", min)
print("Max: ", max)
