def solution(n, s):
    answer = []
    div = s//n
    mod = s % n

    if div == 0:
        return [-1]

    for i in range(n):
        if mod > 0:
            answer.append(div+1)
            mod -= 1
        else:
            answer.append(div)
    answer.reverse()
    return answer
