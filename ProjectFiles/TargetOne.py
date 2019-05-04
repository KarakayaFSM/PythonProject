import pygame
import random
from Plane import Plane

class TargetOne:
    ExplodedEvent = pygame.event.Event(pygame.USEREVENT, {"EventName": "ExplodedEvent"})

    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.mx = 1  # x haraket yönü
        self.my = 0  # y haraket yönü
        self.life = 100
        width = screen.get_width()  # restart error 1.layer
        height = screen.get_height()
        self.y = random.randint(10, height - int(height / 5))
        self.rectangle = pygame.rect.Rect(width + int(width / 20) / 2, self.y + int(height / 10) / 2, int(width / 20),
                                          int(height / 10))

        self.flyImage = pygame.transform.scale(pygame.image.load("images/png/Bombs/Bomb_1_Idle (3).png"),
                                               (self.rectangle[2], self.rectangle[3]))

        self.explosionImage = pygame.transform.scale(
            pygame.image.load("images/png/Bombs/Bomb_1_Expo (3).png"),
            (self.rectangle[2] * 4, self.rectangle[2] * 4))
        self.exploded = False

    def draw(self, screen):
        # BU FONKSİYON BOOLEAN BİR DEĞER DÖNDÜRMELİ
        self.rectangle[0] = self.rectangle[0] - self.mx * 2
        # self.rectangle[1]=self.rectangle[1]-self.my*2
        # self.rectangle.centerx= self.rectangle.centerx-self.mx*2
        screen.blit(self.flyImage,
                    [self.rectangle[0] - int(self.flyImage.get_width() / 2),
                     self.rectangle[1] - int(self.flyImage.get_height() / 2)])
        self.rectangle[0] = self.rectangle[0] - self.mx
        self.rectangle[1] = self.rectangle[1] - self.my
        self.rectangle.centerx = self.rectangle.centerx - self.mx

        screen.blit(self.explosionImage,
                    [self.rectangle[0] - int(self.explosionImage.get_width() / 2),
                     self.rectangle[1] - int(self.explosionImage.get_height() / 2)])

    def hit(self):
        self.life -= 50
        print("1 got hit life:", self.life)
        if self.life <= 0:
            self.explode()

    def explode(self):
        print("1 exploded")
        self.life = 0
        self.exploded = True
        Plane.ammo+=7
