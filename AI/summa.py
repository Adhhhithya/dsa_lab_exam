N=9
def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end=" ")
        print()
def isSafe(grid,row,col,num):
    for x in range(9):
        if grid[row][x]==num:
            return False
    for x in range(9):
        if grid[x][col]==num:
            return False
    startrow=row-row%3
    startcol=col-col%3
    for i in range(3):
        for j in range(3):
            if grid[i+startrow][j+startcol]==num:
                return False
    return True
def solveSudoku(grid,row,col):
    if(row==N-1 and col==N):
        return True
    if col==N:
        row+=1
        col=0
    if grid[row][col]>0:
        return solveSudoku(grid,row,col+1)
    for num in range(1,N+1,1):
        if isSafe(grid,row,col,num):
            grid[row][col]=num
            if solveSudoku(grid,row,col+1):
                return True
        grid[row][col]=0
    return False
grid=[
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0]
]
if solveSudoku(grid,0,0):
    printing(grid)
else:
    print("No solution exists")
        