def solution(n):
    answer = 0
    lists = []

    def backtracking(o, c, str):
        if len(str) == 2 * n:
            lists.append(str)
            return

        if o < n:
            str += "("
            backtracking(o+1, c, str)
            str = str[:-1]

        if o > c:
            str += ")"
            backtracking(o, c+1, str)
            str = str[:-1]

    backtracking(0, 0, "")
    answer = len(lists)
    return answer

# 다른 풀이
# 코드


def solution(n):
    answer = 1

    dp = [0 for i in range(n+1)]
    dp[0], dp[1] = 1, 1

    for i in range(2, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-1-j]

    answer = dp[n]

    return answer
