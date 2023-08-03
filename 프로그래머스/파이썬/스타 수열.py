def solution(a):
    answer = -1
    #스타 수열이려면 같은 숫자가 많아야하고 연속되면 안됨, a의 길이는 500000까지, 부분수열 
    #해를 구하는 방법 -> 연속이 아닌경우 그냥 증가, 연속인 경우 앞뒤 한칸식은 달라야하고 
    numbers = [0] * len(a)
    for i in range(len(a)):
        if len(a) > i + 1 and a[i] == a[i+1]:
            if i + 1 == len(a) -1 or i == 0:
                continue
            elif i + 2 < len(a) and a[i+1] == a[i+2]:
                continue
            elif i + 3 == len(a) - 1 and a[i+1] == a[i+3]:
                continue
            elif i + 4 < len(a) and a[i+1] == a[i+3] and a[i+1] == a[i+4]:
                continue
        
        else:
            numbers[a[i]] += 1
            
    max_number = max(numbers)
    
    if len(a) < 2:
        answer = 0
    else:
        answer = max_number * 2
    
        
    return answer

#정답
from collections import Counter

def solution(a):
    answer = -1

    # 현재 배열에 숫자들이 나온 횟수들
    els = Counter(a)
    # a에 있는 각 원소 k를 기준으로 스타배열을 만들 수 있는지 검사
    for k in els.keys():

        # 현재 k의 등장횟수가 스타수열에 사용된 공통 인자 횟수 이하면 continue
        if els[k] <= answer:
            continue
    
        # k의 등장 횟수
        cnt = 0
        idx = 0
        while idx < len(a)-1:
            # 두 칸 모두 k가 포함 안되어있거나 두 칸이 같은 값이면 스타수열 안되니까 continue
            if (a[idx] != k and a[idx+1] != k) or (a[idx] == a[idx+1]):
                idx += 1
                continue

            # 스타수열의 원소로 추가할 수 있는 경우 k사용횟수 1 증가
            cnt += 1
            # 다음 배열 탐색을 위해 두칸 점프
            idx += 2

        # 스타 수열 완성에 쓰인 공통 원소 k가 사용된 최대 횟수 갱신
        answer = max(cnt, answer)

    return -1 if answer == -1 else answer*2