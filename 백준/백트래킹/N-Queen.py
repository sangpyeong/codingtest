n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
posible = [[True for _ in range(n)] for _ in range(n)]

result = 0


def dfs(n):
    if True not in posible:
        global result
        result += 1
    for i in range(n):
        for j in range(n):
            if posible[i][j] == False:
                continue
            arr[i][j] = 1
            # 가로세로 False 처리
            posible[i] = [False for _ in range(n)]
            posible[:, j] = [False for _ in range(n)]
            # 대각선 False 처리
            for k in range(n):
                if i+k >= 0 and i+k < n and j+k >= 0 and j+k < n and posible[i+k][j+k] == True:
                    posible[i+k][j+k] = False
                if i-k >= 0 and i-k < n and j+k >= 0 and j+k < n and posible[i-k][j+k] == True:
                    posible[i-k][j+k] = False
                if i+k >= 0 and i+k < n and j-k >= 0 and j-k < n and posible[i+k][j-k] == True:
                    posible[i+k][j-k] = False
                if i-k >= 0 and i-k < n and j-k >= 0 and j-k < n and posible[i-k][j-k] == True:
                    posible[i-k][j-k] = False

            dfs()
            # 되돌리기
            # 가로세로 True 처리
            posible[i] = [True for _ in range(n)]
            posible[:, j] = [True for _ in range(n)]
            # 대각선 True 처리
            for k in range(n):
                if i+k >= 0 and i+k < n and j+k >= 0 and j+k < n and posible[i+k][j+k] == False:
                    posible[i+k][j+k] = True
                if i-k >= 0 and i-k < n and j+k >= 0 and j+k < n and posible[i-k][j+k] == False:
                    posible[i-k][j+k] = True
                if i+k >= 0 and i+k < n and j-k >= 0 and j-k < n and posible[i+k][j-k] == False:
                    posible[i+k][j-k] = True
                if i-k >= 0 and i-k < n and j-k >= 0 and j-k < n and posible[i-k][j-k] == False:
                    posible[i-k][j-k] = True


dfs(n)
print(result)


###############################################################################

# 정답

def adjacent(x):  # x와 i 가 같으면 행이 같은거 근데 for문을 보면 x와 i가 같을 수가 없다.
    for i in range(x):  # 인덱스가 행  row[n]값이 열
        # 열이 같거나 대각선이 같으면 false
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            # 대각선이 같은경우는 두 좌표에서 행 - 행 = 열 - 열 이 같으면 두개는 같은 대각선상에 있다.
            return False
    return True

# 한줄씩 재귀하며 dfs 실행


def dfs(x):
    global result

    if x == N:
        result += 1
    else:
        # 각 행에 퀸 놓기
        for i in range(N):  # i 는 열번호 0부터 N 전까지 옮겨가면서 유망한곳 찾기
            row[x] = i
            if adjacent(x):  # 행,열,대각선 체크함수 true이면 백트래킹 안하고 계속 진행
                dfs(x + 1)


# N = int(input())/
N = int(input())
row = [0] * N
result = 0
print(row)
dfs(0)
# print(row)
print(result)


#############################
# 백트래킹 문제로
# 2차원배열을 안쓰고 배열 값을 통해 1차원으로 처리함, 그리고 가지치기를 함수를 따로
# 만들어서 처리함, 대각선은 절대값 비교해서 처리함
