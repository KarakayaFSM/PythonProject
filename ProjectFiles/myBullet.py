import pygame
import math

from pygame import Vector2


class myBullet:
    def __init__(self, plane, mouse_pos):
        self.x = plane.rectangle[0]
        self.y = plane.rectangle[1]

        self.pos = Vector2(x=self.x, y=self.y)
        self.mouse_pos = mouse_pos
        self.rel_x, self.rel_y = mouse_pos[0] - self.x, mouse_pos[1] - self.y
        self.angle = (180 / math.pi) * -math.atan2(self.rel_y, self.rel_x)
        self.mx = 1 - (math.cos(self.angle) <= 0)
        self.my = 1 - (math.sin(self.angle) <= 0)

        self.rectangle = pygame.rect.Rect(plane.rectangle[0] + int(plane.rectangle[2] / 12 * 8),
                                          plane.rectangle[1] + int(plane.rectangle[3] / 12 * 8),
                                          int(plane.rectangle[2] / 5), int(plane.rectangle[3] / 5))

        self.image = pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (1).png"),
                                            (self.rectangle[2], self.rectangle[3]))

    def dene(self):
        distance = math.sqrt((self.rel_x ** 2 + self.rel_y ** 2))
        if distance > 0:
            coefficient = 100 / distance  # 100 -> Normalizer
            self.rel_x *= coefficient
            self.rel_y *= coefficient

    def from_video(self, screen):
        # https://www.youtube.com/watch?v=YfWh0WtwuWE
        # r, phi = (self.mouse_pos - self.pole).as_polar()
        screen.blit(self.image, self.rectangle)

    def draw_aimed(self, screen):
        x = math.cos(self.angle)
        y = math.sin(self.angle)
        self.rectangle[0] += math.cos(self.angle) + self.mx
        self.rectangle[1] += math.sin(self.angle) + self.my

        screen.blit(self.image, self.rectangle)

    def rotate(self, screen):
        # center = self.image.get_rect().center
        # self.rectangle.move(center[0], center[1])
        rotated_image = pygame.transform.rotate(self.image, float(self.angle))
        self.rectangle[0] += math.cos(float(self.angle)) + self.mx
        self.rectangle[1] += math.sin(float(self.angle)) + self.my
        screen.blit(rotated_image, self.rectangle)


    # 0 1 2 3 -> (0,1) (0,2) (0,3)
    #            (1,0) (1,2) (1,3)
    #
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

    def rotateBullet(self, screen):
        aci = math.degrees(math.atan2(self.rel_y, self.rel_x))
        self.rectangle[0] += math.cos(aci) * 5  # + self.mx
        self.rectangle[0] += math.sin(aci) * 5  # + self.my
        screen.blit(self.image, self.rectangle)
        # mouse_x, mouse_y = pygame.mouse.get_pos()
        # rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        # angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

        # screen.blit(self.image, self.rectangle)
