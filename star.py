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

#Pygame window initialization
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Alef', 30)
screen = pygame.display.set_mode((currentScreenWidth, currentScreenHeight), pygame.RESIZABLE)
pygame.display.set_caption("Fancy Boat Display")

# Initialize our grid
grid = []
for i in range(1, GRID_HEIGHT):
    list = []
    for i in range(1, GRID_WIDTH):
        list.append(0)
    grid.append(list)

def updateGrid(screen: pygame.display):
    PIN_Y = currentScreenHeight/8
    PIN_X = currentScreenWidth/2
    CELL_HEIGHT = 30
    CELL_WIDTH = 30
    for i in range(0, len(grid)-1):
        for j in range(0, len(grid)-1):
            box_rect = pygame.Rect(PIN_X+i*CELL_HEIGHT, PIN_Y+j*CELL_WIDTH, 30, 30)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and box_rect.collidepoint(event.pos):
                    grid[i][j] = 1
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and box_rect.collidepoint(event.pos):
                    grid[i][j] = 0
            if grid[i][j] == 0:
                pygame.draw.rect(screen, (255, 255, 255), box_rect) # Draw solid rect center
            elif grid[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 255), box_rect) # Draw solid rect center
            pygame.draw.rect(screen, (0, 0, 0), box_rect, 1) # Draw 1px rect outline

running: bool = True
while running:
    screen.fill((255, 240, 210))
    screen.blit(my_font.render(str(time.time()), True, (0, 0, 0)), (0, 0))  
    updateGrid(screen)
    keys = pygame.key.get_pressed()
    # Press escape to exit
    if keys[pygame.K_ESCAPE]:
        running = False
    for event in pygame.event.get(): # Accept any quit events
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    currentScreenHeight, currentScreenWidth = screen.get_size()
pygame.quit()