#정답 맞춤 1시간 반걸림, 조합 라이브러리를 사용함, 거리를 2차원 배열 대신 구함
#1e9가 정수의 최대값인듯?, for hx, hy in house:에서 hx, hy처럼 쓰는 방법
#조합할 때 오류 발생했는데 리스트는 값이 바뀔수 있어서 chosen을 그대로 넣으면 chosen이 바뀔 때 combi도 바뀜 따라서 새로운 리스트를 만들어서 넣어줘야함

n, m = map(int, input().split())
data = [[0]*n for _ in range(n)]

for i in range(n):
    data[i] = list(map(int, input().split()))

distances =[]

#집마다 치킨집 거리 찾음
for i in range(n):
    for j in range(n):
        if data[i][j]==1:
            distance=[]   
            for k in range(n):
                for l in range(n):
                    if data[k][l] == 2:
                        distance.append(abs(i-k) + abs(j -l))
            distances.append(distance)
#조합
combi=[]
def combination(arr, r):
    
    # 2.
    def generate(chosen):
        if len(chosen) == r:
            tempchosen = sorted(chosen)
            combi.append(tempchosen)
            return

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])
            
combinum = [ i for i in range(len(distances[0]))]
combination(combinum,m)

minsum=10000
for k in range(len(combi)):
    s=0
    for i in range(len(distances)):
        mindis=distances[i][combi[k][0]]
        for j in combi[k]:
            mindis = min(distances[i][j],mindis)
        s+=mindis
    minsum = min(minsum,s)

print(minsum)

#답
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) # 일반 집
        elif data[c] == 2:
            chicken.append((r, c)) # 치킨집

# 모든 치킨 집 중에서 m개의 치킨 집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨 집을 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨 집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
