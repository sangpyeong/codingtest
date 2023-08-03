def solution(n, t, m, p):
    answer = ''
    arr = []
    num = 0
    length = 0
    while length < t*m:
        tmp_num = num
        tmp_arr = []
        if tmp_num == 0:
            arr.append(0)
            num += 1
            continue
        while tmp_num / n != 0:
            if tmp_num % n == 10:
                tmp_arr.append('A')
            elif tmp_num % n == 11:
                tmp_arr.append('B')
            elif tmp_num % n == 12:
                tmp_arr.append('C')
            elif tmp_num % n == 13:
                tmp_arr.append('D')
            elif tmp_num % n == 14:
                tmp_arr.append('E')
            elif tmp_num % n == 15:
                tmp_arr.append('F')
            else:
                tmp_arr.append(tmp_num % n)
            tmp_num = tmp_num // n
            length += 1

        tmp_arr.reverse()
        arr.extend(tmp_arr)
        num += 1
    for i in range(p-1, p+m*(t-1), m):
        answer += str(arr[i])

    return answer

# 다른 사람 풀이

# n진수로 변환하는 함수


def convert(number, n):
    if number == 0:
        return '0'
    NUMBERS = "0123456789ABCDEF"
    res = ""
    while number > 0:
        number, mod = divmod(number, n)
        res += NUMBERS[mod]
    return res[::-1]


def solution(n, t, m, p):
    answer = ''
    game = ''
    cur = p - 1
    for num in range(t * m):
        game += convert(num, n)
    while 1:
        if len(answer) == t:
            break
        answer += game[cur]
        cur += m
    return answer
