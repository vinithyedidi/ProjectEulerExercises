# Problem 7:
# By listing the first six prime numbers, we can see that the 6th prime is 13. What is the 10001st prime number?


def solution(n):
    primes = [2, 3]
    x = 4

    while len(primes) <= 10001:
        print(f'\rTrying {x}: Found {len(primes)} primes so far.', end='')
        has_prime_factor = False
        for p in primes:
            if x % p == 0:
                has_prime_factor = True
        if not has_prime_factor:
            primes.append(x)
        x += 1

    return primes


def main():
    sol = solution(100)
    print()
    print(sol[len(sol)-2])


if __name__ == '__main__':
    main()