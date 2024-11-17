# perm

import itertools

def perms(n):
    permutations = list(itertools.permutations(range(1, n + 1)))
    print(len(permutations))
    
    for perm in permutations:
        print(" ".join(map(str, perm)))


n = 3
perms(n)
