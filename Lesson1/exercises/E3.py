temp = int(input("Enter an int (temperature of water): "))
state = ""

if(temp >= 100):
    state = "gas"
elif(temp > 0 and temp < 100):
    state = "liquid"
else:
    state = "solid"

print(f"At {temp}°C, water is in a {state} state.")
