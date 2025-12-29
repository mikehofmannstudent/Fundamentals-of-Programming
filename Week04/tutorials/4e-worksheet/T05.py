import math

def circleArea(radius):
    area = math.pi * radius**2
    return area

radius1 = 4.5
area1 = circleArea(radius1)
print(f"radius: {radius1}\tarea: {area1}")

radius2 = 10
area2 = circleArea(radius2)
print(f"radius: {radius2}\tarea: {area2}")
