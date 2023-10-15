import math
from collections import deque, defaultdict
import heapq
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 내 풀이 틀림


def solution(land, height):
    answer = 0
    # bfs로 풀자
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

    def visit():
        for i in range(N):
            for j in range(N):
                if visited[i][j] == False:
                    return True
        return False

    while visit():
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
                if land[x][y] + height < land[nx][ny]:
                    continue
                dq.appendleft([nx, ny])

        diff = 10000
        np = []
        for i in range(N):
            for j in range(N):
                if visited[i][j] == True:
                    for k in range(4):
                        ni = i + dx[k]
                        nj = j + dy[k]
                        if not (0 <= ni < N) or not (0 <= nj < N):
                            continue
                        if visited[ni][nj] == True:
                            continue
                        if diff > abs(land[i][j] - land[ni][nj]):
                            diff = abs(land[i][j] - land[ni][nj])
                            np = [ni, nj]
        dq.appendleft(np)
        if diff != 10000:
            answer += diff

    return answer


# 다른 풀이 heap사용
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solution(land, height):
    n = len(land)
    visited = [[False]*n for _ in range(n)]
    heap = [[0, 0, 0]]
    answer = 0

    while heap:
        v, x, y = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = True
        answer += v
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if abs(land[x][y] - land[nx][ny]) > height:
                    heapq.heappush(
                        heap, [abs(land[x][y] - land[nx][ny]), nx, ny])
                else:
                    heapq.heappush(heap, [0, nx, ny])
    return answer


# 다른 풀이 크루스칼 알고리즘


def find_root(x, root):
    if x == root[x]:
        return x
    else:
        r = find_root(root[x], root)
        root[x] = r
        return r


def union_find(x, y, root):
    x_root = find_root(x, root)
    y_root = find_root(y, root)
    root[y_root] = x_root


def BFS(land, height, check, loc, group, N):
    direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    q = deque()
    q.append(loc)
    check[loc[0]][loc[1]] = group

    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or check[nx][ny]:
                continue
            if abs(land[nx][ny] - land[x][y]) <= height:
                q.append([nx, ny])
                check[nx][ny] = group


def find_ladder(check, land, N):
    direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    ladders = defaultdict(lambda: math.inf)

    for i in range(N):
        for j in range(N):
            current = check[i][j]
            for dx, dy in direction:
                nx, ny = i + dx, j + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N or check[nx][ny] == current:
                    continue
                dist = abs(land[i][j] - land[nx][ny])
                ladders[(current, check[nx][ny])] = min(
                    dist, ladders[(current, check[nx][ny])])
    return ladders


def kruskal(ladders, group):
    sum = 0
    roots = {_: _ for _ in range(1, group)}
    for (x, y), value in ladders:
        if find_root(x, roots) != find_root(y, roots):
            union_find(x, y, roots)
            sum += value
        if len(roots.items()) == 1:
            return sum
    return sum


def solution(land, height):
    answer = 0
    N = len(land)
    check = [[0 for _ in range(N)] for _ in range(N)]

    group = 1
    for i in range(N):
        for j in range(N):
            if not check[i][j]:
                BFS(land, height, check, [i, j], group, N)
                group += 1

    ladders = find_ladder(check, land, N)
    ladders = sorted(ladders.items(), key=lambda x: x[1])

    answer = kruskal(ladders, group)
    return answer
