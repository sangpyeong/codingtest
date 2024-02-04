from collections import defaultdict
import sys
sys.setrecursionlimit(300000)
answer = 0


def dfs(x, a, tree, visited):
    global answer
    visited[x] = 1

    for y in tree[x]:
        if not visited[y]:
            visited[y]
            a[x] += dfs(y, a, tree, visited)
    answer += abs(a[x])

    return a[x]


def solution(a, edges):
    global answer

    if sum(a) != 0:
        return -1

    tree = defaultdict(list)
    for i, j in edges:
        tree[i].append(j)
        tree[j].append(i)

    visited = [0]*(len(a))

    dfs(0, a, tree, visited)

    return answer
