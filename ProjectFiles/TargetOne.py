import pygame
import random
from Plane import Plane
from ScoreBoard import ScoreBoard


class TargetOne:
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

        self.flyImage = (pygame.transform.scale(pygame.image.load("images/png/Bombs/Bomb_1_Idle (1).png"),
                                                (self.rectangle[2], self.rectangle[3])))

        self.explosionImageOrder = -1
        self.explosionImages = []
        for i in range(1, 10):
            self.explosionImages.append(
                pygame.transform.scale(pygame.image.load("images/png/Bombs/Bomb_1_Expo (" + str(i) + ").png"),
                                       (self.rectangle[2] * 4, self.rectangle[2] * 4)))
        self.exploded = False

    def draw(self, screen):
        if self.explosionImageOrder == -1:
            self.rectangle[0] = self.rectangle[0] - self.mx * 5
            # self.rectangle[1]=self.rectangle[1]-self.my*2
            # self.rectangle.centerx= self.rectangle.centerx-self.mx*2
            screen.blit(self.flyImage, [self.rectangle[0] - int(self.flyImage.get_width() / 2),
                                        self.rectangle[1] - int(self.flyImage.get_height() / 2)])
        else:
            self.explosionImageOrder = (self.explosionImageOrder + 1) % 9
            self.rectangle[0] = self.rectangle[0] - self.mx * 5
            self.rectangle[1] = self.rectangle[1] - self.my * 5
            self.rectangle.centerx = self.rectangle.centerx - self.mx * 2
            if self.explosionImageOrder == 8:
                return True
            screen.blit(self.explosionImages[self.explosionImageOrder],
                        [self.rectangle[0] - int(self.explosionImages[self.explosionImageOrder].get_width() / 2),
                         self.rectangle[1] - int(self.explosionImages[self.explosionImageOrder].get_height() / 2)])
            if self.explosionImageOrder == 8:
                self.explosionImageOrder = -1
        return False

    def hit(self):
        self.life -= 50
        if self.life <= 0:
            self.explode()
            Plane.ammo += 5
            ScoreBoard.score += 10

    def explode(self):
        self.life = 0
        self.exploded = True
        if self.explosionImageOrder < 0:
            self.explosionImageOrder = 0
