import pygame
from Menu import Menu
from ScoreBoard import ScoreBoard
from threading import Thread
from gameOverMenu import gameOverMenu
from Chapter import Chapter

pygame.init()
gameDisplay_width, gameDisplay_height = 800, 600
gameDisplay = pygame.display.set_mode((gameDisplay_width, gameDisplay_height))
pygame.display.set_caption('Gamemaker')
crashed = False

clock = pygame.time.Clock()
Chapter = Chapter(gameDisplay)
Chapter.start()
endEvent = pygame.event.Event(pygame.USEREVENT, {"EventName": "EndEvent"})
menu = Menu(gameDisplay.get_rect())
gameOverMenu = gameOverMenu(gameDisplay.get_rect())
end = False
ScoreBoard.init_ScoreBoard()
ScoreBoard.set_Score()
TimerThread = Thread(target=ScoreBoard.timer_func, args=(gameDisplay,))
TimerThread.setDaemon(True)
TimerThread.start()

while not crashed:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True
            TimerThread.join(0.1)
        elif event == ScoreBoard.EndOfTimeEvent or end:
            TimerThread.join(0.1)
            Chapter.pgenerateTargetTimer.pause(True)
            crashed = gameOverMenu.runGameOverMenu(gameDisplay)
            Chapter.pgenerateTargetTimer.pause(False)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Chapter.pgenerateTargetTimer.pause(True)
                crashed = menu.runMenu(gameDisplay)
                if event == Menu.Restart_Event:
                    ScoreBoard.reset()
                Chapter.pgenerateTargetTimer.pause(False)

            if event.key == pygame.K_w:
                Chapter.Plane.my = -1
            if event.key == pygame.K_s:
                Chapter.Plane.my = 1
            if event.key == pygame.K_a:
                Chapter.Plane.mx = -1
            if event.key == pygame.K_d:
                Chapter.Plane.mx = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                Chapter.Plane.my = 0
            if event.key == pygame.K_s:
                Chapter.Plane.my = 0
            if event.key == pygame.K_a:
                Chapter.Plane.mx = 0
            if event.key == pygame.K_d:
                Chapter.Plane.mx = 0
        # event karşılaştırmalarında eşitlik koşulu çalışır
        # eventlar aynı olmalı özellikleriyle birlikte
        if event.type == pygame.MOUSEMOTION:
            Chapter.Plane.rotate()

        if pygame.mouse.get_pressed()[0] == 1:
            Chapter.Plane.fire()
        elif event == Chapter.finishEvent:
            print(event)
            end = True
        # elif event == TargetOne.ExplodedEvent:
        #    ScoreBoard.set_Score(10)
        elif event == Chapter.Plane.explodedEvent:
            print(event)

    if not end:
        Chapter.draw(gameDisplay)

    ScoreBoard.draw(gameDisplay)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
