import math

def circleArea(radius):
    area = math.pi * radius**2
    return area

noOfCircles = 3
circleRadius = []

for i in range(noOfCircles):
    radius = float(input("Enter circle radius: "))
    circleRadius.append(radius)

totalArea = 0
for radius in circleRadius:
    area = circleArea(radius)
    totalArea += area

totalArea = round(totalArea, 2)

print(f"Total area of all circles: {totalArea}")
