def solution(A, B):
    answer = 0

    N = len(A)

    A.sort()
    B.sort()
    Aidx = 0
    Bidx = 0
    while Aidx < N and Bidx < N:
        if A[Aidx] > B[Bidx]:
            Bidx += 1
        elif A[Aidx] < B[Bidx]:
            Aidx += 1
            Bidx += 1
            answer += 1
        else:
            Bidx += 1

    return answer
