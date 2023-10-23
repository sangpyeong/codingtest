def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_list = list(skill)
        for s in skill_tree:
            if s in skill and s != skill_list.pop(0):
                break
        else:  # for-else 문법을 사용하면 dirty flag를 제거할 수 있고 파이썬스럽게 푼 느낌이 든다.
            answer += 1

    return answer
