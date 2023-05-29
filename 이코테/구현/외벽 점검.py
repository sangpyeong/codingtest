#시간초과, 오류 남
#어려움 잘 모르겠음

import itertools

def check(data):
    for i in data:
        if i != 0:
            return False
    return True

def solution(n, weak, dist):
    answer = 0
    #순열 만듦
    npr =[]
    for i in range(1,len(dist)+1):
        permutation(dist,i,npr)
    
    

    #순열에 맞게 테스트
    for i in range(len(npr)): #순열 행 결정
        #전체 리스트 만듦
        data = [0]*n
        for k in range(len(weak)):
            data[weak[k]]=1
        o=0 #weak 인덱스 순서대로
        j=0 #weak
        while j<len(weak): #weak 
            for k in range(len(npr[i])): #순열 열 결정
                
                if data[weak[j]] == 1:
                    if weak[j] + npr[i][k]+1 <n:
                        data[weak[j]:weak[j]+npr[i][k]+1]=[0]*(npr[i][k]+1)
                    else:
                        data[weak[j]:n] = [0]*(n-weak[j])
                        data[0:npr[i][k]+1 - (n-weak[j])] = [0]*(npr[i][k]+1 - (n-weak[j]))
                if check(data):
                    print(len(npr[i]))
                    return len(npr[i])
                elif k == len(npr[i])-1:
                     #전체 리스트 만듦
                    data = [0]*n
                    for l in range(len(weak)):
                        data[weak[l]]=1
                    o+=1
                    j=o

                else:
                    for m in range(len(weak)):
                        if data[weak[m]]==1 and m > j:
                            j = m
                            break
                        elif m == len(weak)-1:
                            for p in range(len(weak)):
                                if data[weak[p]] == 1:
                                    j=p
                                    break

            

    return answer

def permutation(arr, r,npr):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            tmp_list = []
            for i in range(len(chosen)):
                tmp_list.append(chosen[i])
            npr.append(tmp_list)
            return
	
	# 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)

solution(12,[1, 5, 6, 10],[1, 2, 3, 4])

#정답
from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약한 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count) # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer