from collections import deque

dx = [1, 0]
dy = [0, 1]


def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    dp[0][0] = 1

    q = deque()
    q.append([0, 0])
    while q:
        x, y = q.popleft()

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if not 0 <= nx < n or not 0 <= ny < m:
                continue
            if [ny + 1, nx + 1] in puddles:
                continue
            if visited[nx][ny]:
                continue
            q.append([nx, ny])
            visited[nx][ny] = True
            bx = nx - 1
            by = ny - 1
            if 0 <= bx < n:
                dp[nx][ny] += dp[bx][ny]
            if 0 <= by < m:
                dp[nx][ny] += dp[nx][by]
            dp[nx][ny] = dp[nx][ny] % 1000000007
    return dp[n-1][m-1]
