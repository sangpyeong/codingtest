from collections import deque

N, M = map(int, input().split())
board = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
red = []
blue = []

for i in range(N):
    row = list(input())
    if "R" in row:
        red = [i, row.index("R")]
    if "B" in row:
        blue = [i, row.index("B")]

    board.append(row)
board[blue[0]][blue[1]] = "."

start = [red[0], red[1], blue[0], blue[1], 0]
visited = [[False]*M for _ in range(N)]

dq = deque()
dq.append(start)
visited[start[0]][start[1]] = True
while dq:
    rx, ry, bx, by, count = dq.popleft()
    if count > 10:
        print(-1)
        break
    for i in range(4):
        nrx, nry = rx + dx[i], ry + dy[i]
        if 1 <= nrx < N-1 and 1 <= nry < M-1 and board[nrx][nry] != "#":
            overlap = False
            fail = False
            end = False
            for j in range(max(N, M)):
                if nrx == bx and nry == by:
                    overlap = True
                    nrx += dx[i]
                    nry += dy[i]
                elif board[nrx][nry] == ".":
                    nrx += dx[i]
                    nry += dy[i]
                elif board[nrx][nry] == "#":
                    if overlap:
                        nrx = nrx - dx[i]
                        nry = nry - dy[i]
                    nrx = nrx - dx[i]
                    nry = nry - dy[i]
                    break
                elif board[nrx][nry] == "O":
                    if overlap:
                        fail = True
                    else:
                        end = True
                    break

            B_overlap = False
            nbx, nby = bx, by
            for j in range(max(N, M)):
                nbx, nby = nbx + dx[i], nby + dy[i]
                if nbx == rx and nby == ry:
                    B_overlap = True
                elif board[nbx][nby] == ".":
                    pass
                elif board[nbx][nby] == "#":
                    if B_overlap:
                        nbx = nbx - dx[i]
                        nby = nby - dy[i]
                    nbx = nbx - dx[i]
                    nby = nby - dy[i]
                    break
                elif board[nbx][nby] == "O":
                    fail = True
                    end = False
                    break

            if not fail:
                visited[nrx][nry] = True
                dq.append([nrx, nry, nbx, nby, count+1])
            if end:
                print(count+1)
                break
    if end:
        break
