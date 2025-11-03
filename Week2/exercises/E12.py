print("\nBUCKET LIST BUILDER\n")
bucket = []
choice = input("Enter selection (e(X)it, (A)dd, (L)ist): ")
while choice [0] != "X":
    if choice[0] == "A":
        print("Enter list item: ")
        newitem = input()
        bucket.append(newitem)
    elif choice[0] == "L":
        for item in bucket:
            print(item)
    else:
        print("Invalid selection.")
    choice = input("Enter selection (e(X)it, (A)dd, (L)ist):")
