n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    return None


A.sort()
B.sort()

for i in B:
    if binary_search(A, i, 0, n-1) != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")
