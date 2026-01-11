string = input()

counUpper = countLower = 0 

for char in string:
    if char.isupper():
        counUpper += 1
    else:
        countLower += 1

if counUpper > countLower:
    print(string.upper())
else:
    print(string.lower())