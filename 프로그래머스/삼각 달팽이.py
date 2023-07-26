def solution(n):
    triangle = [[]*i for i in range(n)]
    tripple = 0
    index = 0
    num = 1
    for i in range(n, 0, -1):
        if tripple % 3 == 0:
            for j in range(1, i+1):
                triangle[index].insert(tripple//3, num)
                num += 1
                index += 1
            tripple += 1
            index -= 1
        elif tripple % 3 == 1:
            for j in range(i):
                triangle[index].insert(tripple//3 + j + 1, num)
                num += 1
            index -= 1
            tripple += 1
        elif tripple % 3 == 2:
            for j in range(1, i+1):
                if tripple//3 == 0:
                    triangle[index].append(num)
                else:
                    triangle[index].insert(
                        len(triangle[index]) - tripple//3, num)
                num += 1
                index -= 1
            tripple += 1
            index += 2
    answer = []
    for i in range(n):
        answer.extend(triangle[i])

    return answer

# 다른 풀이


def solution(n):
    res = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:      # 아래
                x += 1
            elif i % 3 == 1:    # 오른쪽
                y += 1
            elif i % 3 == 2:    # 위
                x -= 1
                y -= 1
            res[x][y] = num
            num += 1

    for i in res:
        for j in i:
            if j:
                answer.append(j)
    return answer
