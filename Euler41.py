# Euler 41: Largest Pandigital (1-9) Prime

def isPandigital(n):
    if len(str(n)) == 7:
        for x in range(1, 8):
            if str(x) not in str(n):
                return False
        return True

def eratosthenes(n):
    multiple = set()
    for i in range(2, n):
        if i not in multiple:
            multiple.update(range(i*i, n+1, i))
            if isPandigital(i):
                yield i

bound = 9999999
print(max(list(eratosthenes(bound))))
