def solution(participant, completion):
    dic = {}
    for p in participant:
        dic[p] = dic.get(p, 0) + 1
    for c in completion:
        dic[c] -= 1
    dnf = [k for k, v in dic.items() if v > 0]
    answer = dnf[0]
    return answer
