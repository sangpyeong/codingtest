def solution(topping):
    answer = 0

    front_element = [0]*(max(topping)+1)
    back_element = [0]*(max(topping)+1)

    for i in range(len(topping)):
        back_element[topping[i]] += 1

    f_num = 0
    b_num = len(set(topping))
    for i in range(len(topping)):
        front_element[topping[i]] += 1
        back_element[topping[i]] -= 1
        if front_element[topping[i]] == 1:
            f_num += 1
        if back_element[topping[i]] == 0:
            b_num -= 1
        if f_num == b_num:
            answer += 1

    return answer
