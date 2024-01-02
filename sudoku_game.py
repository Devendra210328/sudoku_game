import pygame
from sudoku_creater import generate_sudoku
from sudoku_solver import solve_sudoku


#Create a sudoku pazzle with a given difficulty level
sudoku_grid=generate_sudoku(3) # Difficulty levels: 1 to 5(easy to hard)
original_sudoku=[[sudoku_grid[i][j] for j in range(len(sudoku_grid[0]))] for i in range(0, len(sudoku_grid))]# it is for comperison
original_grid_element_color=(50, 50, 150) # original color of filled elements of sudoku_gird

# here ans_sudoku is  answer of sudoku_grid and it is work only for low level
ans_sudoku=[[sudoku_grid[i, j] for j in range(len(sudoku_grid[0]))] for i in range(0, len(sudoku_grid))]
solve_sudoku(ans_sudoku)
print(ans_sudoku)

Width=550
background_color=(251, 247, 245)
buffer=5

# insert function to fill empty space in sudoku window
def insert(win, position):
    myfont=pygame.font.SysFont('Comic Sans MS', 35)
    i, j=position[1],position[0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if(i<1 or j<1 or i>9 or j>9):
                    return
                if(original_sudoku[i-1][j-1]!=0):
                    return
                if(event.key==48):
                    sudoku_grid[i-1][j-1]=event.key-48
                    pygame.draw.rect(win, background_color, (position[0]*50+buffer, position[1]*50+buffer, 50-2*buffer, 50-2*buffer))
                    pygame.display.update()
                    return
                if(0<event.key-48<10):
                    pygame.draw.rect(win, background_color, (position[0]*50+buffer, position[1]*50+buffer, 50-2*buffer, 50-2*buffer))
                    # element_color=(0,0,0)
                    # if(ans_sudoku[i-1][j-1]==event.key-48):
                    #     element_color=(0, 250, 0)
                    value=myfont.render(str(event.key-48), True, (0,0,0))
                    win.blit(value,(position[0]*50+15, position[1]*50))
                    sudoku_grid[i-1][j-1]=event.key-48
                    pygame.display.update()
                    return
                return

def main():
    pygame.init()
    # make a window and set caption
    win= pygame.display.set_mode((Width, Width))
    pygame.display.set_caption("Sudoku")
    # fill window with color
    win.fill(background_color)
    myfont=pygame.font.SysFont('Comic Sans MS', 35)
    
    # make line for sudoku_gird 
    for i in range(0, 10):
        if(i%3==0):
            pygame.draw.line(win, (0, 0, 0), (50+50*i, 50), (50+50*i, 500), 4)
            pygame.draw.line(win, (0,0,0), (50, 50+50*i), (500, 50+50*i), 4)

        pygame.draw.line(win, (0, 0, 0), (50+50*i, 50), (50+50*i, 500), 2)
        pygame.draw.line(win, (0,0,0), (50, 50+50*i), (500, 50+50*i), 2)
    pygame.display.update()
    
    # fill sudoku window with proper value or sudoku_grid's element
    for i in range(0, len(sudoku_grid[0])):
        for j in range(0, len(sudoku_grid[0])):
            if(0<sudoku_grid[i][j]<10):
                value=myfont.render(str(sudoku_grid[i][j]), True, original_grid_element_color)
                win.blit(value,(50*(j+1)+15, 50*(i+1)))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if (event.type== pygame.MOUSEBUTTONUP) and (event.button)==1 :
                pos=pygame.mouse.get_pos()
                print(pos)
                insert(win, (pos[0]//50, pos[1]//50))
                # print(sudoku_grid)
                # print(sudoku_grid)
            if event.type==pygame.QUIT:
                pygame.quit()
                return
            
        pygame.display.flip()
            
main()
