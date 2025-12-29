text = "Python"

# slice 5 to 3 (2-(-1)) with a step of -1
# index -> 5 4 3
text3 = text[5:2:-1]
print(text3) # noh

# slice from 5 to 0 with a step of -1
# index -> 5 4 3 2 1 0
text4 = text[::-1]
print(text4) # nohtyP <- reverse the string

# slice from 5 to 2 (1-(-1)) with a step of -1
# index -> 5 4 3 2
text5 = text[:1:-1]
print(text5) # noht

# slice from 5 to 0 with a step of -2
# index -> 5 3 1
text6 = text[::-2]
print(text6) # nhy

# slice from 5 to 3 (2-(-1)) with a step of -2
# index -> 5 3
text7 = text[:2:-2]
print(text7) #nh
