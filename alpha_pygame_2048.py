import pygame, sys, random, tf8L
from pygame.locals import *
DISPLAYSURF = pygame.display.set_mode((300, 500))
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN_L  = (180, 255, 180)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
TILECOLOR = (134, 134, 194) #8686c2
pygame.display.set_caption('2048')
BOXSIZE = 50
FPS = 60
gap = 1
top = pygame.image.load("tf8_top.png")
buttom = pygame.image.load('tf8_buttom.png')

def main():
    mainboard = tf8L.genBoard()
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    while True:
        DISPLAYSURF.fill(NAVYBLUE)
        DISPLAYSURF.blit(top, (0, 0))
        DISPLAYSURF.blit(buttom, (0, 427))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_w:
                    tf8L.shift_up(mainboard)
                    tf8L.drop_two(mainboard)
                elif event.key == K_s:
                    tf8L.shift_down(mainboard)
                    tf8L.drop_two(mainboard)
                elif event.key == K_a:
                    tf8L.shift_left(mainboard)
                    tf8L.drop_two(mainboard)
                elif event.key == K_d:
                    tf8L.shift_right(mainboard)
                    tf8L.drop_two(mainboard)
        pygame.time.wait(100)            
        drawBoard(mainboard)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawBoard(Board):

    fontObj = pygame.font.SysFont('Montserrat-Black.ttf', 32)  #defualt
    r_Board = clone_matrix(Board)
    tf8L.rotate_90(r_Board) 
    for y in range(0,4): #col
        for x in range(0,4): #rows
            x_c = (x+1)*(BOXSIZE+gap)
            y_c = 125+((y+1)*(BOXSIZE+gap))
            pygame.draw.rect(DISPLAYSURF, TILECOLOR, (x_c, y_c, BOXSIZE, BOXSIZE))
            if r_Board[x][y] != 0: 
                textSurfaceObj = fontObj.render(str(r_Board[x][y]), True, WHITE , TILECOLOR)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (x_c+int((BOXSIZE/2)), y_c+int((BOXSIZE/2)))
                DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    score = tf8L.get_score()
    textScore = fontObj.render(str(score), True, WHITE, NAVYBLUE)
    textScoreRect = textScore.get_rect()
    textScoreRect.center = (120, 458)
    DISPLAYSURF.blit(textScore, textScoreRect)

    #tf8L.print_board(Board) // debug

def clone_matrix(m):
    k = []
    for row in range(len(m)):
        k.append(m[row][:])
    return k

if __name__ == "__main__":
    main()