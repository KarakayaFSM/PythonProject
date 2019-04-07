import pygame
import sys
import math
import random

class Bullet:
    def __init__(self,plane):
        self.x=0
        self.y=0
        self.mx=0 #x haraket yönü
        self.my=0 #x haraket yönü
        self.original_image = None
        self.rectangle=pygame.rect.Rect(plane.rectangle[0] + int(plane.rectangle[2]/12*8), plane.rectangle[1] +  int(plane.rectangle[3]/12*8), int(plane.rectangle[2] / 5), int(plane.rectangle[3] / 5))
        self.imageOrder=0
        self.images=[pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (1).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (2).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (3).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (4).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (5).png"),(self.rectangle[2],self.rectangle[3]))]
    def draw(self,screen):
        self.imageOrder=(self.imageOrder+1)%5
        self.rectangle[0]=self.rectangle[0]+self.mx*3
        self.rectangle[1]=self.rectangle[1]+self.my*3
        #self.rectange.clamp_ip(screen.get_rect())
        ##mermi objesini ekran karesi içinden çıkarsa silinir
        ##bunu planeden kontrol edeceğiz.
        self.original_image = self.images[self.imageOrder]
        screen.blit(self.original_image, self.rectangle)

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.images[self.imageOrder] = pygame.transform.rotate(self.original_image, int(angle))