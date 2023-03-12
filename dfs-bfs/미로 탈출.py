# 동빈이는 N X M 크기의 직사각형 형태의 미로에 갇혔다.
# 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
# 동빈이의 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하고
# 한 번에 한 칸씩 이동할 수 있다.
# 이때 괴물이 있는 부분은 0으로 없는 부분은 1로 표시되어 있다.
# 미로는 반드시 탈출할 수 있는 형태로 제시된다.
# 이때, 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개순느?
# 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해 계산한다.

# 내가 풀던 거
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


def bfs(graph, x, y):
    result = 0
    queue = deque([(x, y)])
    while queue:
        nx, ny = queue.popleft()
        graph[nx][ny] = 0
        result += 1
        if nx == n-1 and ny == m-1:
            break
        if nx - 1 > -1 and nx - 1 < n and ny > -1 and ny < m and graph[nx-1][ny] == 1:
            queue.append((nx-1, ny))
        if nx+1 > -1 and nx+1 < n and ny > -1 and ny < m and graph[nx+1][ny] == 1:
            queue.append((nx+1, ny))
        if nx > -1 and nx < n and ny-1 > -1 and ny-1 < m and graph[nx][ny-1] == 1:
            queue.append((nx, ny-1))
        if nx > -1 and nx < n and ny+1 > -1 and ny+1 < m and graph[nx][ny+1] == 1:
            queue.append((nx, ny+1))
    return result


print(bfs(graph, 0, 0))


# 정답

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):      # 현재 위치에서 4가지 방향으로 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 미로의 범위 벗어나면
                continue                                # 무시
            if graph[nx][ny] == 0:      # 괴물이 존재하면
                continue                # 무시
            if graph[nx][ny] == 1:      # 해당 노드 처음 방문 일때
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]          # 가장 오른쪽 아래의 값(최단 거리) 반환


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 4가지 이동 방향 정의 (상/하/좌/우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))

# 좌표에 1씩 더하면서 결과 구하는 것, dx,dy활용 법 익힘
