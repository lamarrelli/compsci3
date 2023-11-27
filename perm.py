from itertools import permutations

n = 5
def permut(n):
    perms = list(permutations(range(1, n + 1)))
    total_permutations = len(perms)

    return total_permutations, perms


perm= permut(n)
print(perm)