from copy import deepcopy

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]


def rotate(x, y, lst, rt):
    length = len(lst)
    for k in range(5):
        ax, ay = x + dx[k], y + dy[k]
        if -1 < ax < length and -1 < ay < length:
            lst[ay][ax] = (lst[ay][ax] + rt) % 4


def solution(clockHands):
    answer = float('inf')
    length = len(clockHands)

    for i in range(4 ** length):
        tmp = 0
        tmp_clock = deepcopy(clockHands)
        for j in range(length):
            rt = i % 4 ** (j + 1) // 4 ** j
            if rt == 0:
                continue

            rotate(j, 0, tmp_clock, rt)
            tmp += rt

        for y in range(1, length):
            for x in range(length):
                if tmp_clock[y-1][x] == 0:
                    continue
                rt = 4 - tmp_clock[y-1][x]
                rotate(x, y, tmp_clock, rt)
                tmp += rt
        if sum(tmp_clock[-1]) == 0:
            answer = min(answer, tmp)

    return answer


solution([[0, 3, 3, 0], [3, 2, 2, 3], [0, 3, 2, 0], [0, 3, 3, 3]])

# from collections import deque

# dx = [0, 1, 0, -1]#12, 3, 6, 9
# dy = [-1, 0, 1, 0]

# def solution(clockHands):
#     answer = 0
#     N = len(clockHands)
#     #시간초과는 걱정 없을듯, dp로 생각중
#     memo = []
#     dq = deque([(clockHands, 0)])
#     visited = []

#     def rotate(x, y, arr):
#         arr[x][y] = (arr[x][y] + 1) % 4
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < N and 0 <= ny < N:
#                 arr[nx][ny] = (arr[nx][ny] + 1) % 4
#         return arr

#     while True:
#         arr, t = dq.popleft()

#         #정답인 경우
#         total = 0
#         for i in range(N):
#             for j in range(N):
#                 total += arr[i][j]
#         if total == 0:
#             answer = t
#             return answer

#         for i in range(N):
#             for j in range(N):
#                 next_arr = [[0]* N for _ in range(N)]
#                 for k in range(N):
#                     for m in range(N):
#                         next_arr[k][m] = arr[k][m]
#                 result_arr = rotate(i, j, next_arr)
#                 if not result_arr in visited:
#                     dq.append((result_arr,t+1))


#     return answer
