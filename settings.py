# settings.py

""" エイリアン侵略の全設定を格納するクラス """


class Settings:
    """ ゲームの初期設定 """

    def __init__(self):
        # 画面に関する設定
        self.screen_width = 850
        self.screen_height = 600
        # self.bg_color = (230,230,230)
        self.bg_color = (5, 5, 20)
        self.ship_speed = 1.5

        # 弾の設定
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 3
