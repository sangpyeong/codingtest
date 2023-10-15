# 내 풀이

def solution(enroll, referral, seller, amount):
    answer = []
    N = len(enroll)
    money = [0] * N
    dic = {}
    for i in range(N):
        dic[enroll[i]] = i

    for i in range(len(seller)):
        p = seller[i]
        m = amount[i] * 100
        while p != "-":
            if m/10 < 1:
                money[dic[p]] += m
                break
            else:
                money[dic[p]] += m - m//10
                m = int(m/10)
                p = referral[dic[p]]
    answer = money
    return answer

# 다른 풀이


def solution(enroll, referral, seller, amount):
    money = [0 for _ in range(len(enroll))]
    dict = {}
    for i, e in enumerate(enroll):
        dict[e] = i
    for s, a in zip(seller, amount):
        m = a * 100
        while s != "-" and m > 0:
            idx = dict[s]
            money[idx] += m - m//10
            m //= 10
            s = referral[idx]
    return money
