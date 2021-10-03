import pygame
from pygame.sprite import Sprite

""" 星クラス """

class Star(Sprite):

    def __init__(self, ai_game):

        super().__init__()
        self.screen = ai_game.screen

        #星の画像を読み込み、サイズを取得する
        self.image = pygame.image.load('images/star.png')
        # self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()

        #新しい星を画面の左上の近くに配置する
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #星の実際の位置を格納する
        self.x = float(self.rect.x)
