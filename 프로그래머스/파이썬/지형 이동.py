from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(land, height):
    answer = 0
    # bfs로 풀자
    # 가장 작은 곳 위치 부터 시작? ㅇㅇ
    N = len(land)
    mn = 10000
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if mn > land[i][j]:
                mn = land[i][j]
                x, y = i, j

    dq = deque([(x, y)])
    visited = [[False] * N for _ in range(N)]
    mx = land[x][y]
    while dq:
        x, y = dq.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N) or not (0 <= ny < N):
                continue
            if visited[nx][ny] == True:
                continue
            if mx + height < land[nx][ny]:
                continue
            mx = max(mx, land[nx][ny])
            dq.append([nx, ny])

    print(visited)

    return answer
