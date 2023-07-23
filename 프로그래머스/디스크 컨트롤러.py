import heapq
from collections import deque


def solution(jobs):
    answer = 0
    jobs.sort()
    hq = []
    heapq.heappush(hq, [jobs[0][1], jobs[0][0]])
    time = jobs[0][0]
    jobs_index = 1
    time_sum = 0
    while jobs_index < len(jobs):
        for i in range(jobs_index, len(jobs)):
            if time >= jobs[i][0]:
                heapq.heappush(hq, [jobs[i][1], jobs[i][0]])
                jobs_index += 1
            else:
                break
        if not hq:
            time = jobs[jobs_index][0]
            continue

        taken_time, arrive_time = heapq.heappop(hq)
        time += taken_time
        time_sum += time - arrive_time

    while hq:
        taken_time, arrive_time = heapq.heappop(hq)
        time += taken_time
        time_sum += time - arrive_time

    answer = time_sum/len(jobs)
    answer = int(answer)
    return answer
