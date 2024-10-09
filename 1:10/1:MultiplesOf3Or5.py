# Problem 1:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

def solution(n):
    sum = 0
    for x in range(n):
        if x % 3 == 0:
            sum += x
        if x % 5 == 0 and x % 3 != 0:
            sum += x
    return sum


def main():
    sol = solution(1000)
    print(sol)


if __name__ == '__main__':
    main()
