# visualisation of boundary fill algorithm

import pygame
import sys

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 0, 255)

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
blockSize = 20

LEFT = 1
RIGHT = 3

rect_array = [[ None for _ in range(WINDOW_HEIGHT) ] for _ in range(WINDOW_WIDTH) ]
color = [[ BLACK for _ in range(WINDOW_HEIGHT) ] for _ in range(WINDOW_WIDTH) ]

# returns the index of rectangle with given coordinates
def getIndex(posX,posY):
    y = (posY//blockSize)
    x = (posX//blockSize)
    return (x,y)

# boundary fill algorithm
def fill_8(posX,posY):

    if( color[posX][posY] == BLACK):
        color[posX][posY] = GREEN
        drawGrid()
        pygame.display.update()
        pygame.time.wait(1000) # wait for 1 second, for better visualisation

    else:
        return
    fill_8(posX+1,posY)
    fill_8(posX,posY+1)
    fill_8(posX-1,posY)
    fill_8(posX,posY-1)
    fill_8(posX-1,posY-1)
    fill_8(posX-1,posY+1)
    fill_8(posX+1,posY-1)
    fill_8(posX+1,posY+1)

def drawGrid():
    i = 0
    for x in range(0, WINDOW_HEIGHT,blockSize):
        j = 0
        for y in range(0, WINDOW_WIDTH,blockSize):
            rect_array[i][j] = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, color[i][j], rect_array[i][j],1)
            j = j+1
        i = i+1

def help():
    print("""
    This program helps in visualisation of boundary fill algorithm (using 8 connected pixels)
    left click  --> select each pixel of the boundary
    right click --> select the pixel to start the boundary fill algo (a pixel inside boundary)
    RED --> boundary
    GREEN --> filled pixels
    """)

def main():
    global SCREEN
    help()
    pygame.time.wait(1000) # wait for 1 second, so the user will see the help text
    pygame.init()
    pygame.display.set_caption('Boundary fill Algorithm')
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    running = True
    while running:
        
        drawGrid()
        for event in pygame.event.get():
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                posX,posY = pygame.mouse.get_pos()
                indX,indY = getIndex(posX,posY)
                # print(indX,indY)
                color[indX][indY] = RED

            if event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
                posX,posY = pygame.mouse.get_pos()
                indX,indY = getIndex(posX,posY)
                fill_8(indX,indY)
                print("filling done")

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


main()
