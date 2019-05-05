import pygame
import time as timer
from Plane import Plane


class ScoreBoard:
    score = 0
    time = 60
    textColor = (255, 255, 255)
    rectangle = pygame.rect.Rect(0, 50, 200, 50)
    time_text_rectangle = pygame.rect.Rect(650, 20, 100, 50)
    EndOfTimeEvent = pygame.event.Event(pygame.USEREVENT, {"EventName": "EndOfTimeEvent"})
    gameOver = False
    score_fontedText = None
    score_textRectangle = None
    time_text = None

    @staticmethod
    def reset():
        ScoreBoard.score = 0
        ScoreBoard.time = 60
        Plane.ammo = 20


    @staticmethod
    def prepare_text(text,text_size=100):
        pygame.font.init()
        return pygame.font.Font("fonts/ARCADE.TTF", text_size).render(
            str(text), True, ScoreBoard.textColor)

    @staticmethod
    def init_ScoreBoard(rectangle=pygame.rect.Rect(0, 50, 200, 50), textSize=100, textColor=(255, 255, 255)):
        ScoreBoard.textSize = textSize
        ScoreBoard.textColor = textColor
        ScoreBoard.rectangle = rectangle
        ScoreBoard.time_text = ScoreBoard.prepare_text(ScoreBoard.time)

    @staticmethod
    def set_Score(score=0,textSize = 100):
        # ScoreBoard.score += score
        ScoreBoard.score_fontedText = pygame.font.Font("fonts/ARCADE.TTF", textSize).render(
            str(score), True, ScoreBoard.textColor)
        ScoreBoard.score_textRectangle = pygame.rect.Rect(0, 0, ScoreBoard.score_fontedText.get_width(),
                                                          ScoreBoard.score_fontedText.get_height())
        ScoreBoard.score_textRectangle.center = ScoreBoard.rectangle.center

    @staticmethod
    def draw(screen):
        # ScoreBoard.set_Score(ScoreBoard.score)
        screen.blit(pygame.font.Font("fonts/ARCADE.TTF", 100).render(
            str(ScoreBoard.score), True, ScoreBoard.textColor), ScoreBoard.score_textRectangle)
        screen.blit(ScoreBoard.time_text, ScoreBoard.time_text_rectangle)

    @staticmethod
    def init_Timer(rectangle=pygame.rect.Rect(0, 50, 200, 50), textSize=100, textColor=(255, 255, 255)):
        ScoreBoard.textSize = textSize
        ScoreBoard.textColor = textColor
        ScoreBoard.rectangle = rectangle

    @staticmethod
    def getTextRectangle(width, height):
        textRectangle = pygame.rect.Rect(100, 100, width, height)
        # textRectangle.center = ScoreBoard.text_container_rectangle.center
        return textRectangle

    @staticmethod
    def timer_func(screen):
        while ScoreBoard.time is not 0 and not ScoreBoard.gameOver:
            ScoreBoard.time_text = ScoreBoard.prepare_text(ScoreBoard.time)
            # screen.blit(ScoreBoard.fontedText, ScoreBoard.text_container_rectangle)
            ScoreBoard.time -= 1
            timer.sleep(1)
        if ScoreBoard.time is 0:
            pygame.event.post(ScoreBoard.EndOfTimeEvent)
            screen.blit(ScoreBoard.prepare_text("Sure Doldu Basaramadin",50), ScoreBoard.getTextRectangle(100, 100))
