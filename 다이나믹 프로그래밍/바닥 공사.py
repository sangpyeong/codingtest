import sys
input = sys.stdin.readline

n = int(input())

# 타일길이가 n일때 index n까지 나타내기 위해
# 리스트의 길이를 n + 1까지 설정
d = [0] * (n + 1)

# 타일 길이가 1, 2 일 때 값 설정
d[1] = 1
d[2] = 3

# index를 n까지 나타내기 위해 range를 n + 1까지 설정
for x in range(3, n + 1):
    # 타일 최대 길이가 2이기 때문에, 두가지 경우 존재
    # 길이가 1 남을땐 경우의 수 1,
    # 길이가 2 남을땐 경우의 수 2 -> 따라서 2를 곱함
    d[x] = d[x - 1] + (d[x - 2] * 2)

# 796796을 나눈 나머지 값 출력
print(d[n] % 796796)
