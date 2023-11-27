from itertools import product

def stri(alphabet, n):
    aper = ''.join(sorted(alphabet))
    tot = [''.join(x) for x in product(aper, repeat=n)]
    tot.sort()
    return tot

sym = "A B C D E F G H"
n = 3
alphabet = sym.split()
result = stri(alphabet, n)

for string in result:
    print(string)
