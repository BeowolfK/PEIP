grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

print("╔═══SUDOKU NON RESOLU═══╗")
for k in range(len(grid)):
    line = '‖ '
    for l in range(len(grid[k])):
        if l % 3 == 0 and l != 0 :
            line += '‖ ' + f'{ grid[k][l]} '
        elif l == 8 :
            line += f'{ grid[k][l]} ' + '‖'
        else :
            line += f'{ grid[k][l]} '
    if k % 3 == 0: 
        print("╠"+"═══════╬"*2+"═══════"+"╣")
    print(line)
print("╚"+"═══════╩"*2+"═══════"+"╝")
    
def possible(row, column, number, grid):
    #Is the number appearing in the given row?
    
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    #Is the number appearing in the given column?
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    
    #Is the number appearing in the given square?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False

    return True

def solve(grid):
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number, grid):
                        grid[row][column] = number
                        solve(grid)
                grid[row][column] = 0
                return
    print("╔═════SUDOKU RESOLU═════╗")
    for k in range(len(grid)):
        line = '‖ '
        for l in range(len(grid[k])):
            if l % 3 == 0 and l != 0 :
                line += '‖ ' + f'{ grid[k][l]} '
            elif l == 8 :
                line += f'{ grid[k][l]} ' + '‖'
            else :
                line += f'{ grid[k][l]} '
        if k % 3 == 0: 
            print("╠"+"═══════╬"*2+"═══════"+"╣")
        print(line)
    print("╚"+"═══════╩"*2+"═══════"+"╝")
    exit()

solve(grid)
