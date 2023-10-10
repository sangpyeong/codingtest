def solution(gems):
    gem_types = set(gems)
    gem_count = len(gem_types)

    start, end = 0, 0
    current_gems = {gems[0]: 1}
    result = [0, len(gems) - 1]

    while start < len(gems) and end < len(gems):
        if len(current_gems) == gem_count:
            if end - start < result[1] - result[0]:
                result = [start, end]

            if current_gems[gems[start]] == 1:
                del current_gems[gems[start]]
            else:
                current_gems[gems[start]] -= 1

            start += 1
        else:
            end += 1
            if end == len(gems):
                break

            if gems[end] in current_gems:
                current_gems[gems[end]] += 1
            else:
                current_gems[gems[end]] = 1

    return [result[0] + 1, result[1] + 1]
