import heapq


def solution(n, works):
    answer = 0
    hq = []

    for i in range(len(works)):
        heapq.heappush(hq, works[i] * (-1))
    for i in range(n):
        if not hq:
            break
        tmp = heapq.heappop(hq)
        tmp += 1
        if tmp < 0:
            heapq.heappush(hq, tmp)
    while hq:
        tmp = heapq.heappop(hq)
        answer += tmp * tmp
    return answer
