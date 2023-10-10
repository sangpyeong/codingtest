from copy import deepcopy
from itertools import permutations
from collections import defaultdict, deque

# 내 풀이 실패


def solution(board, r, c):
    answer = 0
    # 1 ~ 6까지 순열 구해서 순서에 맞게 모든 경우를 구하는 방법

    # 현재 위치에서 각 그림 위치까지 거리 구하고
    def dis(r, c):
        table = [[0] * 4 for _ in range(4)]

        for i in range(4):
            for j in range(4):
                if i == r and j == c:
                    table[i][j] = 0
                elif i == r or j == c:
                    table[i][j] = 1
                elif abs(i-r) == 1 and abs(j-c) == 1:
                    table[i][j] = 2
                elif (i == 3 or i == 0) and (j == 3 or j == 0):
                    table[i][j] = 2
                elif (i == 3 or i == 0):
                    table[i][j] = 1 + abs(j-c)
                elif (j == 3 or j == 0):
                    table[i][j] = 1 + abs(i-r)
                else:
                    table[i][j] = abs(i-r) + abs(j-c)

        return table
    row, col = r, c
    sm = 0
    for i in range(4):
        sm += sum(board[i])
    while sm != 0:
        tmp_table = dis(row, col)
        mn = 4
        point = []
        for i in range(4):
            for j in range(4):
                if board[i][j] != 0:
                    if tmp_table[i][j] < mn:
                        point = [i, j]
                        mn = tmp_table[i][j]
        answer += mn + 1
        number = board[point[0]][point[1]]
        next_point = []
        for i in range(4):
            check = False
            for j in range(4):
                if i == point[0] and j == point[1]:
                    continue
                if board[i][j] == number:
                    next_point = [i, j]
                    check = True
                    break
            if check:
                break
        tmp_table = dis(point[0], point[1])
        answer += tmp_table[next_point[0]][next_point[1]] + 1
        board[point[0]][point[1]] = 0
        board[next_point[0]][next_point[1]] = 0
        row = next_point[0]
        col = next_point[1]
        sm = 0
        for i in range(4):
            sm += sum(board[i])

    return answer


# 다른 풀이
def move_cost(board, start, end):   # 조작 횟수 Count
    if start == end:
        return 0
    queue, visit = deque([[start[0], start[1], 0]]), {start}
    while queue:                    # BFS
        x, y, c = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x+dx, y+dy     # Normal move
            cx, cy = x, y
            while True:             # Ctrl + move
                cx, cy = cx+dx, cy+dy
                if not (0 <= cx <= 3 and 0 <= cy <= 3):
                    cx, cy = cx-dx, cy-dy
                    break
                elif board[cx][cy] != 0:
                    break

            if (nx, ny) == end or (cx, cy) == end:  # 도착 최단 경로
                return c+1

            if (0 <= nx <= 3 and 0 <= ny <= 3) and (nx, ny) not in visit:
                queue.append((nx, ny, c+1))
                visit.add((nx, ny))
            if (cx, cy) not in visit:
                queue.append((cx, cy, c+1))
                visit.add((cx, cy))


def cls_cost(board, cdict, curr, order, cost):
    if len(order) == 0:
        return cost   # 모든 카드를 확인한 경우
    idx = order[0]+1                # 현재 선택해야할 카드의 종류

    # 현재위치에서 A1까지의 조작 횟수 + A1->A2까지의 조작 횟수 + 2(카드 선택)
    choice1 = move_cost(
        board, curr, cdict[idx][0]) + move_cost(board, cdict[idx][0], cdict[idx][1]) + 2
    choice2 = move_cost(
        board, curr, cdict[idx][1]) + move_cost(board, cdict[idx][1], cdict[idx][0]) + 2

    # 선택한 카드는 board에서 0으로 변경
    new_board = deepcopy(board)
    new_board[cdict[idx][0][0]][cdict[idx][0][1]] = 0
    new_board[cdict[idx][1][0]][cdict[idx][1][1]] = 0

    if choice1 < choice2:   # 적은 조작 횟수를 한 경우를 따라 재귀
        return cls_cost(new_board, cdict, cdict[idx][1], order[1:], cost + choice1)
    else:
        return cls_cost(new_board, cdict, cdict[idx][0], order[1:], cost + choice2)


def solution(board, r, c):
    answer = float('inf')
    cdict = defaultdict(list)
    for row in range(4):        # 카드의 종류에 따라 좌표 저장
        for col in range(4):
            num = board[row][col]
            if num != 0:
                cdict[num].append((row, col))

    for case in permutations(range(len(cdict)), len(cdict)):    # 완전 탐색
        answer = min(answer, cls_cost(board, cdict, (r, c), case, 0))

    return answer
