from itertools import permutations
from itertools import product

# 내 풀이


def solution(user_id, banned_id):
    def backtrack(index):
        if index == len(banned_id):
            nonlocal answer
            temp_set = set(combination)  # 중복된 아이디를 방지하기 위해 set으로 변환
            if len(temp_set) == len(banned_id):
                answer.add(tuple(sorted(temp_set)))  # 중복 제거 후 정렬하여 추가
            return

        for user in table[index]:
            if not used[user]:
                used[user] = True
                combination.append(user)
                backtrack(index + 1)
                used[user] = False
                combination.pop()

    answer = set()  # 중복된 조합을 방지하기 위해 set 사용
    table = []
    used = {}  # 아이디 사용 여부를 기록
    combination = []  # 가능한 조합을 저장

    for i in range(len(banned_id)):
        banned_length = len(banned_id[i])
        banned_id_list = []
        for j in range(len(user_id)):
            user_length = len(user_id[j])
            if banned_length != user_length:
                continue

            case = True
            for k in range(banned_length):
                if banned_id[i][k] == "*":
                    continue
                elif banned_id[i][k] != user_id[j][k]:
                    case = False
                    break
            if case:
                banned_id_list.append(user_id[j])
                used[user_id[j]] = False

        table.append(banned_id_list)
    backtrack(0)
    return len(answer)


# 다른 사람 풀이
def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))
    ban_set = []

    for users in user_permutation:
        if not check(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in ban_set:
                ban_set.append(users)

    return len(ban_set)
