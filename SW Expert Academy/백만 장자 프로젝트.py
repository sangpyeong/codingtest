T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    datas = list(map(int, input().split()))
    result = 0
    mx = 0
    for data in datas[::-1]:
        if data >= mx:
            mx = data
        else:
            result += mx - data
    print("#", test_case, " ", result, sep="")