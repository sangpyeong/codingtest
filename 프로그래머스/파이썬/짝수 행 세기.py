def solution(a):
    answer = -1

    row = []
    for i in range(len(a)):
        row.append(sum(a[i]))
    print(row)

    col = []
    for j in range(len(a[0])):
        total = 0
        for i in range(len(a)):
            if a[i][j] == 1:
                total += 1
        col.append(total)
    print(col)

    return answer
