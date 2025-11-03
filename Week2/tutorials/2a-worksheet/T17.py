# 0 to 5-1 (4)
list1 = list(range(5))
print(list1)

# 2 to 13-1 (12)
list2 = list(range(2, 13))
print(list2)

# 2 to 13-1 (12) with steps of 2
list3 = list(range(2, 13, 2))
print(list3)

# 2 to 12-1 (11) with steps of 3
list4 = list(range(2, 12, 3))
print(list4)

# 5 to -1-(-1) (0)
list5 = list(range(5, -1, -1))
print(list5) # [5, 4, 3, 2, 1, 0]

# 5 to 0-(-1) (1)
list6 = list(range(5, 0, -1))
print(list6) # [5, 4, 3, 2, 1]

# 10 to -1-(-1) (0) step of -2
list7 = list(range(10, -1, -2))
print(list7) # [10, 8, 6, 4, 2, 0]

# 10 to 0-(-1) (1) steps of -3
list8 = list(range(10, 0, -3))
print(list8) # [10, 7, 4, 1]
