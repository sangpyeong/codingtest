def solution(cookie):
    answer = 0
    # m을 설정하고 l과 r을 조정하면서 값을 찾자
    N = len(cookie)
    for m in range(N - 1):
        l = m
        r = m + 1
        left_total = cookie[l]
        right_total = cookie[r]
        while 0 <= l < N and 0 <= r < N:
            if left_total > right_total:
                r += 1
                if 0 <= r < N:
                    right_total += cookie[r]
            elif left_total < right_total:
                l -= 1
                if 0 <= l < N:
                    left_total += cookie[l]
            elif left_total == right_total:
                answer = max(answer, left_total)
                r += 1
                l -= 1
                if (0 <= l < N) and (0 <= r < N):
                    left_total += cookie[l]
                    right_total += cookie[r]

    return answer
