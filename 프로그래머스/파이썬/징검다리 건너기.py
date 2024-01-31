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
    answer = 0
    s = 1
    e = max(stones)

    while s <= e:
        mid = (s+e)//2
        print(s, e, mid)
        count = 0
        for stone in stones:
            if stone < mid:
                count += 1
            else:
                count = 0
            if count >= k:
                break
        if count >= k:
            e = mid - 1
        else:
            answer = mid
            s = mid + 1

    return answer
