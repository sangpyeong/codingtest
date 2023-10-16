N = int(input())
E = int(input())

graph = [[] for _ in range(N+1)]

for i in range(E):
    edge = list(map(int, input().split()))
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

visited = [False] * (N+1)
visited[1] = True
answer = 0


def dfs(cur):
    global answer

    for n in graph[cur]:
        if visited[n] == False:
            visited[n] = True
            answer += 1
            dfs(n)


dfs(1)

print(answer)
