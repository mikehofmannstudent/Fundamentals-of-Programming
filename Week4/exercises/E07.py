import numpy as np

def distance2D(point1, point2):
    points = point1 - point2
    distance = (points[0]**2 + points[1]**2)**0.5
    return distance


numArray = []
for i in range(1,3):
    num = int(input(f"Enter a number (Array1: {i}/2): "))
    numArray.append(num)
p1 = np.array([numArray[0], numArray[1]])

numArray = []
for i in range(1,3):
    num = int(input(f"Enter a number (Array2: {i}/2): "))
    numArray.append(num)
p2 = np.array([numArray[0], numArray[1]])

print(distance2D(p1, p2))
