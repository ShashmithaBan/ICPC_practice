#This is a hackathon related python script

x =  input()
y = input()

int1 = int(x, 2)
int2 = int(y, 2)

tot = int1 ^ int2

print(bin(tot)[2:].zfill(len(x)))