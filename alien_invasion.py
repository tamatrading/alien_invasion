# alien_invasion.py

import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

""" ゲームのアセットと動作を管理する全体的なクラス """


class AlienInvasion:
    """ ゲームを初期化し、ゲームのリソースを作成する """

    def __init__(self):

        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("エイリアン侵略")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    """ ゲームのメインループを開始する """

    def run_game(self):

        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    """ キーボードのマウスのイベントを監視する """

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("終了！")
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    """ キーを押すイベントに対応する """

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:  # 右へ移動
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # 左へ移動
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:  # 弾を発射
            self._fire_bullet()
        elif event.key == pygame.K_q:  # qを押したら終了させる
            sys.exit()

    """ キーを離すイベントに対応する """

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:  # 右移動を停止
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:  # 左移動を停止
            self.ship.moving_left = False

    """ 新しい弾を生成し、bulletsグループに追加する """

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    """ 弾の位置を更新し、見えなくなった弾を廃棄する """

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    # print(len(self.bullets))

    """ 画面上の画像を更新し、新しい画面に切り替える """

    def _update_screen(self):

        # ループを通過するたびに画面を再描画する
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 最新の状態の画面を表示する
        pygame.display.flip()


if __name__ == "__main__":
    # ゲームのインスタンスを作成し、ゲームを実行する
    ai = AlienInvasion()
    ai.run_game()
