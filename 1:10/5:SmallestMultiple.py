# Problem 5:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is
# the smallest positive number that is evenly divisible by all numbers from 1 to 20?

def solution():
    num = 2520 * 11 * 13 * 2 * 17 * 19
    verification = True
    for i in range(1, 21):
        if num % i != 0:
            verification = False
            print(f'Verification failed at i={i}')
    return num


def main():
    sol = solution()
    print(sol)


if __name__ == '__main__':
    main()
