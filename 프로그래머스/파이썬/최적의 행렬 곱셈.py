import copy
from collections import deque

# 내 풀이 실패함


def solution(matrix_sizes):
    answer = 0

    length = len(matrix_sizes)
    used = {}
    table = []
    combi = []
    nums = set()
    for i in range(length):
        nums.add(matrix_sizes[i][0])
        used[tuple(matrix_sizes[i])] = False

    def backtracking(index):
        if index == length:
            tmp_combi = copy.deepcopy(combi)
            table.append(tmp_combi)
            return

        for i in range(length):
            if not used[tuple(matrix_sizes[i])]:
                if not combi:
                    combi.append(tuple(matrix_sizes[i]))
                    used[tuple(matrix_sizes[i])] = True
                    backtracking(index + 1)
                    used[tuple(matrix_sizes[i])] = False
                    combi.pop()
                elif combi[index-1][1] == tuple(matrix_sizes[i])[0]:
                    combi.append(tuple(matrix_sizes[i]))
                    used[tuple(matrix_sizes[i])] = True
                    backtracking(index + 1)
                    used[tuple(matrix_sizes[i])] = False
                    combi.pop()
                else:
                    break

    backtracking(0)
    print(table)

    sored_nums = sorted(list(nums), reverse=True)

    # for order in table:
    #     dq = deque(sored_nums)
    #     for i in range(len(order)):
    #         mx = dq.popleft()
    #         if order[0][0] == mx:
    #             mx = dq.popleft()
    #         if order[len(order)-1][1] == mx:
    #             mx = dq.popleft()

    return answer

# 다른 사람 풀이


def solution(matrix_sizes):
    N = len(matrix_sizes)
    dp = [[0] * N for _ in range(N)]

    for gap in range(1, N):
        for i in range(N - gap):
            j = i + gap
            dp[i][j] = float('inf')  # 초기값을 무한대로 설정

            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + matrix_sizes[i][0] * \
                    matrix_sizes[k][1] * matrix_sizes[j][1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][N-1]


# 예시 입력
matrix_sizes = [(5, 3), (3, 10), (10, 6)]
result = solution(matrix_sizes)
print(result)  # 출력: 270
