n = int(input())
k = int(input())

arr = [[0] * n for _ in range(n)]

for i in range(k):
    a, b = map(int, input())
    arr[a-1][b-1] = 1

print(arr)
