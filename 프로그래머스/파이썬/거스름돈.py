def solution(n, money):
    dp = [1] + [0] * n
    for m in money:
        for i in range(m, n+1):
            dp[i] = (dp[i] + dp[i-m]) % 1000000007
    return dp[n]
# 시간복잡도 = O(n), 공간복잡도 = O(n)
