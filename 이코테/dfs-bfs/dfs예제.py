# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 표현 (2차원 리스트)
# 인접리스트 방식으로 그래프 표현
graph = [
    [],         	# 보통 노드는 1번부터 시작하므로 인덱스 0은 비움
    [2, 3, 8],  	# 1번 노드와 연결된 2, 3, 8번 노드
    [1, 7],     	# 2번 노드와 연결된 1, 7번 노드
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
# default는 False
visited = [False] * 9   # 인덱스 0은 사용 X, 노드8개+1의 크기의 리스트

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)      # 출력: 1 2 7 6 8 3 4 5
