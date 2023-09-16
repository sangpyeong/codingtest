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


def solution(arr):
    nums = [int(i) for i in arr[0::2]]
    ops = [i for i in arr[1::2]]

    dp_max = {}
    dp_min = {}
    for i in range(len(nums)):
        dp_max[(i, i)] = nums[i]
        dp_min[(i, i)] = nums[i]

    for d in range(1, len(nums)):
        for i in range(len(nums)):
            j = i + d
            if j >= len(nums):
                continue

            max_candidate = []
            min_candidate = []
            for k in range(i+1, j+1):
                if ops[k-1] == "-":
                    mx = dp_max[(i, k-1)] - dp_min[(k, j)]
                    mn = dp_min[(i, k-1)] - dp_max[(k, j)]
                    max_candidate.append(mx)
                    min_candidate.append(mn)
                else:
                    mx = dp_max[(i, k-1)] + dp_max[(k, j)]
                    mn = dp_min[(i, k-1)] + dp_min[(k, j)]
                    max_candidate.append(mx)
                    min_candidate.append(mn)
            dp_max[(i, j)] = max(max_candidate)
            dp_min[(i, j)] = min(min_candidate)

    return dp_max[(0, len(nums)-1)]
