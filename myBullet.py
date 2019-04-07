import pygame
import math


class myBullet:
    def __init__(self, plane):
        self.x = 0
        self.y = 0
        self.mx = 0  # x haraket yönü
        self.my = 0  # x haraket yönü
        self.change_x = 0
        self.change_y = 0
        # self.original_image = None
        self.rectangle = pygame.rect.Rect(plane.rectangle[0] + int(plane.rectangle[2] / 12 * 8),
                                          plane.rectangle[1] + int(plane.rectangle[3] / 12 * 8),
                                          int(plane.rectangle[2] / 5), int(plane.rectangle[3] / 5))

        self.image = pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (1).png"),
                                                      (self.rectangle[2], self.rectangle[3]))

    def draw_aimed(self, screen):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        xdiff = mouse_x - self.x
        ydiff = mouse_y - self.y
        angle = math.atan2(ydiff, xdiff)
        self.change_x = math.cos(angle) * self.mx * 3
        self.change_y = math.sin(angle) * self.my * 3
        self.rectangle[0] += math.cos(angle) * self.mx * 3
        self.rectangle[1] += math.sin(angle) * self.my * 3
        screen.blit(self.image, self.rectangle)

    # def draw(self, screen):
    #     self.y += self.change_y
    #     self.x += self.change_x
    #     self.rectangle.y = self.y
    #     self.rectangle.x = self.x
    #
    #     self.rectangle[0] += math.cos(self.angle) * self.mx * 3
    #     self.rectangle[1] += math.sin(self.angle) * self.my * 3
    #     # self.rectange.clamp_ip(screen.get_rect())
    #     # mermi objesini ekran karesi içinden çıkarsa silinir
    #     # bunu planeden kontrol edeceğiz.
    #     screen.blit(self.image, self.rectangle)


def rotate(self):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
    pygame.transform.rotate(self.images[self.imageOrder], int(angle))
