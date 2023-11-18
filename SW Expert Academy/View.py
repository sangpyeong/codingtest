for i in range(10):
    N = int(input())
    datas = list(map(int, input().split()))
    answer = 0
    for j in range(2, N-2):
        mx = max([datas[j-2], datas[j-1], datas[j+1], datas[j+2]])
        if datas[j] > mx:
            answer += datas[j] - mx
    print("#"+str(i+1)+" "+str(answer))