import time

def getCands(x, y, puzzle):
    t, s = set(), set()
    t.update(range(1, 10))

    s.update([puzzle[x][a] for a in range(0,9) if not puzzle[x][a] == 0])
    s.update([puzzle[b][y] for b in range(0,9) if not puzzle[b][y] == 0])

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
                        if 0 not in puzzle:
                            return puzzle
                if not temp_table:
                    return []
    # Base Cases:
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