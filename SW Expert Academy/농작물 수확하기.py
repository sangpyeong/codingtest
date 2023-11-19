T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [[] for _ in range(N)]
    answer = 0
    mn, mx = int(N / 2), int(N / 2)
    for i in range(int(N/2)):
        graph[i] = list(map(int, input()))
        for j in range(mn, mx+1):
            answer += graph[i][j]
        mx, mn = mx + 1, mn - 1
    graph[int(N/2)] = list(map(int, input()))
    answer += sum(graph[int(N/2)])
    mx, mn = mx - 1, mn + 1
    for i in range(int(N/2)+1, N):
        graph[i] = list(map(int, input()))
        for j in range(mn, mx+1):
            answer += graph[i][j]
        mx, mn = mx - 1, mn + 1
    print(f"#{tc} {answer}")