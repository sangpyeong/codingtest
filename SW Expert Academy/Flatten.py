for tc in range(1, 11):
    N = int(input())
    datas = list(map(int, input().split()))
    graph = [0] * 101
    for data in datas:
        graph[data] += 1
    s, e = 1, 100
    mn, mx = 100, 1
    for i in range(99):
        if mn == 100 and graph[s] != 0:
            mn = s
        if mx == 1 and graph[e] != 0:
            mx = e
        if mx != 1 and mn != 100:
            break
        s += 1
        e -= 1
    for i in range(N):
        graph[mn] -= 1
        graph[mn+1] += 1
        graph[mx] -= 1
        graph[mx-1] += 1
        if graph[mn] == 0:
            mn += 1
        if graph[mx] == 0:
            mx -= 1

    print(f"#{tc} {mx-mn}")
