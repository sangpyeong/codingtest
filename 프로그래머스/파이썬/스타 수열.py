from collections import Counter


def solution(a):
    if len(a) < 2:
        return 0

    counter = Counter(a)
    counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    max_length = 0
    for num, _ in counter:
        if counter[0][1] * 2 <= max_length:
            break
        length = 0
        i = 0
        while i < len(a) - 1:
            if (a[i] != num and a[i+1] != num) or (a[i] == a[i+1]):
                i += 1
                continue
            length += 2
            i += 2
        max_length = max(max_length, length)
    return max_length
