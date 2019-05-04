import pygame
from TargetOne import TargetOne
from TargetTwo import TargetTwo
from TargetThree import TargetThree
from Plane import Plane
from pTimer import pTimer
import random


class Chapter:
    def __init__(self, screen):
        self.name = "Haydi Başla"
        self.Plane = Plane(screen)
        self.targets = []
        self.backGroundImage = pygame.transform.scale(pygame.image.load("images/png/BG.png"),
                                                      (screen.get_width(), screen.get_height()))
        self.backGroundImageX = 0
        self.backGroundImageY = 0
        self.screen = screen

        self.pgenerateTargetTimer = pTimer(2, self.generateTarget, screen)
        self.finishEvent = pygame.event.Event(pygame.USEREVENT, {"EventName": "FinishEvent"})
        self.Targets = (TargetOne,TargetTwo,TargetThree)

    def start(self):
        self.pgenerateTargetTimer.start()

    def finish(self):
        self.pgenerateTargetTimer.stop()
        pygame.event.post(self.finishEvent)

    def generateTarget(self, arguments):
        newTarget = self.Targets[random.randint(0,2)](arguments[0])  # restart error 2nd layer
        self.targets.append(newTarget)

    def drawBackGround(self, screen):
        screen.blit(self.backGroundImage, (self.backGroundImageX, 0))
        self.backGroundImageX = self.backGroundImageX - 1
        screen.blit(self.backGroundImage, (screen.get_width() + self.backGroundImageX, 0))
        # resim dönüşünde x değerini sıfırlıyoruz
        if screen.get_width() == -self.backGroundImageX:
            self.backGroundImageX = 0

    def drawPlane(self, screen):
        self.Plane.draw(screen)

    def drawTargets(self, screen):
        for target in self.targets:
            exploded = target.draw(screen) # TARGET DRAW BOOLEAN BİR DEĞER DÖNDÜRMELİ
            if exploded:
                self.targets.remove(target)
                pygame.event.post(TargetOne.ExplodedEvent)
                if self.Plane.exploded:
                    pygame.event.post(self.Plane.explodedEvent)
                    self.finish()
            else:
                if target.rectangle.colliderect(self.Plane.rectangle):
                    if not target.exploded:
                        target.explode()
                        self.Plane.explode()

                else:
                    for bullet in self.Plane.bullets:
                        # eğer eşleşme varsa
                        if target.rectangle.colliderect(bullet.rectangle):
                            # target hit almış demektir.
                            target.hit()
                            # mermi kaybolmalı
                            self.Plane.bullets.remove(bullet)

    def draw(self, screen):
        self.drawBackGround(screen)
        self.drawPlane(screen)
        self.drawTargets(screen)
