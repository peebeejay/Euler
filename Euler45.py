# Euler45: Triangular, Pentagonal, Hexagonal
import math, time

def Triangularity(x):
    return (math.sqrt(8*x+1)-1)/2 % 1 == 0

def Pentagonality(x):
    return ((math.sqrt(24*x+1)+1)/6) % 1 == 0

def Hexagonality(x):
    return (math.sqrt(8*x+1)+1)/4 % 1 == 0

i = 1000
f = False
while not f:
    n = i*(2*i-1)
    if Pentagonality(n):
        print("Hit: ", i, n)
        f = True
    i+=1
