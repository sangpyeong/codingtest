from collections import deque
n = int(input())
A, B = list(map(int, input().split()))
E = int(input())
graph = [[] for _ in range(n+1)]

for i in range(E):
    edge = list(map(int, input().split()))
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

visited = [-1] * (n+1)
visited[B] = 0
dq = deque([B])
while dq:
    cur = dq.pop()
    for i in graph[cur]:
        if visited[i] != -1:
            continue
        dq.appendleft(i)
        visited[i] = visited[cur] + 1

print(visited[A])
