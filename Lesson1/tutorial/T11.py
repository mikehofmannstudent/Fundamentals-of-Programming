# L-Local F-Foreign E-Exchange V-Visitor
std_type = input("Enter a letter (L-Local, F-Foreign, E-Exchange, V-Visitor): ")

if(std_type == "L" or std_type == "F"):
    print("10% discount")

elif(std_type == "E"):
    print("5% discount")
else:
    print("No discount")
