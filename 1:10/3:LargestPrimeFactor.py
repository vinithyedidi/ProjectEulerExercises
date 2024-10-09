# Problem 3:
# The prime factors of 13195 are 5, 7, 13, and 29. What is the largest prime factor of the number 600851475143?

def solution(n):
    factors = []
    for x in range(1, 10000):
        if n % x == 0:
            factors.append(x)
    return factors


def main():
    sol = solution(600851475143)
    print(max(sol))


if __name__ == '__main__':
    main()
