n = int(input())
arr = list(map(int, input().split(" ")))

arr.sort()

result = 0
i = 0

while i < len(arr):
    i += arr[i]
    result += 1

print(result-1)


##################################
# 정답
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹 수
count = 0  # 현재 그룹에 포함된 모험가 수

for i in data:  # 공포도를 낮은 것부터 하나씩 확인
    count += 1  # 현재 그룹에 해당 모험가를 포함시킴
    if count >= i:  # 현재 그룹의 모험가 수가 현재의 공포도 이상이면, 그룹 결성
        result += 1  # 총 그룹의 수 증가시킴
        count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(result)

#############
# 내가 푼게 맞는지 모르겠음
