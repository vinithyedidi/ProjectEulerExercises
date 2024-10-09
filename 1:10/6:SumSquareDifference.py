# Problem 6:
# The sum of the squares of the first ten natural numbers is 385. The square of the sum of the first ten natural numbers
# is 3025. Hence the difference between the sum of the squares of the first ten natural numbers and the square of the
# sum is 2640. Find the difference between the sum of the squares of the first one hundred natural numbers and the
# square of the sum.

def solution(n):
    diff = 0
    sum_sq = 0
    sq_sum = 0
    for i in range(1, 101):
        sum_sq += (i*i)
        sq_sum += i
    sq_sum = sq_sum * sq_sum
    diff = sum_sq - sq_sum
    return diff


def main():
    sol = solution(100)
    print(sol)


if __name__ == '__main__':
    main()
