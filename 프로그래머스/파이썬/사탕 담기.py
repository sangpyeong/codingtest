from itertools import combinations

# 조합 활용


def solution(m, weights):
    answer = 0
    for i in range(len(weights)):
        com = list(combinations(weights, i+1))
        for j in com:
            if m == sum(j):
                answer += 1
    return answer

# 백트래킹 활용


def solution(m, weights):
    answer = 0

    def backtrack(index, current_weight):
        nonlocal answer
        if current_weight == m:
            answer += 1
            return
        elif current_weight > m or index == len(weights):
            return

        # 현재 사탕을 선택하는 경우
        backtrack(index + 1, current_weight + weights[index])

        # 현재 사탕을 선택하지 않는 경우
        backtrack(index + 1, current_weight)

    backtrack(0, 0)
    return answer
