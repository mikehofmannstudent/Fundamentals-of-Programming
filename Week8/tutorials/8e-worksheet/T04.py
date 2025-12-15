import re

p = re.compile(r'[^5]')
# first re letter must not be 5
strings_to_test = ['555','512', '215', '5', '222']

# testing
print("match to beginning of string")
for s in strings_to_test:
    r = p.match(s)
    if(r):
        print(s)

print()
print("search - match to anywhere in the string")
for s in strings_to_test:
    r = p.search(s)
    if(r):
        print(s)
