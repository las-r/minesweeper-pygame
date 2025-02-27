"""
Written by las_r
"""

import pygame
import random

# initialize
pygame.init()
font = pygame.font.Font(None, 64)

# settings
BWIDTH, BHEIGHT = 9, 9 # board size
TILESIZE = 64  # tile size
WIDTH, HEIGHT = BWIDTH * TILESIZE, BHEIGHT * TILESIZE # window size
MINES = 10  # mine amount
WINTEXT = "You win!" # win text
LOSETEXT = "You lose!" # lose text

# colors
BG = (71, 77, 89)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# variables
playing = True
win = False
firstClick = True
flagAmnt = 0

# board
board = [[0 for _ in range(BHEIGHT)] for _ in range(BWIDTH)] # mine board
revealed = [[False for _ in range(BHEIGHT)] for _ in range(BWIDTH)] # revealed board
flags = [[False for _ in range(BHEIGHT)] for _ in range(BWIDTH)] # flag board

# load images
ms1 = pygame.transform.scale(pygame.image.load("sprites/ms1.png"), (TILESIZE, TILESIZE))
ms2 = pygame.transform.scale(pygame.image.load("sprites/ms2.png"), (TILESIZE, TILESIZE))
ms3 = pygame.transform.scale(pygame.image.load("sprites/ms3.png"), (TILESIZE, TILESIZE))
ms4 = pygame.transform.scale(pygame.image.load("sprites/ms4.png"), (TILESIZE, TILESIZE))
ms5 = pygame.transform.scale(pygame.image.load("sprites/ms5.png"), (TILESIZE, TILESIZE))
ms6 = pygame.transform.scale(pygame.image.load("sprites/ms6.png"), (TILESIZE, TILESIZE))
ms7 = pygame.transform.scale(pygame.image.load("sprites/ms7.png"), (TILESIZE, TILESIZE))
ms8 = pygame.transform.scale(pygame.image.load("sprites/ms8.png"), (TILESIZE, TILESIZE))
msb = pygame.transform.scale(pygame.image.load("sprites/msb.png"), (TILESIZE, TILESIZE))
msd = pygame.transform.scale(pygame.image.load("sprites/msd.png"), (TILESIZE, TILESIZE))
msf = pygame.transform.scale(pygame.image.load("sprites/msf.png"), (TILESIZE, TILESIZE))
msm = pygame.transform.scale(pygame.image.load("sprites/msm.png"), (TILESIZE, TILESIZE))

# load sounds
blip1 = pygame.mixer.Sound("sounds/blip1.wav")
blip2 = pygame.mixer.Sound("sounds/blip2.wav")
coin1 = pygame.mixer.Sound("sounds/coin1.wav")
coin2 = pygame.mixer.Sound("sounds/coin2.wav")
exp1 = pygame.mixer.Sound("sounds/exp1.wav")
exp2 = pygame.mixer.Sound("sounds/exp2.wav")
winSfx = pygame.mixer.Sound("sounds/win.wav")
blip1.set_volume(0.2)
blip2.set_volume(0.2)
coin1.set_volume(0.2)
coin2.set_volume(0.2)
exp1.set_volume(0.2)
exp2.set_volume(0.2)
winSfx.set_volume(0.2)

# functions
def generateBoard(nw, nh):
    global board

    for _ in range(MINES):
        w = random.randint(0, BWIDTH - 1)
        h = random.randint(0, BHEIGHT - 1)
        if nw != None and nh != None:
            while board[w][h] == 1 or (w == nw and h == nh):
                w = random.randint(0, BWIDTH - 1)
                h = random.randint(0, BHEIGHT - 1)
        else:
            while board[w][h] == 1:
                w = random.randint(0, BWIDTH - 1)
                h = random.randint(0, BHEIGHT - 1)
        board[w][h] = 1

