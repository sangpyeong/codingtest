from collections import defaultdict, deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def search(x, y, map_list, visited, mode=1):
    result = [(0, 0)]
    visited[y][x] = True
    n = len(map_list)
    q = deque([(0, 0)])
    while q:
        mx, my = q.popleft()
        for k in range(4):
            ax, ay = x + mx + dx[k], y + my + dy[k]
            if -1 < ax < n and -1 < ay < n and map_list[ay][ax] == mode and not visited[ay][ax]:
                visited[ay][ax] = True
                q.append((mx + dx[k], my + dy[k]))
                result.append((mx + dx[k], my + dy[k]))
    print(result)
    return result


def rotate_list(lst):
    result = [lst.copy()]

    for k in range(3):
        tmp = list()
        for x, y in result[-1]:
            tmp.append((-y, x))
        result.append(tmp)
    print(result)
    return result


def make_piece_list(map_list):
    n = len(map_list)
    visited = [[False]*n for _ in range(n)]
    result = list()

    for i in range(n):
        for j in range(n):
            if map_list[i][j] and not visited[i][j]:
                tmp = search(j, i, map_list, visited)
                tmp_size = len(tmp)
                result.append([tmp_size] + rotate_list(tmp))

    return result


def is_inside(map_list, piece, x, y):
    n = len(map_list)
    for px, py in piece:
        ax, ay = x + px, y + py
        if ax < 0 or ay < 0 or ax >= n or ay >= n or map_list[ay][ax]:
            return False
    return True


def dfs(piece_list, map_list):
    n = len(map_list)
    m = len(piece_list)

    piece_visited = [False]*m
    visited = [[False]*n for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] or map_list[i][j]:
                continue
            empty_list = search(j, i, map_list, visited, 0)
            empty_size = len(empty_list)

            for ex, ey in empty_list:
                flg = False
                x, y = j + ex, i + ey

                for k in range(m):
                    if piece_visited[k]:
                        continue
                    piece_size = piece_list[k][0]
                    if piece_size != empty_size:
                        continue

                    for _piece in piece_list[k][1:]:
                        if is_inside(map_list, _piece, x, y):
                            result += piece_size
                            piece_visited[k] = True
                            flg = True
                            break
                    if flg:
                        break
                if flg:
                    break

    return result


def solution(game_board, table):
    piece_list = make_piece_list(table)
    answer = dfs(piece_list, game_board)

    return answer


# 내가 짠거 실패함
# from collections import deque
# import copy

# def solution(game_board, table):
#     answer = -1
#     #
#     length = len(game_board)
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     q = deque()
#     pieces = []
#     for i in range(length):
#         for j in range(length):
#             if table[i][j] == 1:
#                 x, y = i, j
#                 q.append([x, y])
#                 table[x][y] = 0
#                 piece = []
#                 while q:
#                     tx, ty = q.popleft()
#                     piece.append([tx - x, ty - y])
#                     for k in range(4):
#                         nx, ny = tx + dx[k], ty + dy[k]

#                         if 0 <= nx < length and 0 <= ny < length and table[nx][ny] == 1:
#                             q.append([nx, ny])
#                             table[nx][ny] = 0
#                 pieces.append(piece)
#     print(pieces)

#     rotated_pieces = []
#     for i in range(len(pieces)):
#         for k in range(4):
#             tmp_pieces = copy.deepcopy(pieces[i])
#             rotated_pieces.append(tmp_pieces)
#             for j in range(len(pieces[i])):
#                 tmp = pieces[i][j][0]
#                 pieces[i][j][0] = pieces[i][j][1]
#                 pieces[i][j][1] = -tmp

#     print(rotated_pieces)

#     visited = [[False] * length for _ in range(length)]
#     for i in range(length):
#         for j in range(lenght):
#             if game_board[i][j] == 0:
#                 x, y = i, j
#                 q.append([x, y])
#                 visited[x][y] = True
#                 piece = []
#                 while q:
#                     tx, ty = q.popleft()
#                     piece.append([tx - x, ty - y])
#                     for k in range(4):
#                         nx, ny = tx + dx[k], ty + dy[k]

#                         if 0 <= nx < length and 0 <= ny < length and visited[nx][ny] == False and game_board[nx][ny] == 0:
#                             q.append([nx, ny])
#                             visited[nx][ny] = True
#                 piece


#     return answer
