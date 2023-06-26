def solution(line):
    answer = []
    points = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            if (line[i][0] * line[j][1] - line[i][1] * line[j][0]) != 0:
                x = (line[i][1] * line[j][2] - line[i][2] * line[j][1]) / (line[i][0] * line[j][1] - line[i][1] * line[j][0])
                y = (line[i][2] * line[j][0] - line[i][0] * line[j][2]) / (line[i][0] * line[j][1] - line[i][1] * line[j][0])
                if int(x) == x and int(y) == y:
                    points.append([int(x),int(y)]) 
            else:
                continue
                
    
        
     # 교점의 x좌표들 
    xs = [p[0] for p in points]
    x_min = min(xs)
    x_max = max(xs)
    
    # 교점의 y좌표들
    ys = [p[1] for p in points]
    y_min = min(ys)
    y_max = max(ys)
    
    range_x = int(x_max - x_min + 1)
    range_y = int(y_max - y_min + 1)
    
    answer = [['.'] * range_x for _ in range(range_y) ]

    for i in range(len(points)):
        points[i][0] -= x_min
        points[i][1] -= y_min
        
    for i in range(len(points)):
        answer[points[i][1]][points[i][0]] = '*'
    
    answer.reverse()
    
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
        
    return answer