import re

p = re.compile(r'[cbm]at')
# first letter in the re must be c, b or m then followed by 'at'
strings_to_test = ['cat', 'bat', 'mat', 'caa', 'dat', 'xcat', 'ca', 'ct']

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
