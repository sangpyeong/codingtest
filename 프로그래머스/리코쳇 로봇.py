from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solution(board):
    answer = -1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                R = [i, j, 0]
    dq = deque([R])
    visited = set()

    while dq:
        y, x, t = dq.popleft()

        if board[y][x] == 'G':
            answer = t
            return answer
        if (y, x) in visited:
            continue
        visited.add((y, x))

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] != 'D':
                nx, ny = nx + dx[i], ny + dy[i]

            if not (ny-dy[i], nx-dx[i]) in visited:
                dq.append([ny-dy[i], nx-dx[i], t+1])

    return answer
