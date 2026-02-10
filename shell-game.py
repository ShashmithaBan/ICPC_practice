n = int(input())

cup = [0, 0, 0]
cup[n-1] = 1

for i in range(3):
    x, y = map(int, input().split())
    cup[x-1], cup[y-1] = cup[y-1], cup[x-1]


for i in range(3):
    if cup[i] == 1:
        print(i+1)