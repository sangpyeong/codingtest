#시간초과, 생각한 방법은 같음, 나는 조합을 썻지만 정답은 재귀함수 안에 반복문으로 해결
#조합이 필요하다고 생각하면 재귀함수에 반복문 사용해서 풀기


from itertools import combinations
from collections import deque

n, m = map(int, input().split())
graph = [[0]*m for i in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))

empty = []
virus = []
result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append([(i, j)])

for walls in combinations(empty, 3):
    #벽 3개 추가한 그래프 만들기
    tmpgraph = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            tmpgraph[i][j] = graph[i][j]
    for wall in walls:
        tmpgraph[wall[0][0]][wall[0][1]] = 1
    
    #바이러스 위치 찾기
    for i in range(n):
        for j in range(m):
            if tmpgraph[i][j] ==2:
                virus.append([i,j])

    #bfs
    q = deque([])

    for x, y in virus:
        q.append([x,y])
    while q:
        x, y = q.popleft()
        if x+1 <n :
            if tmpgraph[x+1][y]==0:
                q.append([x+1,y])
                tmpgraph[x+1][y] =2
        if x-1 >=0:
            if tmpgraph[x-1][y]==0:
                q.append([x-1,y])
                tmpgraph[x-1][y] =2
        if y+1 <n :
            if tmpgraph[x][y+1]==0:
                q.append([x,y+1])
                tmpgraph[x][y+1] =2
        if y-1 >=0:
            if tmpgraph[x][y-1]==0:
                q.append([x,y-1])
                tmpgraph[x][y-1] =2
            
    #답 구하기
    empty_sum=0
    for i in range(n):
        for j in range(m):
            if tmpgraph[i][j]== 0:
                empty_sum+=1
    result = max(result, empty_sum)

print (result)

#정답 
# # BOJ에서는 [언어]를 PyPy3로 설정하여 제출해주세요.

n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매 번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최대값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리를 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)          