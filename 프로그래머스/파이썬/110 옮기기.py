# 시간초과, 오답
# import heapq


# def solution(s):
#     answer = []

#     # 뒤에서 110, 111 찾고 교환 반복 근데 시간초과 생각해야함
#     # 바뀌는 부분이 교환하는 곳 뒤만 확인하면 됨
#     # 110, 111 빠르게 찾는 방법->직접 찾는 방법 이외 생각 안남
#     for i in range(len(s)):
#         heap_110 = []
#         heap_111 = []
#         # 110, 111 인덱스 찾기
#         for j in range(len(s[i])-2):
#             if s[i][j] == '1' and s[i][j+1] == '1':
#                 if s[i][j+2] == '1':
#                     heapq.heappush(heap_111, j)
#                 elif s[i][j+2] == '0':
#                     heapq.heappush(heap_110, -j)
#         tmp_list = list(s[i])
#         while heap_110 and heap_111:
#             num_110, num_111 = heapq.heappop(
#                 heap_110) * -1, heapq.heappop(heap_111)
#             if num_111 < num_110:
#                 tmp_list[num_111+2] = '0'
#                 tmp_list[num_110+2] = '1'
#                 if num_111+1 in heap_111:
#                     heapq.heappop(heap_111)
#                 if num_111+2 in heap_111:
#                     heapq.heappop(heap_111)
#                 if num_110 + 4 < len(tmp_list) and tmp_list[num_110 + 3] == '1' and tmp_list[num_110 + 4] == '0':
#                     heapq.heappush(heap_110, (num_110+2)*-1)
#             else:
#                 break

#         answer.append(''.join(tmp_list))

#     return answer


# 정답
# 110 다 추출하고 111앞에 넣기
def solution(s):
    answer = []

    for string in s:
        stack = []
        count_110 = 0
        for str in string:
            # 110이 나온 경우
            if (len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1' and str == '0'):
                count_110 += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(str)

        # 110을 모두 제거했으므로 남은 문자열에서 연속된 1이 존재하는 곳은 한 곳밖에 없다.
        count_1 = 0
        for s in stack[::-1]:
            if s == '0':
                break
            else:
                count_1 += 1
        answer.append(
            ''.join(stack[:len(stack) - count_1]) + '110' * count_110 + '1' * count_1)
    return answer


solution(["10101011110110111110"])
