"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

import math
import time



# Recursive Solution 1
def coinsum(t, c):
    if t == 0 or (c+1 == len(coinset) and t % coinset[c] == 0):
        return 1
    elif c+1 == len(coinset) and t % coinset[c] != 0:
        return 0
    elif c+1 < len(coinset):
        sum = 0
        for i in range(0, math.floor(t/coinset[c])+1, 1):
            if memo[t][c] > 0:
                return memo[t][c]
            else:
                sum += coinsum(t-i*coinset[c], c+1)
        memo[t][c] = sum
        return sum


coinset = [9, 8, 7, 6, 5, 4, 3, 2, 1]
_t = 45
_total = 0
memo = [[0]*(len(coinset)+1) for _ in range(_t+1)]

t1 = time.time()
print("Total:", coinsum(_t, 0), "\nTime:", (time.time()-t1))


# Dynamic Programming Solution
coinset = [1, 2, 5, 10]
amount = 6
coins = len(coinset)

ways = [1] + [0]*amount

for i in range(0, coins):
    for j in range(coinset[i], amount+1):
        ways[j] = ways[j] + ways[j-coinset[i]]
    print(ways)
print(ways)
