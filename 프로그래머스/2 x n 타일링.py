def solution(n):
    answer = 0
    if n == 1:
        answer = 1
    elif n == 2:
        answer = 2
    else:
        a = 1
        b = 2
        c = 0
        for i in range(3, n+1):
            c = a + b
            a = b
            b = c
        answer = c % 1000000007

    return answer
