""" Euler96 is a Sudoku Solving Problem"""
import math
import time

def getPuzzles(s):
    # Currently returns only the first table

    with open(s) as f:
        lines = f.read()
    lines = lines.split('Grid')
    '''for x, line in enumerate(lines):
        print(line)
        if x == 10:
            break'''

    for x in range(0, 100):
        print("char", x, lines[1][x])

def printPuzzle(puzzle):
    for row in puzzle:
        print(row)

def valid(puzzle):
    t = set()
    t.update([1,2,3,4,5,6,7,8,9])

    # Check Horizontal Rows
    for hRow in puzzle:
        s = set()
        for cell in hRow:
            s.add(cell)
        if not s == t:
            return False

    # Check Vertical Rows
    for x in range(0,9):
        s = set()
        for y in range(0,9):
            s.add(puzzle[y][x])
        if not s == t:
            return False

    # Check Blocks
    for a in range(0,3):
        for b in range(0,3):
            s = set()
            for x in range(0+a*3,3+a*3):
                for y in range(0+b*3,3+b*3):
                    s.add(puzzle[x][y])
            if not s == t:
                return False

    if max([cell for row in puzzle for cell in row]) > 9:
        return False
    return True

def getCands(x, y, puzzle):
    t = set()
    s = set()
    t.update(range(1, 10))

    for a in range(0,9):
        if not puzzle[x][a] == 0:
            s.add(puzzle[x][a])

    for b in range(0,9):
        if not puzzle[b][y] == 0:
            s.add(puzzle[b][y])

    for c in range((x//3)*3, (x//3)*3+3):
        for d in range((y//3)*3, (y//3)*3+3):
            if not puzzle[c][d] == 0:
                s.add(puzzle[c][d])

    return list(s.symmetric_difference(t))

def solve(puzzle):
    # Base Case:
    if 0 not in puzzle and valid(puzzle) is True:
        return puzzle

    # Reduction Step:
    for x in range(0,9):
        for y in range(0,9):
            if puzzle[x][y]>9:
                return []
            if puzzle[x][y] == 0:
                cands = getCands(x, y, puzzle)
                if len(cands)== 0:
                    return []

                temp_table = []
                for n in cands:
                    puzzle = [row[:] for row in puzzle]
                    puzzle[x][y] = n

                    temp_table = solve(puzzle)

                    if temp_table:
                        puzzle = [row[:] for row in temp_table]
                        if valid(puzzle):
                            return puzzle

                if not temp_table:
                    return []

def main():
    # getPuzzles(r'C:\Users\Jay Puntham-Baker\Documents\Programs\Euler\p096_sudoku.txt')
    _puzzle = [[0,0,3,0,2,0,6,0,0],
              [9,0,0,3,0,5,0,0,1],
              [0,0,1,8,0,6,4,0,0],
              [0,0,8,1,0,2,9,0,0],
              [7,0,0,0,0,0,0,0,8],
              [0,0,6,7,0,8,2,0,0],
              [0,0,2,6,0,9,5,0,0],
              [8,0,0,2,0,3,0,0,9],
              [0,0,5,0,1,0,3,0,0]]

    medium_puzzle = [[0,0,0,6,8,0,0,0,1],
                     [9,8,3,0,5,0,0,0,0],
                     [0,0,0,0,0,0,5,0,0],
                     [4,9,0,0,7,0,1,0,5],
                     [0,0,0,0,0,0,0,0,0],
                     [2,0,5,0,4,0,0,7,8],
                     [0,0,4,0,0,0,0,0,0],
                     [0,0,0,0,2,0,3,5,6],
                     [5,0,0,0,9,8,0,0,0]]

    hard_puzzle = [[0,8,0,0,0,0,0,0,0],
                   [0,0,9,1,0,0,2,0,0],
                   [4,1,0,0,5,0,3,0,7],
                   [0,0,0,6,0,0,0,0,0],
                   [9,4,0,8,0,1,0,7,2],
                   [0,0,0,0,0,9,0,0,0],
                   [6,0,8,0,7,0,0,1,3],
                   [0,0,3,0,0,0,8,0,0],
                   [0,0,0,0,0,0,0,9,0]]

    superHard_puzzle = [[8,0,0,0,0,0,0,0,0],
                        [0,0,3,6,0,0,0,0,0],
                        [0,7,0,0,9,0,2,0,0],
                        [0,5,0,0,0,7,0,0,0],
                        [0,0,0,0,4,5,7,0,0],
                        [0,0,0,1,0,0,0,3,0],
                        [0,0,1,0,0,0,0,6,8],
                        [0,0,8,5,0,0,0,1,0],
                        [0,9,0,0,0,0,4,0,0]]

    t1 = time.time()
    fin = solve(superHard_puzzle)
    print((time.time() - t1)*1000, "ms")

    for row in fin:
        print(row)



if __name__ == "__main__":
    main()