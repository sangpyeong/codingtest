from itertools import combinations


def solution(n):
    sieve = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        print(i)
        if sieve[i]:
            for j in range(i * 2, n, i):
                sieve[j] = False

    prime_numbers = [i for i in range(2, n) if sieve[i]]
    l = [sum(c) for c in combinations(prime_numbers, 3)]
    return [sum(c) for c in combinations(prime_numbers, 3)].count(n)


solution(33)
