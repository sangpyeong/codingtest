n = int(input())

arr = []
for i in range(n):
    tp = input().split()
    print(tp)
    arr.append((tp[0], int(tp[1])))

print(arr)

arr = sorted(arr, key=lambda student: student[1])

for student in arr:
    print(student[0], end=" ")
