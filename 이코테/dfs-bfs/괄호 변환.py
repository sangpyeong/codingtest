from collections import deque


def right(w):
    st = deque()
    for i in w:
        if i == '(':
            st.append(i)
        elif i == ')':
            if len(st) == 0:
                return False
            else:
                st.pop()
    if len(st) == 0:
        return True
    else:
        return False


def modi(p):
    st = deque()
    for i in range(len(p)):
        if p[i] == p[0]:
            st.append(i)
        else:
            if len(st) == 0:
                u = p[0:i]
                v = p[i:len(p)]
            else:
                st.pop()
    if right(u):
        answer += u
        if len(v) > 0:
            modi(v)
        else:
            return
    else:
        modi(v)


def solution(p):
    global answer
    if right(p):
        answer = p
    else:
        modi(p)

    return answer
