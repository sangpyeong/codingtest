#문제에서 원하는 대로 풀어야함, 뱀의 위치를 가지고 있음 페어 리스트로

n = int(input())
k = int(input())

apple = [[False] * n for _ in range(n)]
map = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def straight(x, y, d):
    x, y = x+dx[d], y+dy[d]
    map[x][y] = tail


def check(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    elif map[x][y] > 0:
        return False
    else:
        return True


def mapdown():
    for i in range(n):
        for j in range(n):
            if map[i][j] > 0:
                map[i][j] -= 1


for i in range(k):
    a, b = list(map(int, input().split()))
    apple[a-1][b-1] = True

x, y = 0, 0
d = 0
count = 0
tail = 1
for i in range(L):
    move, c = input()
    for j in range(int(move)):
        count += 1
        straight(x, y, d)
        if apple[x][y] == True:
            tail += 1
        if check(x, y) == False:
            break
    if check(x, y) == False:
        break
    if c == 'L':
        d = (d-1) % 4
    elif c == 'D':
        d = (d+1) % 4

print(count)

#정답
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())
