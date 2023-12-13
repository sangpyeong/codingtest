def solution(n):
    sieve = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * 2, n, i):
                sieve[j] = False

    prime_numbers = [i for i in range(2, n) if sieve[i]]
    cb = []

    def combi(start, list):
        if len(list) == 3:
            if sum(list) == n:
                cb.append(list)
            return
        for i in range(start, len(prime_numbers)):
            combi(i+1, list + [prime_numbers[i]])

    combi(0, [])
    print(cb)
    return len(cb)


print(solution(33))
