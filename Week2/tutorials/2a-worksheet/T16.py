#          0    1    2    3    4    5
letters = ['A', 'B', 'C', 'D', 'E', 'F']

# slice from index 0 to 4-1 (3)
print(letters[0:4]) # ['A', 'B', 'C', 'D']

# slice from index 2 to 5-1 (4)
print(letters[2:5]) # ['C', 'D', 'E']

# slice from index 0 to 5-1 (4)
print(letters[:5]) # ['A', 'B', 'C', 'D', 'E']

# slice from index 1 to the end
print(letters[1:]) # ['B', 'C', 'D', 'E', 'F']

# slice from index 1 to 4-1, step of 2
# extract from index [1, 3]
print(letters[1:4:2]) # ['B', 'D']

# slice from index 0 to the end, step of 2
# extract from index [0, 2, 4]
print(letters[::2]) # ['A', 'C', 'E']
