T = int(input())
for tc in range(1, T+1):
    N = int(input())
    answer = 0
    def bt(l):
        global answer
        if len(l) == N:
            answer += 1
            return
        for i in range(N):
            check = False
            if l and i in l:
                continue
            for j in range(len(l)):
                if abs(l[j] - i) == abs(j - len(l)):
                    check = True
                    break
            if check:
                continue
            l.append(i)
            bt(l)
            l.pop()

    bt([])
    print(f"#{tc} {answer}")

