import numpy as np

grid=[[5, 3, 0, 0, 7, 0, 0, 0, 0],
      [6, 0, 0, 1, 0, 5, 0, 0, 0],
      [0, 9, 8, 0, 0, 0, 0, 6, 0],
      [8, 0, 0, 0, 6, 0, 0, 0, 3],
      [4, 0, 0, 8, 0, 3, 0, 0, 1],
      [7, 0, 0, 0, 2, 0, 0, 0, 6],
      [0, 6, 0, 0, 0, 0, 2, 8, 0],
      [0, 0, 0, 4, 1, 9, 0, 0, 5],
      [0, 0, 0, 0, 8, 0, 0, 0, 0]]

# print(np.matrix(grid))

def is_possible(num, row, col):
    global grid
    # check number is present in colomn
    for i in range(0,9):
        if(grid[row][i]==num):
            return False

    # check number in row   
    for j in range(0,9):
        if(grid[j][col]==num):
            return False
    # check number in given square  
    x0= (row//3)*3
    y0= (col//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if(grid[x0+i][y0+j]==num):
                return False
            
    return True


def solve():
    global grid
    for i in range(0,9):
        for j in range(0,9):
            if(grid[i][j]==0):
                for num in range(1, 10):
                    if(is_possible(num, i, j)):
                        grid[i][j]=num
                        solve()
                        grid[i][j]=0
                return
            
    print(np.matrix(grid))
    input("more solution")

solve()