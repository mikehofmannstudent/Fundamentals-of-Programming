print("\nBUCKET LIST BUILDER\n")
bucket = []
choice = input("Enter selection (e(X)it, (A)dd, (D)elete, (L)ist): ").upper()
while choice [0] != "X":
    if choice[0] == "A":
        print("Enter list item: ")
        newitem = input()
        bucket.append(newitem)
    elif choice[0] == "D":
        print("Enter item to delete: ")
        delItem = input()
        if delItem in bucket:
            bucket.remove(delItem)
        else:
            print("Item is not in list. (Check spelling)")
    elif choice[0] == "L":
        for item in bucket:
            print(item)
    else:
        print("Invalid selection.")
    choice = input("Enter selection (e(X)it, (A)dd, (D)elete, (L)ist):").upper()
