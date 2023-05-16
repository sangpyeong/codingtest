def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False
  

n, m = map(int, input().split())
s = []
dfs()
visited = [False] * (n+1)

#백트래킹 기본 예제, 일반적인 DFS와 차이점은 가지치기

#백트래킹은 일반적으로 재귀의 형태로 작성되며, 크게 다음의 3개 내용을 작성해야한다.
#   재귀를 진행하는 동안 사용될 깊이(depth)를 매개변수로 넣기
#   재귀가 종료되는 시점에서 수행해야할 내용
#   재귀가 진행중이면 가지치기(백트래킹)할 내용
