n, m, k = map(int, input().split())
array = list(map(int, input().split()))
result = 0

array.sort(reverse=True)

for i in range(1, m+1):
    if i % k == 0:
        result += array[1]
    else:
        result += array[0]

print(result)