#시간 초과, deque는 안에 하나의 값이라고 생각함, 따로 거리 리스트를 만들면 시간초과 해결됨 
from collections import deque


def bfs(graph, start, visited):
    queue = deque([(start, 0)])
    visited[start] = True
    while queue:
        v, distance = queue.popleft()
        if distance == k:
            result.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append([i, distance+1])
                visited[i] = True


n, m, k, x = map(int, input().split())
arr = [[] for i in range(n+1)]
result = []
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

visited = [False]*(n+1)

bfs(arr, x, visited)

if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)


#정답 
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)