def solution(k, ranges):
    answer = []
    #그래프 구하기
    points=[]
    index = 0
    while(k!=1):
        points.append([index, int(k)])
        if k%2==0:
            k/=2
        elif k%2==1:
            k*=3
            k+=1
        index+=1
        if k==1:
            points.append([index,int(k)])
            
    
    
    #결과 값 구하기
    for i in range(len(ranges)):
        start = ranges[i][0]
        end = index + ranges[i][1]
        if start > end:
            answer.append(-1)
        elif start == end:
            answer.append(0)
        else:
            sum_area=0
            for j in range(start, end):
                sum_area+=(points[j][1] + points[j+1][1])/2
            answer.append(sum_area)
    return answer