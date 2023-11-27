import math

def cunr(n):
    return math.prod(range(2*n-5, 1, -2)) % 10**6

def main():
    n = 888
    count = cunr(n)
    print(count)

if __name__ == '__main__':
    main()
