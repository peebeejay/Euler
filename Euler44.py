# Euler 44: Pentagon Numbers

def pentagonNumbers(n):
    return [int(x/2*(3*x-1))for x in range(1, n)]

s = pentagonNumbers(2500)

def solution1():
    for x in range(len(s)):
        for y in range(x, len(s)):
            dif = s[y] - s[x]
            sm = s[x] + s[y]
            if dif in s:
                if sm in s:
                    print(x, y, sm, dif)
