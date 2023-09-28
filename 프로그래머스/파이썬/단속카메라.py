def solution(routes):
    answer = 0

    sorted_routes = sorted(routes, key=lambda x: x[1])
    nums = [sorted_routes[0][1]]

    for i in range(len(sorted_routes)):
        if sorted_routes[i][0] <= nums[-1] <= sorted_routes[i][1]:
            continue
        nums.append(sorted_routes[i][1])

    answer = len(nums)

    return answer
