# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
INF = int(1e9)
# 2차원 리스트(그래프 표현) 설정, 모든 값을 무한으로 초기화
road = [[INF] * (n+1) for _ in range(n + 1)]


# 자기 자신에서 자기 자신으로 가는 비용(대각선)은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            road[a][b] == 0

for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1으로 설정
    a, b = map(int, input().split())
    road[a][b] = 1
    road[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 K 입력 받기
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            road[a][b] = min(road[a][b], road[a][k] + road[k][b])

# 수행된 결과를 출력
distance = road[1][k] + road[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
    print("-1")
# 도달할 수 있다면, 최단 거리를 출력
else:
    print(distance)
