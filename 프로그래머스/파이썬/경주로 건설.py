# 내 풀이 틀림
from sys import maxsize
from heapq import heappop, heappush
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(board):
    answer = 0
    N = len(board)
    INF = float('inf')
    visited = [[INF]*N for _ in range(N)]
    visited[0][0] = 0
    dq = deque([(0, 0, 1), (0, 0, 2)])
    while dq:
        x, y, d = dq.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if not (0 <= nx < N) or not (0 <= ny < N):
                continue
            if board[nx][ny] == 1:
                continue

            cost = 100
            if d != i:
                cost += 500
            if visited[nx][ny] < visited[x][y] + cost:
                continue

            visited[nx][ny] = visited[x][y] + cost
            print(nx, ny)
            print(visited)
            dq.append((nx, ny, i))
    print(visited)
    answer = visited[N-1][N-1]
    return answer


# 다른 풀이


def solution(board):
    N = len(board)
    costBoard = [[[maxsize] * N for _ in range(N)] for _ in range(4)]
    for i in range(4):
        costBoard[i][0][0] = 0

    # BFS
    heap = [(0, 0, 0, 0), (0, 0, 0, 2)]
    while heap:
        cost, x, y, d = heappop(heap)

        # 4방향 이동
        for dx, dy, dd in ((1, 0, 0), (-1, 0, 1), (0, 1, 2), (0, -1, 3)):
            nx, ny = x + dx, y + dy

            # 경계 침범 or 벽
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[ny][nx]:
                continue

            # 이동비용 갱신
            newCost = cost + (100 if d == dd else 600)

            # 최소비용 갱신
            if costBoard[dd][ny][nx] > newCost:
                costBoard[dd][ny][nx] = newCost
                heappush(heap, (newCost, nx, ny, dd))

    return min(costBoard[0][N-1][N-1], costBoard[1][N-1][N-1], costBoard[2][N-1][N-1], costBoard[3][N-1][N-1])
