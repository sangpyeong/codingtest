from collections import deque

# BFS 메서드 정의


def bfs(graph, start, visited):
    # 큐(Queue) 구현 위해 deque 라이브러리 사용
    queue = deque([start])      # 첫번째 과정) 시작 노드를 큐에 넣음
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()         # 가장 먼저 들어온 원소 꺼냄
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드가 연결된 정보를 표현 (2차원 리스트)
# 인접리스트 방식으로 그래프 표현
graph = [
    [],         # 보통 노드는 1번부터 시작하므로 인덱스 0은 비움
    [2, 3, 8],  # 1번 노드와 연결된 2, 3, 8번 노드
    [1, 7],     # 2번 노드와 연결된 1, 7번 노드
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
bfs(graph, 1, visited)      # 출력: 1 2 3 8 7 4 5 6
