#내가 푼거
import heapq

def dijkstra(start, graph, n):
    distance = [1000000] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for node in graph[now]:
            if dist + node[1] < distance[node[0]]:
                distance[node[0]] = dist + node[1]
                heapq.heappush(q, (dist + node[1], node[0]))
    
    return distance

def solution(n, s, a, b, fares):
    answer = 1e9
    #a, b, s에서 다익스트라로 전부 최소 거리 구하고, 특정 지점을 지나서 가는게 빠른지 확인
    
    graph = [[]*i for i in range(n+1)]
    for i in range(len(fares)):
        graph[fares[i][0]].append((fares[i][1],fares[i][2]))
        graph[fares[i][1]].append((fares[i][0],fares[i][2]))
        
    s_distance = dijkstra(s, graph, n)
    a_distance = dijkstra(a, graph, n)
    b_distance = dijkstra(b, graph, n)
    
    for i in range(n+1):
        answer = min(answer, s_distance[i] + a_distance[i] + b_distance[i])
        
    return answer
solution(6,	4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])


#다른 풀이들
#플루이드와샬
def solution(n, s, a, b, fares):
    ans = 200000001
    cost = [[20000001] * (n+1) for _ in range(n+1)]
    def floyd_warshall():
        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if i == j:
                        cost[i][j] = 0
                    else:
                        cost[i][j] = min(cost[i][k] + cost[k][j], cost[i][j])
        
    for i, j, c in fares:
        cost[i][j] = c
        cost[j][i] = c
    floyd_warshall()
        
    for i in range(1, n+1):
        ans = min(cost[s][i] + cost[i][a] + cost[i][b], ans)
    return ans

#다익스트라
import heapq
def solution(n, s, a, b, fares):
 
    def dijkstra(start):
        res = [float('INF') for _ in range(n+1)]
        res[start] = 0
        q = []
        heapq.heappush(q, (res[start], start))
        while q:
            result_x, x = heapq.heappop(q)
            for fu, fw in graph[x]:
                if res[fu] > result_x + fw:
                    res[fu] = result_x + fw
                    heapq.heappush(q, ([res[fu], fu]))
        return res
 
    ans = 200000001
    graph = [[] for _ in range(n+1)]
    for i, j, c in fares:
        graph[i].append((j, c))
        graph[j].append((i, c))
    
    dist = [[]]
    for i in range(1, n+1):
        dist.append(dijkstra(i))
 
    for i in range(1, n+1):
        ans = min(ans, dist[s][i] + dist[i][a] + dist[i][b])
    return ans