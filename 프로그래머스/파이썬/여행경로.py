def solution(tickets):
    answer = []
    goal = len(tickets) + 1
    ch = [0] * len(tickets)

    def dfs(path):
        if len(path) == goal:
            answer.append(path)
            return
        for i, [start, end] in enumerate(tickets):
            if ch[i] == 0 and path[-1] == start:
                ch[i] = 1
                dfs([*path, end])
                ch[i] = 0

    dfs(["ICN"])
    return min(answer)
