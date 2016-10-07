"""
Euler 96 - Solve 50 Sudoku puzzles (recursively with backtracking in this case), concatenate
the three values on the first row in the upper left corner ~ ''.join([0][0:3]),
and sum these values.
"""
import time

def getCands(x, y, puzzle):
    # Initiates S as an empty set
    # Initiates T as an empty set and adds values from 1 to 9 inclusive
    T, S = set(), set()
    T.update(range(1, 10))

    # Add numbers found vertically and horizontally from puzzle[x][y] to set S
    S.update([puzzle[x][a] for a in range(0,9) if not puzzle[x][a] == 0])
    S.update([puzzle[b][y] for b in range(0,9) if not puzzle[b][y] == 0])

    # Add numbers found in 3x3 cell relative to puzzle[x][y] to set S
    for c in range((x//3)*3, (x//3)*3+3):
        for d in range((y//3)*3, (y//3)*3+3):
            if not puzzle[c][d] == 0:
                S.add(puzzle[c][d])

    # Return the symmetric difference between set S & set T
    return list(S.symmetric_difference(T))

def solve(puzzle):
    # Reduction Steps:
    # 1. Check for single solutions
    for i in range(0,9):
        for j in range(0,9):
            if puzzle[i][j] == 0:
                cands = getCands(i, j, puzzle)
                if len(cands) == 1:
                    puzzle = [row[:] for row in puzzle]
                    puzzle[i][j] = cands.pop()

    # 2. Recurse when multiple solutions possible
    for x in range(0,9):
        for y in range(0,9):
            if puzzle[x][y] == 0:
                cands = getCands(x, y, puzzle)
                if len(cands)== 0:
                    return []

                for n in cands:
                    puzzle = [row[:] for row in puzzle]
                    puzzle[x][y] = n
                    temp_table = solve(puzzle)
                    if temp_table:
                        puzzle = temp_table
                        if 0 not in puzzle:
                            return puzzle
                if not temp_table:
                    return []
    # Base Case:
    if 0 not in puzzle:
        return puzzle

def getPuzzles(s):
    puzzles = []
    with open(s) as f:
        lines = f.read()
    lines = lines.split('Grid')
    lines.pop(0)

    for puzzle in lines:
        p = []
        for x in range(0, 9):
            p.append([int(cell) for cell in puzzle[4+x*10:13+x*10]])
        puzzles.append(p)
    return puzzles

def main():
    puzzles = getPuzzles('p096_sudoku.txt')

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
    # Concatenates the 3 values found in the top row on the upper left ~ ''.join([0][0:3])
    # Sums the values for all 50 puzzles in text file
    print(sum([int(''.join(str(_) for _ in solve(puzzle)[0][0:3])) for puzzle in puzzles]))
    print((time.time() - t1)*1000, "ms")

if __name__ == "__main__":
    main()