# Problem 10:
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million.


def solution(n):
    primes = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    sum = 0
    for p in range(2, n + 1):
        if primes[p]:
            sum += p
    return sum


def main():
    sol = solution(2000000)
    print(f'Solution = {sol}.')


if __name__ == '__main__':
    main()