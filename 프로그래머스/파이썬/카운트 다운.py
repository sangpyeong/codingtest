def create_table():
    d_t = []
    s_b = []
    for i in range(1, 21):
        s_b.append(i)
    s_b.append(50)
    for i in range(2, 4):
        for j in range(1, 21):
            d_t.append(i*j)
    return [d_t, s_b]


def solution(target):
    answer = []
    table = create_table()

    dp = [[1e9, 0] for _ in range(target + 1)]
    dp[0][0] = 0

    for i in range(1, target + 1):
        for j in range(2):
            for k in range(len(table[j])):
                prev = i - table[j][k]

                if prev < 0:
                    continue

                if dp[prev][0] + 1 < dp[i][0]:
                    dp[i][0] = dp[prev][0] + 1
                if dp[prev][0] + 1 == dp[i][0]:
                    dp[i][1] = dp[prev][1] + j

    return dp[target]
