array = input()

c0 = 0
c1 = 0

if array[0] == '0':
    c0 += 1
else:
    c1 += 1

for i in range(0, len(array)-1):
    if array[i] != array[i+1]:
        if array[i] == '1':
            c0 += 1
        else:
            c1 += 1

print(min(c0, c1))
