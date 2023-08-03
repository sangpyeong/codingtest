def solution(a):
    if len(a) == 1:
        return 1

    answer = 2   # 기본적으로 양쪽 끝은 끝까지 살아남을 수 있음
    
    # 최솟값 쌓기 ----------------
    l_min = [a[0]]     
    r_min = [a[-1]]
    for i in range(1, len(a)):
        if a[i] < l_min[-1]:
            l_min.append(a[i])
        else:
            l_min.append(l_min[-1])
        if a[len(a) - 1 - i] < r_min[-1]:
            r_min.append(a[len(a) - 1 - i])
        else:
            r_min.append(r_min[-1])
    r_min.reverse()    
    # -----------------

	# 찾은 최솟값으로 비교 계산 -------------
    for i in range(1, len(a) - 1):
        if l_min[i - 1] > a[i] or r_min[i + 1] > a[i]:
            answer += 1
    # --------------------------------
            
    return answer