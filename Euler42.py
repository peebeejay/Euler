# Euler 42: Coded Triangle Numbers

def getWords(s):
    with open(s) as f:
        lines = f.read()
        lines = lines.split(',')
        return [word[1:len(word) - 1] for word in lines]

def triangleNumbers(n):
    return [int(1/2*x*(x+1))for x in range(1, n)]

wordList = getWords('p042_words.txt')
tnums = triangleNumbers(100)

print(len([sum([ord(c)-96 for c in word.lower()])
         for word in wordList
         if sum([ord(c)-96 for c in word.lower()]) in tnums]))
