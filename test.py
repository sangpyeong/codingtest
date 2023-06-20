arr = list(map(int, input().split()))
arr.sort()
result = []
consequence = 1
for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        consequence += 1
    elif consequence != 1:
        result.append(consequence)
        consequence = 1
if consequence != 1:
    result.append(consequence)

if len(result) == 0:
    result.append(-1)
    print(result)
else:
    print(result)
