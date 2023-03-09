n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n%=coin

print(count)

# 그리디 알고리즘의 정당성을 검토해야함
# 만약 동전이 배수가 형태가 아니면 최적의 해가 아님




