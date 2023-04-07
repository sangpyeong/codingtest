n = list(map(int, input()))

result = 0
for i in n:
    if i == 0 or i == 1 or result == 0:
        result += i
    else:
        result *= i

print(result)