def getTile(x, y):
    if board[x][y] == 1:
        return msm  # mine tile (show a mine)

    # count surrounding mines
    mine_count = 0
    for dx in range(-1, 2):  # x direction: -1, 0, 1
        for dy in range(-1, 2):  # y direction: -1, 0, 1
            nx, ny = x + dx, y + dy
            if 0 <= nx < BWIDTH and 0 <= ny < BHEIGHT and board[nx][ny] == 1:
                mine_count += 1

    # return the corresponding tile based on the mine count
    if mine_count == 1:
        return ms1
    elif mine_count == 2:
        return ms2
    elif mine_count == 3:
        return ms3
    elif mine_count == 4:
        return ms4
    elif mine_count == 5:
        return ms5
    elif mine_count == 6:
        return ms6
    elif mine_count == 7:
        return ms7
    elif mine_count == 8:
        return ms8
    else:
        return msb

def click(w, h):
    global playing
    
    if not flags[w][h]:
        if board[w][h] == 1:
            playing = False
            pygame.mixer.Sound.play(random.choice([exp1, exp2]))

            # reveal all mines
            for w in range(BWIDTH):
                for h in range(BHEIGHT):
                    if board[w][h] == 1:
                        if flags[w][h]:
                            flags[w][h] = False
                        revealed[w][h] = True
        else:
            if not revealed[w][h]:
                pygame.mixer.Sound.play(random.choice([blip1, blip2]))
            
            floodFill(w, h)
            checkWin()
            
def flag(w, h):    
    global flagAmnt
    
    if not revealed[w][h] and not firstClick:
        if not flags[w][h] and flagAmnt < MINES:
            pygame.mixer.Sound.play(random.choice([coin1, coin2]))
            flags[w][h] = True
            flagAmnt += 1
        elif flags[w][h]:
            pygame.mixer.Sound.play(random.choice([coin1, coin2]))
            flags[w][h] = False
            flagAmnt -= 1    
        
def floodFill(w, h):
    if revealed[w][h]:
        return
    revealed[w][h] = True
    
    if getTile(w, h) == msb:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = w + dx, h + dy
                if 0 <= nx < BWIDTH and 0 <= ny < BHEIGHT:
                    floodFill(nx, ny)

def drawBoard():
    for w in range(BWIDTH):
        for h in range(BHEIGHT):
            if flags[w][h]:
                screen.blit(msf, (w * TILESIZE, h * TILESIZE))  # draw flag
            elif revealed[w][h]:
                screen.blit(getTile(w, h), (w * TILESIZE, h * TILESIZE))
            else:
                screen.blit(msd, (w * TILESIZE, h * TILESIZE))   
        
def checkWin():
    global playing
    global win
    
    for w in range(BWIDTH):
        for h in range(BHEIGHT):
            if board[w][h] == 0 and not revealed[w][h]:
                return
    playing = False
    win = True
    
    pygame.mixer.Sound.play(winSfx)

# display setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# main loop
running = True
while running:
    screen.fill(BG)

    # draw the board
    drawBoard()

    # event handling
    for event in pygame.event.get():
        # quit event
        if event.type == pygame.QUIT:
            running = False

        # mouse click event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            w = mouseX // TILESIZE
            h = mouseY // TILESIZE

            if event.button == 1 and playing:  # left mb
                if firstClick:
                    generateBoard(w, h)
                    firstClick = False
                click(w, h)
            elif event.button == 3 and playing:  # right mb
                flag(w, h)
                
        # key press event
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: # r key
                # reset
                board = [[0 for _ in range(BHEIGHT)] for _ in range(BWIDTH)]
                revealed = [[False for _ in range(BHEIGHT)] for _ in range(BWIDTH)]
                flags = [[False for _ in range(BHEIGHT)] for _ in range(BWIDTH)]
                playing = True
                win = False
                firstClick = True
                flagAmnt = 0

    # win lose text
    if not playing:
        if win:
            text = font.render(WINTEXT, True, GREEN)
            screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        else:
            text = font.render(LOSETEXT, True, RED)
            screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    # update the display
    pygame.display.flip()

# quit pygame
pygame.quit()