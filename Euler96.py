import time

def valid(puzzle):
    t = set()
    t.update(range(1,10))

    # Check Horizontal Rows
    for hRow in puzzle:
        s = set()
        s.update([cell for cell in hRow])
        if not s == t:
            return False

    # Check Vertical Rows
    for x in range(0,9):
        s = set()
        s.update([puzzle[y][x] for y in range(0,9)])
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
    # Reduction Steps:
    for i in range(0,9):
        for j in range(0,9):
            if puzzle[i][j] == 0:
                cands = getCands(i, j, puzzle)
                if len(cands) == 1:
                    puzzle = [row[:] for row in puzzle]
                    puzzle[i][j] = cands.pop()

    for x in range(0,9):
        for y in range(0,9):
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

    # Base Cases:
    if max([cell for row in puzzle for cell in row]) > 9:
        return []
    elif 0 not in puzzle and valid(puzzle) is True:
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
            l = []
            l.extend([int(cell) for cell in puzzle[4+x*10:13+x*10]])
            p.append(l)
        puzzles.append(p)
    return puzzles

def main():
    puzzles = getPuzzles(r'C:\Users\Jay Puntham-Baker\Documents\Programs\Euler\p096_sudoku.txt')

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
    print(sum([int(''.join(str(_) for _ in solve(puzzle)[0][0:3])) for puzzle in puzzles]))
    print((time.time() - t1)*1000, "ms")

if __name__ == "__main__":
    main()