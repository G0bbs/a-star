#
# A simple visual A star pathfinding program.

import pygame
import os
import math
import time

currentScreenWidth = 1100
currentScreenHeight = 900

GRID_HEIGHT = 20
GRID_WIDTH = 20

CELL_HEIGHT = 25
CELL_WIDTH = 25

# Styling
white = [255, 255, 255]
black = [0, 0, 0]

# Initialize our grid
grid = []
for i in range(1, GRID_HEIGHT):
    list = []
    for i in range(1, GRID_WIDTH):
        list.append(0)
    grid.append(list)
    
# PIN_Y = currentScreenHeight/2.5-(CELL_WIDTH*len(grid[0]))/2+1
PIN_Y = 50
PIN_X = currentScreenWidth/2-(CELL_WIDTH*len(grid[0]))/2+1

hasStart = False
hasEnd = False

# Pygame window initialization
pygame.init()
pygame.font.init()
font_30 = pygame.font.SysFont('Alef', 30)
font_20 = pygame.font.SysFont('Alef', 20)
screen = pygame.display.set_mode((currentScreenWidth, currentScreenHeight), pygame.RESIZABLE)
pygame.display.set_caption("A* Pathfinding")

def updateGrid(screen: pygame.display):
    for i in range(0, len(grid)-1):
        for j in range(0, len(grid)-1):
            box_rect = pygame.Rect(PIN_X+i*CELL_HEIGHT, PIN_Y+j*CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT)
            # for event in pygame.event.get():
            #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and box_rect.collidepoint(event.pos):
            #         grid[i][j] = 1
            #     elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and box_rect.collidepoint(event.pos):
            #         grid[i][j] = 0
            if grid[i][j] == 0:
                pygame.draw.rect(screen, (255, 255, 255), box_rect) # Draw solid rect center
            elif grid[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 255), box_rect) # Draw solid rect center
            elif grid[i][j] == 2:
                pygame.draw.rect(screen, (0, 150, 0), box_rect) # Draw solid rect center
            else:
                pygame.draw.rect(screen, (0, 255, 0), box_rect) # Draw solid rect center

            pygame.draw.rect(screen, (0, 0, 0), box_rect, 1) # Draw 1px rect outline

def setGridToValue(screen: pygame.display, value: int):
    if value == 0 or value == 1:
        hasEnd = False
        hasStart = False
    for i in range(0, len(grid)-1):
        for j in range(0, len(grid)-1):
            grid[i][j] = value
    if value == 0 or value == 1:
        return False, False


running: bool = True
while running:
    screen.fill((255, 240, 210))
    lastTime= time.time()
    screen.blit(font_30.render(str(time.time()-lastTime), True, (0, 0, 0)), (0, 0))
    screen.blit(font_20.render("Controls: Click to create barriers, right click to clear", True, (0, 0, 0)), (PIN_X, 0))
    screen.blit(font_20.render("          Press e to place start, q to place end", True, (0, 0, 0)), (PIN_X, 20))    
    updateGrid(screen)
    
    middleLineH = pygame.Rect(0, currentScreenHeight/2, currentScreenWidth, 3)
    pygame.draw.rect(screen, black, middleLineH)
    middleLineV = pygame.Rect(currentScreenWidth/2, 0, 3, currentScreenHeight)
    pygame.draw.rect(screen, black, middleLineV)
    
    clear_button = pygame.Rect(PIN_X, PIN_Y+CELL_HEIGHT*len(grid[0]), 30, 30)
    pygame.draw.rect(screen, (255, 0, 0), clear_button)
    
    keys = pygame.key.get_pressed()
    # Press escape to exit
    if keys[pygame.K_ESCAPE]:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:  # Left mouse button is being held down
            mouse_pos = pygame.mouse.get_pos()
            for i in range(0, len(grid)-1):
                for j in range(0, len(grid)-1):
                    box_rect = pygame.Rect(PIN_X+i*CELL_HEIGHT, PIN_Y+j*CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT)
                    if box_rect.collidepoint(mouse_pos):
                        grid[i][j] = 1
            if clear_button.collidepoint(mouse_pos):
                hasStart, hasEnd = setGridToValue(screen, 0)
        if mouse_pressed[2]:  # Left mouse button is being held down
            mouse_pos = pygame.mouse.get_pos()
            for i in range(0, len(grid)-1):
                for j in range(0, len(grid)-1):
                    box_rect = pygame.Rect(PIN_X+i*CELL_HEIGHT, PIN_Y+j*CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT)
                    if box_rect.collidepoint(mouse_pos):
                        if grid[i][j] == 2:
                            hasStart = False
                        elif grid[i][j] == 3:
                            hasEnd = False
                        grid[i][j] = 0
        if keys[pygame.K_q] and not hasStart:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(0, len(grid)-1):
                for j in range(0, len(grid)-1):
                    box_rect = pygame.Rect(PIN_X+i*CELL_HEIGHT, PIN_Y+j*CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT)
                    if box_rect.collidepoint(mouse_pos):
                        if grid[i][j] == 3:
                            hasEnd = False
                        grid[i][j] = 2
                        hasStart = True
        if keys[pygame.K_e] and not hasEnd:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(0, len(grid)-1):
                for j in range(0, len(grid)-1):
                    box_rect = pygame.Rect(PIN_X+i*CELL_HEIGHT, PIN_Y+j*CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT)
                    if box_rect.collidepoint(mouse_pos):
                        if grid[i][j] == 2:
                            hasStart = False
                        grid[i][j] = 3
                        hasEnd = True
    pygame.display.update()
    currentScreenWidth, currentScreenHeight = screen.get_size()
    PIN_X = currentScreenWidth/2-(CELL_WIDTH*len(grid[0]))/2+(CELL_WIDTH/2)
pygame.quit()