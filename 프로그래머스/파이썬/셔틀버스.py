from collections import deque

def solution(n, t, m, timetable):
    answer = ''
    
    #문자열->분
    minute_time = []
    for i in timetable:
        hour = int(i[0]) * 10 + int(i[1])
        minute = int(i[3]) * 10 + int(i[4])
        minute_time.append(hour*60 + minute)

    #가능한 제일 마지막 시간부터 0까지 가능한지 체크
    for i in range(540 + (n-1)*t, -1, -1):
        #i에 대한 인덱스 구함
        tmp_minute_time = minute_time[:]
        tmp_minute_time.append(i)
        tmp_minute_time.sort()
        tmp_minute_time.reverse()
        index_i = len(tmp_minute_time) - tmp_minute_time.index(i) - 1
        tmp_minute_time.reverse()
        
        q = deque(tmp_minute_time)
        
        #버스 도착해서 조건에 맞게 큐에서 뺌
        index = -1
        start = 540
        for j in range(n):
            people = 0
            while people != m:
                if q[0] <= start:
                    q.popleft()
                    people += 1
                    index += 1
                    if index == index_i:
                        hour = int(i/60)
                        if hour < 10:
                            hour = "0" + str(hour)
                        else:
                            hour = str(hour)
                        minute = i%60
                        if minute < 10:
                            minute = "0" + str(minute)
                        else:
                            minute = str(minute)
                        answer = hour + ":" + minute
                        return answer
                else: 
                    break
            start += t
        
    return answer



#검색해서 나온 코드
def solution(n, t, m, timetable):
    answer = 0
    # 모든 시간을 분으로 환산해서 생각
    # 예시: "09:10" => 9*60 + 10 = 550(분)
    # 크루 도착 시각 리스트
    crewTime = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    crewTime.sort()
    # 버스 도착 시각 리스트
    busTime = [9*60 + t*i for i in range(n)]

    i = 0       # 다음에 버스에 오를 크루의 인덱스
    for tm in busTime:
      cnt = 0   # 버스에 타는 크루 수
      while cnt < m and i < len(crewTime) and crewTime[i] <= tm:
        i += 1
        cnt += 1
      # 버스에 자리가 남았을 경우
      if cnt < m: answer = tm
      # 버스에 자리가 없는 경우 맨 마지막 크루보다 1분 먼저 도착
      else: answer = crewTime[i - 1] - 1

    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)