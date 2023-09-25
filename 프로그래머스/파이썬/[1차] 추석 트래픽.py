from collections import deque


# 내가 풀다 실패한 거
def solution(lines):
    answer = 0
    # 시작과 끝 부분을 찾아서 최대값을 구하면 된다.
    # 시간 계산이 복잡함
    # 푸는 알고리즘 시작 시간과 끝 시작을 heap에 넣음, while문으로 heap하나씩 빼면서 2차원 리스트에 현재 진행중인 시작 시간과 끝 시간을
    # 가지고 있는 리스트 추가
    for i in range(len(lines)):
        end = lines[i][11:23]
        time = lines[i][24:]
        print(end, time)
        s = end[6:]
    return answer

# 다른 사람 풀이


def solution(lines):
    answer = 0
    start_time = []
    end_time = []

    for t in lines:
        time = t.split(" ")
        start_time.append(get_start_time(time[1], time[2]))
        end_time.append(get_time(time[1]))
    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        # i번째는 현재 자신의 시작시간이고, i 이하는 그 이전의 시작시간이므로 카운트 할 필요가 없다.
        for j in range(i, len(lines)):
            if cur_end_time > start_time[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)
    return answer


def get_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second) * 1000 + millisecond


def get_start_time(time, duration_time):
    n_time = duration_time[:-1]
    int_duration_time = int(float(n_time) * 1000)
    return get_time(time) - int_duration_time + 1
