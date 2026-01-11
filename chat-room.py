string = input()
target = 'hello'
pointer = 0
for char in string:
        if char == target[pointer]:
            pointer += 1
        if pointer == len(target):
            print("YES")
            break
else:
    print("NO")