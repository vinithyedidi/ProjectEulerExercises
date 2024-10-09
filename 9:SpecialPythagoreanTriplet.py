# Problem 9:
# A Pythagorean triplet is a set of three natural numbers a, b, c for which a^2 + b^2 = c^2. There exists exactly one
# Pythagorean triplet for which a + b + c = 1000. Find the product abc.


def solution():
    potential_triplets = []
    for i in range(1, 1000):
        for j in range(1, 1000):
            for k in range(1, 1000):
                if i+j+k == 1000:
                    potential_triplets.append([i, j, k])
    print('Compiled list of triplets a + b + c = 1000')

    pythagorean_triplet = None
    for triplet in potential_triplets:
        if triplet[0]**2 + triplet[1]**2 == triplet[2]**2:
            pythagorean_triplet = triplet

    return pythagorean_triplet

def main():
    sol = solution()
    print(f'Solution = {sol}.')
    print(sol[0] * sol[1] * sol[2])


if __name__ == '__main__':
    main()