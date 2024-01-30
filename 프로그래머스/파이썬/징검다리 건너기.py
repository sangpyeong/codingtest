# 시간초과 발생
def solution(stones, k):
    answer = 0
    min_stones = sorted(list(set(stones)))
    index = 0
    while True:
        count = 0
        m = min_stones[index]
        for s in stones:
            if s < m:
                count += 1
            else:
                count = 0
            if count == k:
                return min_stones[index-1]
        index += 1

    return answer

# 다른 풀이


def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left
