# def solution(dirs):
#     answer = 0
#     #좌표
#     maps = [[""]*11 for _ in range(11)]
#     #이동
#     start = [5,5]
#     for i in range(len(dirs)):
#         if dirs[i] == 'U' and start[0]>=1:
#             if "U" not in maps[start[0]][start[1]]:
#                 maps[start[0]][start[1]] += "U"
#                 answer+=1
#                 start[0] -= 1
#                 maps[start[0]][start[1]] += "D"
#             else:
#                 start[0] -= 1

#         elif dirs[i] == 'D' and start[0]<=9:
#             if "D" not in maps[start[0]][start[1]]:
#                 maps[start[0]][start[1]] += "D"
#                 answer+=1
#                 start[0] += 1
#                 maps[start[0]][start[1]] += "U"
#             else:
#                 start[0] += 1

#         elif dirs[i] == 'R' and start[1]<=9:
#             if "R" not in maps[start[0]][start[1]]:
#                 maps[start[0]][start[1]] += "R"
#                 answer+=1
#                 start[1] += 1
#                 maps[start[0]][start[1]] += "L"
#             else:
#                 start[1] += 1

#         elif dirs[i] == 'L' and start[1]>=1:
#             if "L" not in maps[start[0]][start[1]]:
#                 maps[start[0]][start[1]] += "L"
#                 answer+=1
#                 start[1] -= 1
#                 maps[start[0]][start[1]] += "R"
#             else:
#                 start[1] -= 1


#     return answer


def solution(dirs):
    sets = set()
    y, x = 0, 0
    udrl = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}

    for d in dirs:
        dy, dx = udrl[d]
        ny = y + dy
        nx = x + dx
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            sets.add(((y, x), (ny, nx)))
            sets.add(((ny, nx), (y, x)))
            y = ny
            x = nx
    return len(sets) // 2
