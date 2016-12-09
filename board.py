import arcade
from random import randint

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class MainScreen(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)
		arcade.set_background_color(arcade.color.BABY_PINK)

		self.check_left = 0
		self.check_right = 0

		start = randint(0, 9)
		self.score_left = start
		self.score_right = start
		self.cat_sprites = []

		self.total_cat = randint(3, 9)
		
		self.plus_left = arcade.Sprite('images/plus.png')
		self.minus_left = arcade.Sprite('images/minus.png')
		self.plus_left.set_position(300, 75)
		self.minus_left.set_position(100, 75)

		self.plus_right = arcade.Sprite('images/plus.png')
		self.minus_right = arcade.Sprite('images/minus.png')
		self.plus_right.set_position(900, 75)
		self.minus_right.set_position(700, 75)

		for i in range(1, self.total_cat):
			self.cat_sprites.append(arcade.Sprite('images/CAT' + str(randint(1, 12)) + '.png'))
			self.cat_sprites[i - 1].set_position(randint(150, 850), randint(250, 475))

	def on_draw(self):
		arcade.start_render()

		for sprite in self.cat_sprites:
			sprite.draw()

		self.plus_left.draw()
		self.minus_left.draw()

		self.plus_right.draw()
		self.minus_right.draw()

		self.number_left = arcade.Sprite('images/' + str(self.score_left) + '.png')
		self.number_left.set_position(200, 75)
		self.number_left.draw()

		self.number_right = arcade.Sprite('images/' + str(self.score_right) + '.png')
		self.number_right.set_position(800, 75)
		self.number_right.draw()

		arcade.draw_text(str(self.check_left), self.width - 60, self.height - 60, arcade.color.BLACK, 20)
		# arcade.draw_text(str(self.check_right), self.width - 60, self.height - 60, arcade.color.BLACK, 20)

	def on_key_press(self, key, key_modifiers):
		if key == arcade.key.A:
			self.score_left -= 1
		elif key == arcade.key.D:
			self.score_left += 1

		if key == arcade.key.J:
			self.score_right -= 1
		elif key == arcade.key.L:
			self.score_right += 1

		if self.score_left > 9:
			self.score_left = 0
		elif self.score_left < 0:
			self.score_left = 9

		if self.score_right > 9:
			self.score_right = 0
		elif self.score_right < 0:
			self.score_right = 9

		if key == arcade.key.S and self.score_left == self.total_cat - 1:
			self.check_left += 1

		if key == arcade.key.K and self.score_right == self.total_cat - 1:
			self.check_right += 1

if __name__ == '__main__':
	window = MainScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()