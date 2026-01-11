#This is a hackathon related python script

x = int(raw_input())
a = []
for i in range(x):
    y = raw_input()
    a.append(y)


for i in range (len(a)):
    a[i] = a[i].split()

b = []

for i in range(len(a)):
    if a[i][1] == "rat":
        b.append(a[i][0])

for i in range(len(a)):
    if a[i][1] == "woman" or a[i][1] == "child":
        b.append(a[i][0])

for i in range(len(a)):
    if a[i][1] == "man":
        b.append(a[i][0])

for i in range(len(a)):
    if a[i][1] == "captain":
        b.append(a[i][0])


print("\n".join(b))