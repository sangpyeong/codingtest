# def solution(n, results):
#     answer = 0
#     #링크드리스트처럼 연결된 구조가 있어야 함


#     #dic으로 위 아래만 가지고 있으면 해결 되나?
#     #일단 전부 다 상대했으면 순위를 알 수 있음 근데 예시에 5번 선수는 어떻게 처리해야하지
#     #그래프로 될거 같은데?
#     #안되나? 일단 2번이 4등인건 알 수 잇음 근데 5번은 어케알지? 생각해보자 모르겠음 그냥 정답 보자

#     return answer
def solution(n, results):
    answer = 0
    board = [[0]*n for _ in range(n)]

    for a, b in results:
        board[a-1][b-1] = 1
        board[b-1][a-1] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or board[i][j] in [1, -1]:
                    continue
                if board[i][k] == board[k][j] == 1:
                    board[i][j] = 1
                    board[j][i] = board[k][i] = board[j][k] = -1
    for row in board:
        if row.count(0) == 1:
            answer += 1
    return answer
