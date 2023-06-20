from collections import deque

dx = [1, 0 ,-1, 0]#상 우 하 좌
dy = [0, 1, 0, -1]
def calculate_day(map, x, y):
    result=0
    q = deque([(x, y)])
    while(q):
        tx, ty = q.popleft()
        result += int(float(map[tx][ty]))
        map[tx] = list(map[tx])
        map[tx][ty] = "X"
        map[tx] = ''.join(s for s in map[tx])
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if nx>=0 and nx <len(map) and ny>=0 and ny<len(map[0]) and map[nx][ny]!="X":
                print(nx,ny)
                q.append((nx,ny))
    return result
    
    
def solution(maps):
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "X":
                continue
            calculate_day(maps, i, j)
    return answer

solution(["X591X","X1X5X","X231X", "1XXX1"])