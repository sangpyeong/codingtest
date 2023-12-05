# M[(i, j)]
# nums[i] 부터 nums[j]까지 연산했을 때 나올 수 있는 최댓값
# m[(i, j)]
# nums[i] 부터 nums[j]까지 연산했을 때 나올 수 있는 최솟값
M, m = {}, {}
# 점화식
# i~j를 두 부분으로 분할하는 모든 k에 대해서 (k=i+1, i+2, ..., j)
# --> i~k-1 / k~j로 나뉜다고 하자
# 나올 수 있는 연산의 최댓값, 최솟값을 저장해 두어야 한다.
# ops[k-1]의 경우에 따라 나뉜다
# ops[k-1] == '-'인 경우,
# 최댓값을 위해서는 M[(i, k-1)] - m[(k, j)] 를 기억해둔다.
# 최솟값을 위해서는 m[(i, k-1)] - M[(k, j)] 를 기억해둔다.
# ops[k-1] == '+'인 경우,
# 최댓값을 위해서는 M[(i, k-1)] + M[(k, j)] 를 기억해둔다.
# 최솟값을 위해서는 m[(i, k-1)] + m[(k, j)] 를 기억해둔다.


def solution(arr):
    nums = [int(x) for x in arr[::2]]
    ops = [x for x in arr[1::2]]

    for i in range(len(nums)):
        M[(i, i)] = nums[i]
        m[(i, i)] = nums[i]

    for d in range(1, len(nums)):
        for i in range(len(nums)):
            j = i + d
            if j >= len(nums):
                continue

            maxcandidates, mincandidates = [], []
            for k in range(i+1, j+1):
                if ops[k-1] == '-':
                    mx = M[(i, k-1)] - m[(k, j)]
                    mn = m[(i, k-1)] - M[(k, j)]
                    maxcandidates.append(mx)
                    mincandidates.append(mn)
                else:
                    mx = M[(i, k-1)] + M[(k, j)]
                    mn = m[(i, k-1)] + m[(k, j)]
                    maxcandidates.append(mx)
                    mincandidates.append(mn)

            M[(i, j)] = max(maxcandidates)
            m[(i, j)] = min(mincandidates)

    return M[(0, len(nums) - 1)]

# dp를 2차원 배열로 최소 최대 값 튜플을 가지고 있는 것으로 설정


def solution(arr):
    nums = [int(i) for i in arr[0::2]]
    ops = [i for i in arr[1::2]]
    n = len(nums)

    # dp 배열 초기화
    # 각 요소는 (최대값, 최소값)을 저장
    dp = [[(0, 0) for _ in range(n)] for _ in range(n)]

    # 대각선(자기 자신에 대한 값)은 먼저 계산
    for i in range(n):
        dp[i][i] = (nums[i], nums[i])

    # 길이를 2부터 n까지 증가시키며 확인
    for d in range(1, n):
        for i in range(n - d):
            j = i + d
            max_value = -1e9  # 아주 작은 값으로 초기화
            min_value = 1e9  # 아주 큰 값으로 초기화

            # i부터 j사이의 모든 k에 대해 경우의 수를 따져보고 최대/최소 갱신
            for k in range(i, j):
                if ops[k] == "+":
                    max_temp = max(dp[i][k][0] + dp[k+1][j][0],
                                   dp[i][k][1] + dp[k+1][j][1])
                    min_temp = min(dp[i][k][0] + dp[k+1][j][0],
                                   dp[i][k][1] + dp[k+1][j][1])
                else:  # ops[k] == "-"
                    max_temp = max(dp[i][k][0] - dp[k+1][j][1],
                                   dp[i][k][1] - dp[k+1][j][0])
                    min_temp = min(dp[i][k][0] - dp[k+1][j][0],
                                   dp[i][k][1] - dp[k+1][j][1])

                max_value = max(max_value, max_temp)
                min_value = min(min_value, min_temp)

            # dp 갱신
            dp[i][j] = (max_value, min_value)

    return dp[0][n-1][0]
