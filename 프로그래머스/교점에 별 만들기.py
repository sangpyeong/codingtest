def solution(line):
    answer = []
    maps=[]
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a1 = line[i][0]
            b1 = line[i][1]
            c1 = line[i][2]
            a2 = line[j][0]
            b2 = line[j][1]
            c2 = line[j][2]
            if (a1==0 and a2==0) or (b1==0 and b2==0):
                continue
            elif a1!=0 and a2!=0:
                tmp = []
                for k in range(3):
                    tmp.append(line[i][k] * a2/a1)
                by = tmp[1] - b2
                c = c2 - tmp[2]
                y = c/by
                x = -(b1*y + c1)/a1
                if int(x)==x and int(y)==y:
                    maps.append([x,y])
            elif b1!=0 and b2!=0:
                tmp = []
                for k in range(3):
                    tmp.append(line[i][k] * b2/b1)
                bx = tmp[0] - a2
                c = c2 - tmp[2]
                x = c/bx
                y = -(a1*x + c1)/b1
                if int(x)==x and int(y)==y:
                    maps.append([x,y])
                    
            else:
                if a1!=0 and b2!=0:
                    x = -c1/a1
                    y = -c2/b2
                elif b1!=0 and a2!=0:
                    y = -c1/b1
                    x = -c2/a2
                if int(x)==x and int(y)==y:
                    maps.append([x,y])
                    
            print(maps)
            
    max_x=-1e9
    min_x=1e9
    max_y=-1e9
    min_y=1e9
    range_x=1
    range_y=1
    for i in range(len(maps)):
        max_x = max(max_x, maps[i][0])
        min_x = min(min_x, maps[i][0])
        max_y = max(max_y, maps[i][1])
        min_y = min(min_y, maps[i][1])
        
    if max_x > 0 and min_x < 0:
        range_x = max_x - min_x +1
    elif max_x == 0 and min_x == 0:
        pass
    else:
        range_x = max_x - min_x
        
    if max_y > 0 and min_y < 0:
        range_y = max_y - min_y +1
    elif max_y == 0 and min_y == 0:
        pass
    else:
        range_y = max_y - min_y
    if range_x == 0 :
        range_x =1
    if range_y == 0:
        range_y = 1
    
    answer = [["."]*int(range_x) for _ in range(int(range_y))]
    
    for i in range(len(maps)):
        maps[i][0] -= min_x
        maps[i][1] -= min_y
    
    print(maps)
    
    for i in range(int(range_x)):
        for j in range(int(range_y)):
            for k in range(len(maps)):
                if i == int(maps[k][0]) and j == int(maps[k][1]):
                    answer[j][i] = "*"
    answer.reverse()
    print(answer)
    
    result = []
    
    for i in range(len(answer)):
        
        result.append(''.join(s for s in answer[i]))
    print(result)
    
    return result