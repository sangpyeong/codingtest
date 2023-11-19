T = int(input())
for i in range(1, T+1):
    N = int(input())
    datas = list(map(int, input().split()))
    dic = dict()
    for data in datas:
        if data not in dic:
            dic[data] = 1
        else:
            dic[data] += 1
    mx = 0
    for k, v in dic.items():
        if mx < v:
            mx = v
            answer = k
        elif mx == v:
            answer = max(k, answer)
    print("#{} {}".format(i, answer))
