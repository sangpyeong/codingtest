# N X M 크기의 얼음 틀이 있다.
# 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1 표시
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우
# 서로 연결되어 있는 것으로 간주
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는
# 총 아이스크림의 개수를 구하는 프로그램을 작성
# 연결요소 찾는 문제!
from collections import deque


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:      # 범위 벗어나면
        return False                                # 즉시 종료
    if graph[x][y] == 0:        # 현재 노드가 방문 X면
        graph[x][y] = 1         # 방문 처리
        # 상/하/좌/우 방문 처리 재귀 호출
        # return 값 사용 X 단순히 연결된 모든 노드 방문 처리
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드에 음료수 채우기
cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:   # 방문처리를 처음하는 시작 노드만
            cnt += 1            # 카운트

print(cnt)

# dfs의 재귀함수를 사용해서 좌표를 편하게 이동하면서 1로 만드는 방법 알게 됨, 좌표가 나오기 때문에 인접 행렬을 사용하는 것이 좋음, visited가 굳이 필요 없었음
