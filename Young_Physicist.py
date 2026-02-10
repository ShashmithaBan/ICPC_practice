n = int(input())

a = []

for i in range(n):
    x, y, z = map(int, input().split())
    a.append((x, y, z))

x_sum = 0
y_sum = 0
z_sum = 0

for i in range(n):
    x_sum += a[i][0]
    y_sum += a[i][1]
    z_sum += a[i][2]    

if x_sum == 0 and y_sum == 0 and z_sum == 0:
    print("YES")
else:
    print("NO")