n, m = map(int, input().split())
result = 0

for i in range(n):
    arr = list(map(int, input().split()))
    result = min(arr) if min(arr) > result else result

print(result)
