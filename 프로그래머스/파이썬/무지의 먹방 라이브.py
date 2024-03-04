# 내 풀이, 테스트 29만 실패 ㅈㄴ 빡침
def solution(food_times, k):
    answer = 0
    if sum(food_times)<=k:
        return -1
    sorted_food = sorted(food_times)
    N = len(food_times)
    mn_food = 0
    prev_food = 0
    eat_food = 0
    for i in range(N):
        if mn_food < sorted_food[i]:
            mn_food = sorted_food[i]
            if k > (N-i)*(mn_food-prev_food):
                k -= (N-i)*(mn_food-prev_food)
                prev_food = mn_food
            else:
                if k <= N-i:
                    for j in range(N):
                        
                        if food_times[j] <= prev_food:
                            continue
                        k -= 1
                        if k == 0:
                            eat_food = j
                            break
                else:
                    k -= (k//(N-i))*(N-i)    
                    for j in range(N):
                        if food_times[j] <= prev_food:
                            continue
                        k -= 1
                        if k == 0:
                            eat_food = j
                            break
                break
    eat_food = (eat_food + 1) % N
    while food_times[eat_food] <= prev_food:
        eat_food = (eat_food + 1) % N
    
    answer = eat_food + 1
    return answer

# 무지의 먹방 라이브 다른 풀이
import heapq


def solution(food_times, k):
    answer = -1
    h = []
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i + 1))

    food_num = len(food_times)  # 남은 음식 개수
    previous = 0  # 이전에 제거한 음식의 food_time

    while h:
        # 먹는데 걸리는 시간: (남은 양) * (남은 음식 개수)
        t = (h[0][0] - previous) * food_num
        # 시간이 남을 경우 현재 음식 빼기
        if k >= t:
            k -= t
            previous, _ = heapq.heappop(h)
            food_num -= 1
        # 시간이 부족할 경우(음식을 다 못먹을 경우) 남은 음식 중에 먹어야 할 음식 찾기
        else:
            idx = k % food_num
            h.sort(key=lambda x: x[1])
            answer = h[idx][1]
            break

    return answer
