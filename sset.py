def count_subsets(n):
    return (2 ** n) % 1000000

n = 879
result = count_subsets(n)
print(result)
