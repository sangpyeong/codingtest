def solution(money):
    answer = 0

    dp1 = [0] * (len(money) - 1)
    dp2 = [0] * (len(money) - 1)
    dp1[0], dp1[1] = money[0], money[0] if money[0] > money[1] else money[1]
    dp2[0], dp2[1] = money[1], money[1] if money[1] > money[2] else money[2]
    for i in range(2, len(money)-1):
        dp1[i] = dp1[i-2] + money[i] if dp1[i-2] + \
            money[i] > dp1[i-1] else dp1[i-1]
    for i in range(2, len(money)-1):
        dp2[i] = dp2[i-2] + money[i+1] if dp2[i-2] + \
            money[i+1] > dp2[i-1] else dp2[i-1]
    answer = max(dp1[-1], dp2[-1])

    return answer
