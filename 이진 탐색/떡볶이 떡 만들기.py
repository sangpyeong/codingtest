import sys
# 떡의 개수 N과 요청한 떡의 길이 M 입력 받기
n, m = map(int, sys.stdin.readline().rstrip().split())
# 떡의 개별 높이 입력 받기
n_list = list(map(int, sys.stdin.readline().rstrip().split()))

# 이진 탐색 시작 위치와 종료 위치 초기화
start = 0
end = max(n_list)

# 절단기의 높이
result = 0

while (start < end):

    # 절단기 높이 지정
    mid = (start+end)//2

    sum = 0
    # 절단기로 모든 떡을 잘랐을 때, 남은 떡의 길이 계산
    for n in n_list:
        # 떡의 높이가 더 높을 때만 자를 수 있음
        if (n > mid):
            sum += n - mid

    # 남은 떡의 길이가 손님이 요청한 떡의 길이보다 적을 경우,
    # 절단기의 높이를 낮춰야함
    if (sum < m):
        end = mid - 1

    # 남은 떡의 길이가 손님이 요청한 떡의 길이보다 많거나 같을 경우,
    # 해당 절단기의 높이를 기록하고, 절단기의 높이를 높여야함
    else:
        result = mid
        start = mid + 1

print(result)
