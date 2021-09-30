#bullet.py

import pygame
from pygame.sprite import Sprite

""" 宇宙船から発射される弾を管理するクラス """
class Bullet(Sprite):

	""" 宇宙船の現在の位置から弾のオブジェクトを生成する """
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		#弾のrectを(0,0)の位置に作成してから、正しい位置を設定する
		self.rect = pygame.Rect(0,0,self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midtop  = ai_game.ship.rect.midtop

		#弾の位置を浮動小数点数で保存する
		self.y = float(self.rect.y)

	""" 画面上の弾を移動する """
	def update(self):

		#弾の有働小数点数での位置を更新する
		self.y -= self.settings.bullet_speed

		#rectの位置を更新する
		self.rect.y = self.y

	""" 画面に弾を描画する """
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

