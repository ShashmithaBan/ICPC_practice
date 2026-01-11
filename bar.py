n = int(input())  


a = []
for i in range(n):
    x =  input()
    if x.isdigit():
        a.append(int(x))
    else:
        a.append(x)



count = 0

b = [ "ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE", "TEQUILA", "VODKA", "WHISKEY", "WINE" ]
for i in range(len(a)):
    if isinstance(a[i], int):
        if a[i] < 18:
            count += 1
    else:
        for j in range (len(b)):
            if a[i] == b[j]:
                count += 1
                break        

print(count)


