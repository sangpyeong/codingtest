#[]이거 씌우는거 생각, 버리기 trunc, 복습이 필요함



from math import trunc
from collections import deque

n, l, r = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
countrys = []


def posible():
    for i in range(n):
        for j in range(n):
            x, y = i, j
            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                dif = abs(A[nx][ny]-A[x][y])
                if dif >= l and dif <= r:
                    return True
    return False


def dfs(i, j):
    visited = []
    dq = deque([(i, j)])
    while len(dq) != 0:
        x, y = dq.pop()
        visited.append((x, y))
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if (nx, ny) in visited:
                continue
            dif = abs(A[nx][ny]-A[x][y])
            if dif >= l and dif <= r:
                dq.append((nx, ny))
    countrys.append(visited)
    visited = []


day = 0
while posible():
    day += 1
    for i in range(n):
        for j in range(n):
            check = False
            for k in countrys:
                if (i, j) in k:
                    check = True

            if check == True:
                break
            dfs(i, j)

    for i in countrys:
        sum = 0
        aver = 0
        for x, y in i:
            sum += A[x][y]
        aver = trunc(sum/len(i))
        for x, y in i:
            A[x][y] = aver
    countrys = []

print(day)
print(A)

#정답 
from collections import deque

# 땅의 크기(N), L, R 값을 입력받기
n, l, r = map(int, input().split())

# 전체 나라의 정보(N x N)를 입력 받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))
    # 너비 우선 탐색 (BFS)을 위한 큐 라이브러리 사용
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복(BFS)
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가하기
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)