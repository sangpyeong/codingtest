def solution(s):
    answer = 0
    # 그리디 방법
    for i in range(len(s)):
        length_odd = 1
        length_even = 0
        for j in range(1, len(s)):
            if not (0 <= i+j < len(s)) or not (0 <= i-j < len(s)):
                break

            if s[i+j] == s[i-j]:
                length_odd += 2
            else:
                break
        if 0 <= i+1 < len(s) and s[i] == s[i+1]:
            length_even = 2
            for j in range(1, len(s)):
                if not (0 <= i+j+1 < len(s)) or not (0 <= i-j < len(s)):
                    break
                if s[i+j+1] == s[i-j]:
                    length_even += 2
                else:
                    break
        answer = max(answer, length_odd, length_even)

    return answer
# 다른 풀이


def isPalindrome(x):
    if x == x[::-1]:
        return True


def solution(s):
    MAX = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if isPalindrome(s[i:j]):
                if MAX < len(s[i:j]):
                    MAX = len(s[i:j])
    return MAX
