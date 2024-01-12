import pygame
import time

pygame.display.init()
screenWidth = 700
screenHeight = 700

playWidth = screenWidth * 0.8
playHeight = screenHeight * 0.7

areas = [
    [(screenWidth * 0.1, screenHeight * 0.2), (playWidth * 1/3 + screenWidth * 0.1, playHeight * 1/3 + screenHeight * 0.2)],
    [(playWidth * 1/3 + screenWidth * 0.1, screenHeight * 0.2), (playWidth * 2/3 + screenWidth * 0.1, playHeight * 1/3 + screenHeight * 0.2)],
    [(playWidth * 2/3 + screenWidth * 0.1, screenHeight * 0.2), (screenWidth * 0.9, playHeight * 1/3 + screenHeight * 0.2)],
    [(screenWidth * 0.1, playHeight * 1/3 + screenHeight * 0.2), (playWidth * 1/3 + screenWidth * 0.1, playHeight * 2/3 + screenHeight * 0.2)],
    [(playWidth * 1/3 + screenWidth * 0.1, playHeight * 1/3 + screenHeight * 0.2), (playWidth * 2/3 + screenWidth * 0.1, playHeight * 2/3 + screenHeight * 0.2)],
    [(playWidth * 2/3 + screenWidth * 0.1, playHeight * 1/3 + screenHeight * 0.2), (screenWidth * 0.9, playHeight * 2/3 + screenHeight * 0.2)],
    [(screenWidth * 0.1, playHeight * 2/3 + screenHeight * 0.2), (playWidth * 1/3 + screenWidth * 0.1, screenHeight * 0.9)],
    [(playWidth * 1/3 + screenWidth * 0.1, playHeight * 2/3 + screenHeight * 0.2), (playWidth * 2/3 + screenWidth * 0.1, screenHeight * 0.9)],
    [(playWidth * 2/3 + screenWidth * 0.1, playHeight * 2/3 + screenHeight * 0.2), (screenWidth * 0.9, screenHeight * 0.9)]
]

tiles = {0:None, 1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None}

turn = True

screen = pygame.display.set_mode([screenWidth, screenHeight])

def graphics():
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(screenWidth * 0.1, screenHeight * 0.2, playWidth, playHeight))

    pygame.draw.line(screen, (0,0,0), (playWidth * 1/3 + screenWidth * 0.1, screenHeight * 0.2), (playWidth * 1/3 + screenWidth * 0.1, screenHeight * 0.9), width=5)
    pygame.draw.line(screen, (0,0,0), (playWidth * 2/3 + screenWidth * 0.1, screenHeight * 0.2), (playWidth * 2/3 + screenWidth * 0.1, screenHeight * 0.9), width=5)

    pygame.draw.line(screen, (0,0,0), (screenWidth * 0.1, playHeight * 1/3 + screenHeight * 0.2), (screenWidth * 0.9, playHeight * 1/3 + screenHeight * 0.2), width=5)
    pygame.draw.line(screen, (0,0,0), (screenWidth * 0.1, playHeight * 2/3 + screenHeight * 0.2), (screenWidth * 0.9, playHeight * 2/3 + screenHeight * 0.2), width=5)

    for x in tiles:
        if tiles[x] != None:
            if tiles[x][0] == "circle":
                pygame.draw.circle(tiles[x][1], tiles[x][2], tiles[x][3], tiles[x][4], width=3)
            else:
                pygame.draw.line(tiles[x][1][0], tiles[x][1][1], tiles[x][1][2], tiles[x][1][3], width=3)
                pygame.draw.line(tiles[x][2][0], tiles[x][2][1], tiles[x][2][2], tiles[x][2][3], width=3)
        
    # DEBUG AREAS
    #for x in areas:
    #    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x[0][0], x[0][1], x[1][0] - x[0][0], x[1][1] - x[0][1]))

def circle(index):
    width = areas[index][0][0] + (areas[index][1][0] - areas[index][0][0])/2
    height = areas[index][0][1] + (areas[index][1][1] - areas[index][0][1])/2
    radius = (areas[index][1][1] - areas[index][0][1])/2 - 10
    return ["circle", screen, (0,0,0), (width, height), radius]

def cross(index):
    pygame.draw.line(screen, (0,0,0), (areas[index][0][0], areas[index][0][1]), (areas[index][1][0], areas[index][1][1]))
    pygame.draw.line(screen, (0,0,0), (areas[index][0][0], areas[index][1][1]), (areas[index][1][0], areas[index][0][1]))
    return [
        "banana",
        [screen, (0,0,0), (areas[index][0][0]+10, areas[index][0][1]+10), (areas[index][1][0]-10, areas[index][1][1]-10)],
        [screen, (0,0,0), (areas[index][0][0]+10, areas[index][1][1]-10), (areas[index][1][0]-10, areas[index][0][1]+10)]
    ]

while True:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.display.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for num in range(len(areas)):
                if event.pos[0] > areas[num][0][0] and event.pos[0] < areas[num][1][0] and event.pos[1] > areas[num][0][1] and event.pos[1] < areas[num][1][1]:
                    if turn and tiles[num] == None:
                        tiles[num] = cross(num)
                        turn = False
                    elif not turn and tiles[num] == None:
                        tiles[num] = circle(num)
                        turn = True
    
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(0,0,screenWidth,screenHeight))

    graphics()
    
    pygame.display.flip()

    time.sleep(0.5)
