#시간 초과, 재귀함수 사용법, global사용법, 순열


n = int(input())
A = list(map(int, input().split()))
addtion, substraction, multiplication, division = map(int, input().split())

maxnum=-1e9
minnum=1e9
arr=[i for i in range(1,n)]
used = [ 0 for _ in range(n-1)]

def permu(oper,used):


    if len(oper)==n-1:#연산자 다 채워지면 계산
        result = A[0]
        global maxnum
        global minnum
        for i in range(n-1):
            if oper[i] >= 1 and oper[i] <= addtion:
                result+=A[i+1]
            elif oper[i] >= addtion+1 and oper[i] <= addtion+substraction:
                result-=A[i+1]
            elif oper[i] >= addtion+substraction+1 and oper[i] <= addtion+substraction+multiplication:
                result*=A[i+1]
            elif oper[i] >= addtion+substraction+multiplication+1 and oper[i] <= addtion+substraction+multiplication+division:
                result/=A[i+1]
        maxnum = max(maxnum, result)
        minnum = min(minnum, result)
            
    for i in range(n-1):
        if not used[i]:
            oper.append(arr[i])
            used[i]=1
            permu(oper,used)
            used[i]=0
            oper.pop()

permu([], used)

print(maxnum)
print(minnum)


#정답
n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색 (DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i])) # 나눌 때는 나머지를 제거
            div += 1

# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)
