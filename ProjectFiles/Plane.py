import pygame
import math
from myBullet import myBullet


class Plane:
    def __init__(self, screen):
        self.x = 150
        self.y = 150
        self.mx = 0  # x haraket yönü
        self.my = 0  # y haraket yönü
        width = screen.get_width()
        height = screen.get_height()
        self.rectangle = pygame.rect.Rect(10, int(height / 2) - int(height / 5 / 2), int(width / 5), int(height / 5))
        self.originalImage = self.flyImage = pygame.transform.scale(pygame.image.load("images/png/Plane/spaceship1.png"),
                                               (self.rectangle[2]-30, self.rectangle[3]-30))

        self.explodedImage = pygame.transform.scale(pygame.image.load("images/png/Plane/Dead (1).png"),
                                                    (self.rectangle[2], self.rectangle[3]))
        self.bullets = []
        self.exploded = False
        self.explodedEvent = pygame.event.Event(pygame.USEREVENT,{"EventName":"ExplodedEvent"})

    def draw(self, screen):

        if self.exploded:
            screen.blit(self.explodedImage, self.rectangle)
            return True

        self.rectangle[0] = self.rectangle[0] + self.mx * 5
        self.rectangle[1] = self.rectangle[1] + self.my * 5
        self.rectangle.clamp_ip(screen.get_rect())  # plane objesini ekran karesi içinde tutar
        screen.blit(self.flyImage, self.rectangle)

        for bullet in self.bullets:
            bullet.draw_aimed(screen)
            # rectangle sınıfının contains fonsiyonu dörtgenin diğerinin içinde olup olmadığı bilgisini döndürür.
            # biz burada mermiler ekrandan çıkmışmı kontrolü yapacağız
            # ekrandan çıkan mermiler mermi listesinden silinmeli, aksi taktirde binlerce mermi sonsuzluğa kadar gider bu da boşa kaynak sarfıdır.
            if not screen.get_rect().contains(bullet.rectangle):
                self.bullets.remove(bullet)  # foreach döngülerinde bunu yapmak iyi bir yöntem değildir, çünkü dizin bozulur. Bir çok programlama dilinde hata alırsınız.
                # ancak burada python kabul etti :D

    def fire(self):
        nbullet = myBullet(self)
        nbullet.mx = 1
        self.bullets.append(nbullet)

    def explode(self):
        self.exploded = True

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        center = self.flyImage.get_rect().center
        self.flyImage = pygame.transform.rotate(self.originalImage, int(angle))
        self.rectangle.move(center[0],center[1])