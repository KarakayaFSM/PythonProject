import pygame
import math
import random
import sys
import os
from Chapter import Chapter
from Menu import Menu

pygame.init()

gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Gamemaker')

crashed = False

clock = pygame.time.Clock()
Chapter = Chapter(gameDisplay)
Chapter.start()
endEvent=pygame.event.Event(pygame.USEREVENT,{"EventName":"EndEvent"})
menu = Menu(gameDisplay.get_rect())
end=False

while not crashed:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Chapter.pgenerateTargetTimer.pause(True)
                crashed = menu.runMenu(gameDisplay)
                Chapter.pgenerateTargetTimer.pause(False)

            if event.key == pygame.K_UP:
                Chapter.Plane.my = -1
            if event.key == pygame.K_DOWN:
                Chapter.Plane.my = 1
            if event.key == pygame.K_LEFT:
                Chapter.Plane.mx = -1
            if event.key == pygame.K_RIGHT:
                Chapter.Plane.mx = 1
            if event.key == pygame.K_SPACE:
                Chapter.Plane.fire(gameDisplay)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                Chapter.Plane.my = 0
            if event.key == pygame.K_DOWN:
                Chapter.Plane.my = 0
            if event.key == pygame.K_LEFT:
                Chapter.Plane.mx = 0
            if event.key == pygame.K_RIGHT:
                Chapter.Plane.mx = 0
        # event karşılaştırmalarında eşitlik koşulu çalışır
        # eventlar aynı olmalı özellikleriyle birlikte
        elif event == Chapter.finishEvent:
            print(event)
            end = True

        elif event == Chapter.Plane.explodedEvent:
            print(event)

    if not end:
        Chapter.draw(gameDisplay)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()






















