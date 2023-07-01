from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    for i in range(len(priorities)):
        q.append([priorities[i], i])
    
    for j in range(len(q)):
        #큐 정렬
        for i in range(len(q)):
            priorlist = [i[0] for i in q]
            if max(priorlist) != q[0][0]:
                tmp = q.popleft()
                q.append(tmp)
        #프로세스 실행
        process = q.popleft()
        answer+=1
        if process[1] == location:
            break
    
    return answer