T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    graph = [[0] * N for _ in range(N)]
    graph[0][0] = 1
    curr = [0, 0]

    def check():
        for g in graph:
            if 0 in g:
                return True
        return False

    while check():
        for i in range(4):
            nx = curr[0] + dx[i]
            ny = curr[1] + dy[i]
            if not ((0 <= nx < N) and (0 <= ny < N)):
                continue
            if graph[nx][ny] != 0:
                continue
            while (0 <= nx < N) and (0 <= ny < N) and graph[nx][ny] == 0:
                graph[nx][ny] = graph[curr[0]][curr[1]] + 1
                curr[0], curr[1] = nx, ny
                nx = nx + dx[i]
                ny = ny + dy[i]

            break
    print('#{}'.format(tc))
    for grap in graph:
        for gra in grap:
            print(gra, end=" ")
        print()