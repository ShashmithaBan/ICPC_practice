n , k  = map(int, input().split())

def is_prime(num):
    if num <=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


c = []

for i in range(2, n+1):
    if is_prime(i):
        c.append(i)

count = 0 

for i in range(len(c)-1):
    j = c[i] + c[i+1] + 1
    for m in range(i+2,len(c)):
        if j == c[m]:
            count += 1

if count >= k:
    print("YES")
else:
    print("NO")