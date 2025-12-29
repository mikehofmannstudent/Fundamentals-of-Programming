def areaCircle(radius):
    area = 3.142 * radius**2
    return area

def areaTriangle(base, height):
    area = (base * height) / 2
    return area

totalArea = 2 * areaCircle(6) + areaTriangle(10, 5) - areaTriangle(3, 2)
print(totalArea)
