def sudoku2(grid):
    aski = ord("1")
    for i in range(0,9):
        checker = [0]*9
        for j in range(0,9):
            if grid[i][j] != ".":
                checker[ord(grid[i][j])-aski] = checker[ord(grid[i][j])-aski] + 1
        for k in range(0,9):
            if checker[k] > 1:
                return False
    
    for i in range(0,9):
        checker = [0]*9
        for j in range(0,9):
            if grid[j][i] != ".":
                checker[ord(grid[j][i])-aski] = checker[ord(grid[j][i])-aski] + 1
        for k in range(0,9):
            if checker[k] > 1:
                return False
    
    for i in range(0,3):
        for j in range(0,3):
            checker = [0] * 9
            for k in range(0,3):
                for l in range(0,3):
                    if grid[k+i*3][l+j*3] != ".":
                        checker[ord(grid[k+i*3][l+j*3])-aski] = checker[ord(grid[k+i*3][l+j*3])-aski] + 1
            for m in range(0,9):
                if checker[m] > 1:
                    return False
    
    return True
