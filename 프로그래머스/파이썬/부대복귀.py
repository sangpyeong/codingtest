from collections import deque


def solution(n, roads, sources, destination):
    answer = [-1] * len(sources)

    def bfs(start):
        q = deque()
        q.append([start, 0])
        visited = set()
        visited.add(start)
        while q:
            cur, distance = q.popleft()

            if cur in set_sources:
                result.append([cur, distance])

            if not set_sources:
                return

            for node in graph[cur]:
                if node in visited:
                    continue
                visited.add(node)
                q.append([node, distance + 1])

        return
    # 그래프 문제, bfs로 했는데 시간초과, destination을 bfs하면 해결됨
    graph = [[] for _ in range(n+1)]
    for i, [s, e] in enumerate(roads):
        graph[s].append(e)
        graph[e].append(s)
    set_sources = set(sources)
    result = []
    bfs(destination)
    for i, [s, d] in enumerate(result):
        answer[sources.index(s)] = d

    return answer
