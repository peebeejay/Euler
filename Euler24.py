"""
Euler 24 - Find all possible permutations of a list of n elements. Elements can be repeated
within the list.

My progression is documented through the three methods. The function named permutations is
the first iteration of the function, while permutations3 is the final version of the
function that allows for repeated elements.
"""

def permutations(s, t, depth, l ):
    if len(t) == len(s):
        l.append(t)
        return
    for c in s:
        if c not in t:
            permutations(s, t+c, depth+1, l)

def permutations2(s, t, i, l ):
    if len(t) == len(s) and t not in l:
        l.append(t)
        return
    for x in range(len(s)):
        if str(x) not in i:
            permutations2(s, t+s[x], i+str(x), l)


def permutations3(s, t, i, l):
    if len(t) == len(s) and t not in l:
        l.append(t)
    for x in range(len(s)):
        if x not in i:
            permutations3(s, t+s[x], i + [x], l)

f = []
k = []

h = []
u = []

permutations("abc", "", 0, f)
permutations2("aac", "", "", k)
permutations3("aaacc", "", u, h)

print(f)
print(k)
print(h)


