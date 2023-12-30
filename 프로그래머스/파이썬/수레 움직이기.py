import heapq

# 1 -> 3
# 2 -> 4
# 자기 색깔이 지나온 곳과 5는 이동불가


def solution(maze):
    answer = 0

    redX, redY = 0, 0
    blueX, blueY = 0, 0
    redEndX, redEndY = 0, 0
    blueEndX, blueEndY = 0, 0
    redVisited = []
    blueVisited = []

    # 원래의 위치와 벽은 갈 수 없으니 미리 visited에 추가
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 1:
                redX, redY = row, col
                redVisited.append((row, col))
            elif maze[row][col] == 2:
                blueX, blueY = row, col
                blueVisited.append((row, col))
            elif maze[row][col] == 3:
                redEndX, redEndY = row, col
            elif maze[row][col] == 4:
                blueEndX, blueEndY = row, col
            elif maze[row][col] == 5:
                redVisited.append((row, col))
                blueVisited.append((row, col))
            else:
                continue

    answer = bfs(redX, redY, blueX, blueY, redEndX, redEndY,
                 blueEndX, blueEndY, maze, redVisited, blueVisited)
    return answer


def bfs(rx, ry, bx, by, rex, rey, bex, bey, maze, redVisited, blueVisited):
    q = []
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    heapq.heappush(q, (0, rx, ry, bx, by, redVisited, blueVisited))

    while q:
        cnt, crx, cry, cbx, cby, _redVisited, _blueVisited = heapq.heappop(q)
        redArrive = False
        blueArrive = False

        if (crx, cry) == (cbx, cby):
            continue
        if not redArrive and (crx, cry) == (rex, rey):
            redArrive = True
        if not blueArrive and (cbx, cby) == (bex, bey):
            blueArrive = True

        # 둘 다 도착 -> 종료
        # 한 쪽만 도착 -> 도착하지 못한 쪽의 위치만 갱신해서 우선순위 큐에 삽입
        # 둘 다 도착 X -> 양쪽다 위치 갱신해서 우선순위 큐에 삽입
        # 큐에 삽입 시 [:]로 각각의 경우마다 독립되게 넣어줘야 함
        if redArrive and blueArrive:
            return cnt
        elif redArrive:
            for dx, dy in direction:
                nbx, nby = cbx + dx, cby + dy

                # 맵 범위 밖
                if not (0 <= nbx < len(maze) and 0 <= nby < len(maze[0])):
                    continue
                # 조건을 만족하면 다음 위치 추가 후 새로운 경로로 우선순위 큐에 등록
                if not (nbx, nby) in _blueVisited:
                    _blueVisited.append((nbx, nby))
                    heapq.heappush(q, (cnt + 1, crx, cry, nbx,
                                   nby, _redVisited[:], _blueVisited[:]))
                    _blueVisited.pop()
        elif blueArrive:
            for dx, dy in direction:
                nrx, nry = crx + dx, cry + dy

                # 맵 범위 밖
                if not (0 <= nrx < len(maze) and 0 <= nry < len(maze[0])):
                    continue
                # 조건을 만족하면 다음 위치 추가 후 새로운 경로로 우선순위 큐에 등록
                if not (nrx, nry) in _redVisited:
                    _redVisited.append((nrx, nry))
                    heapq.heappush(q, (cnt + 1, nrx, nry, cbx,
                                   cby, _redVisited[:], _blueVisited[:]))
                    _redVisited.pop()
        else:
            for dbx, dby in direction:
                nbx, nby = cbx + dbx, cby + dby

                if not (0 <= nbx < len(maze) and 0 <= nby < len(maze[0])):
                    continue
                #################################
                if (nbx, nby) in _blueVisited:
                    continue
                _blueVisited.append((nbx, nby))
                #################################
                # 이렇게 하면 조건을 더 추가하지 않으면 append하지 않았음에도
                # 밑에서 pop으로 계속 빠져나감
                # if not (nbx, nby) in _blueVisited:
                #     _blueVisited.append((nbx, nby))

                for drx, dry in direction:
                    nrx, nry = crx + drx, cry + dry

                    # 서로 교차해서 움직일 때
                    if (nrx, nry) == (cbx, cby) and (nbx, nby) == (crx, cry):
                        continue
                    if not (0 <= nrx < len(maze) and 0 <= nry < len(maze[0])):
                        continue
                    if not (nrx, nry) in _redVisited:
                        _redVisited.append((nrx, nry))
                        heapq.heappush(
                            q, (cnt + 1, nrx, nry, nbx, nby, _redVisited[:], _blueVisited[:]))
                        _redVisited.pop()

                _blueVisited.pop()

    return 0
