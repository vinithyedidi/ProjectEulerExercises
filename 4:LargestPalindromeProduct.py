# Problem 4:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 * 99. Find the largest palindrome made from the product of two 3-digit numbers.

def solution():
    potential_palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            x = i * j
            x_str = str(x)
            n = len(x_str)
            if x_str[0] == x_str[n-1]:
                if x_str[1] == x_str[n-2]:
                    if x_str[2] == x_str[n-3]:
                        potential_palindromes.append(x)
    return potential_palindromes

def main():
    sol = solution()
    print(sol)
    print(max(sol))


if __name__ == '__main__':
    main()
