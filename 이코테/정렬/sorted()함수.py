array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result_1 = sorted(array) #sorted 함수

array.sort() # sort함수 별도의 정렬된 리스트가 반환되지 않고, 내부 원소가 바로 정렬

print(result_1)
print("------------")
print(array)


array_1 = [("바나나", 2), ("사과", 5), ("당근", 3)]

def setting(data):
  return data[1]

result = sorted(array_1, key = setting)
print(result)