#문자열과 리스트는 다르다, 리스트는 mutable, 문자열은 immutable이고 내장함수도 다르다
#join함수 사용법(리스트를 문자열로 변환)  
s = input()
result = ""
sum = 0
for i in range(len(s)):
    if s[i] >= '0' and s[i] <= '9':
        sum += int(s[i])
    else:
        result = result + s[i]
result = str(sorted(result))
result = result + str(sum)

print(result)

#답
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))