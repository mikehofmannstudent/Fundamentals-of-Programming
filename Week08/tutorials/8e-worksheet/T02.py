import re

p = re.compile(r'[tes]')
# as long as the re matches one of the charaters 'tes'
string_to_test = ['test', 'est', 'st', 'tea', 'abc', 'es', 'aes']

# testing
print("match to beginning of the string")
for s in string_to_test:
    r = p.match(s)
    if(r):
        print(s)

print()
print("search - match to anywhere in the string")
for s in string_to_test:
    r = p.search(s)
    if(r):
        print(s)
