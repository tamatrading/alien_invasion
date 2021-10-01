# ship.py

import pygame

""" 宇宙船を管理するクラス """


class Ship:
    """ 宇宙船を初期化し、開始時の位置を設定する """

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # 宇宙船の画像を読み込み、サイズを取得する
        self.image = pygame.image.load("images/ship_toumei.png")
        self.rect = self.image.get_rect()

        # 新しい宇宙船を画面下部の中央に配置する
        self.rect.midbottom = self.screen_rect.midbottom

        # 宇宙船の水平位置の浮動小数点数を格納する
        self.x = float(self.rect.x)

        # 移動フラグ
        self.moving_right = False
        self.moving_left = False

    """ 移動フラグによって宇宙船の位置を更新する """

    def update(self):

        # 宇宙船のxの位置を更新する（rectではない）
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # self.xからrectオブジェクトの位置を更新する
        self.rect.x = self.x

    """ 宇宙船を現在位置に描画する """

    def blitme(self):

        self.screen.blit(self.image, self.rect)
