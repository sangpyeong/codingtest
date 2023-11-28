from collections import deque

dx = [1, 0, -1, 0]  # 상 우 하 좌
dy = [0, 1, 0, -1]


def calculate_day(map, x, y, visited):
    result = 0
    q = deque([(x, y)])
    visited[x][y] = True
    while (q):
        tx, ty = q.popleft()
        result += int(map[tx][ty])
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if nx >= 0 and nx < len(map) and ny >= 0 and ny < len(map[0]) and map[nx][ny] != "X" and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    return result


def solution(maps):
    answer = []
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "X" or visited[i][j]:
                continue
            answer.append(calculate_day(maps, i, j, visited))
    answer.sort()
    if len(answer) == 0:
        answer = [-1]
    return answer
