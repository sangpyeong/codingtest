import heapq

INF = float('inf')

# 갈수있는 방향 판별 함수


def isReverse(cur_pos, next_pos, cur_state, traps_idx):
    is_cur_trap_on, is_next_trap_on = False, False
    if cur_pos in traps_idx:
        is_cur_trap_on = (cur_state & (1 << traps_idx[cur_pos])) > 0
    if next_pos in traps_idx:
        is_next_trap_on = (cur_state & (1 << traps_idx[next_pos])) > 0

    # 함정 상태가 같으면 순방향, 다르면 역방향
    return is_cur_trap_on != is_next_trap_on

# 다음 노드를 밟은 후 상태를 반환하는 함수


def getNextState(next_pos, cur_state, traps_idx):
    if next_pos in traps_idx:
        return cur_state ^ (1 << traps_idx[next_pos])
    return cur_state


def solution(n, start, end, roads, traps):
    answer = INF
    min_cost = [[INF for _ in range(n+1)] for _ in range(2**len(traps))]
    traps_idx = {v: i for i, v in enumerate(traps)}
    graph = [[] for _ in range(n+1)]  # end, cost, isReverse
    # graph 생성
    for _start, _end, _cost in roads:
        graph[_start].append([_end, _cost, False])
        graph[_end].append([_start, _cost, True])

    hq = []  # [[sum, cur_pos, trap_state]]
    heapq.heappush(hq, [0, start, 0])
    min_cost[0][start] = 0  # 첫 시작점

    while hq:
        cur_sum, cur_pos, cur_state = heapq.heappop(hq)
        if cur_pos == end:
            answer = min(answer, cur_sum)
            continue
        if cur_sum > min_cost[cur_state][cur_pos]:
            continue
        for next_pos, next_cost, is_reverse in graph[cur_pos]:
            # 못 가는 방향이면 pass
            if is_reverse != isReverse(cur_pos, next_pos, cur_state, traps_idx):
                continue

            next_state = getNextState(next_pos, cur_state, traps_idx)
            next_sum = next_cost+cur_sum
            # 다음 상태의 비용이 이미 더 작으면 pass
            if next_sum >= min_cost[next_state][next_pos]:
                continue

            min_cost[next_state][next_pos] = next_sum
            heapq.heappush(hq, [next_sum, next_pos, next_state])

    return answer
