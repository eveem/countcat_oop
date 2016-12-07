import arcade
from random import randint

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class MainScreen(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)
		arcade.set_background_color(arcade.color.BABY_PINK)

		self.score_left = randint(0, 9)
		self.score_right = randint(0, 9)
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

	def on_key_press(self, key, key_modifiers):
		if key == arcade.key.A:
			self.score_left += 1
			if self.score_left > 9:
				self.score_left = 0

if __name__ == '__main__':
	window = MainScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()