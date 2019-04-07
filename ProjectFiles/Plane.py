import pygame
from Bullet import Bullet


class Plane:
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.mx = 0  # x haraket yönü
        self.my = 0  # x haraket yönü
        width = screen.get_width()
        height = screen.get_height()
        self.rectangle = pygame.rect.Rect(10, int(height / 2) - int(height / 5 / 2), int(width / 5), int(height / 5))
        self.flyImage = pygame.transform.scale(pygame.image.load("images/png/Plane/spaceship1.png"),
                                               (self.rectangle[2], self.rectangle[3]))
        # self.shootImageOrder = 0

        self.explodedImage = pygame.transform.scale(pygame.image.load("images/png/Plane/Dead (1).png"),
                                                    (self.rectangle[2], self.rectangle[3]))
        self.bullets = []
        self.exploded = False
        self.explodedEvent = pygame.event.Event(pygame.USEREVENT)

    def draw(self, screen):

        if self.exploded:
            screen.blit(self.explodedImage, self.rectangle)

            return True
        self.rectangle[0] = self.rectangle[0] + self.mx * 2
        self.rectangle[1] = self.rectangle[1] + self.my * 2
        self.rectangle.clamp_ip(screen.get_rect())  # plane objesini ekran karesi içinde tutar
        screen.blit(self.flyImage, self.rectangle)

        for bullet in self.bullets:
            bullet.draw(screen)
            # rectangle sınıfının contains fonsiyonu dörtgenin diğerinin içinde olup olmadığı bilgisini döndürür.
            # biz burada mermiler ekrandan çıkmışmı kontrolü yapacağız
            # ekrandan çıkan mermiler mermi listesinden silinmeli, aksi taktirde binlerce mermi sonsuzluğa kadar gider bu da boşa kaynak sarfıdır.
            if not screen.get_rect().contains(bullet.rectangle):
                self.bullets.remove(
                    bullet)  # foreach döngülerinde bunu yapmak iyi bir yöntem değildir, çünkü dizin bozulur. Bir çok programlama dilinde hata alırsınız.
                # ancak burada python kabul etti :D

    def fire(self, screen):

        nbullet = Bullet(self)
        nbullet.mx = 1
        self.bullets.append(nbullet)
        # her ateş edilişinde bir ateş edilme animasyonu devreye girmelidir
        # bu işlem farklı yollarla yapılabilir
        # burada yaprığımız normalde -1 olan shoot değerini 0  yapıyoruz ve nesnenin çizim fonksiyonunda bir if yapısıyla bu durumu kontrol ediyoruz.
        self.shootImageOrder = 0

    def explode(self):
        self.exploded = True
