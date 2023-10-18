def solution(max_weight, specs, names):
    answer = 1

    dic_spec = {}
    for spec in specs:
        if spec[0] not in dic_spec:
            dic_spec[spec[0]] = int(spec[1])

    st_weight = 0
    for name in names:
        if max_weight < st_weight + dic_spec[str(name)]:
            answer += 1
            st_weight = dic_spec[str(name)]
        else:
            st_weight += dic_spec[str(name)]

    return answer
