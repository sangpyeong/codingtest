#문제그대로 따라감, join으로 리스트를 문자열로 바꿈, 쉽게함


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
    u = ""
    v = ""
    global answer
    if p == "":
        return p
    for i in range(len(p)): # 균형 u, v 나눔
        if p[i] == p[0]:
            st.append(i)
        else:
            st.pop()
        if len(st)==0:
            u = p[0:i+1]
            v = p[i+1:len(p)]
            break


    if right(u): #u가 올바른인 경우

        if len(v) > 0: #v가 존재하면 재귀
            answer += u
            modi(v)
        else: #v가 없다면 그대로 반환
            return u
    else: #u가 올바르지 않은 경우
        tmp = "("
        tmp += modi(v)
        tmp += ")"
        for i in range(1, len(u)-1):
            if u[i] == "(":
                tmp += ")"
            else:
                tmp += "("
        answer += tmp


def solution(p):
    global answer
    answer = ""
    if right(p):
        answer = p
    else:
        modi(p)

    return answer


solution("(())))(())((")

#정답
# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# "올바른 괄호 문자열"인지 판단
def check_proper(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1
    return True # 쌍이 맞는 경우에 True 반환

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer
