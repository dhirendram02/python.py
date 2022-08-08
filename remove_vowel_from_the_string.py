string = input()

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
newstr = ""
strlen = len(string)

for i in range(strlen):
    if string[i] not in vowels:
        newstr = newstr + string[i]

string = newstr
print(string)
