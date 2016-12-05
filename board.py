import arcade
from random import randint

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class MainScreen(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)
		arcade.set_background_color(arcade.color.BABY_PINK)

		self.cat_sprites = []

		self.total_cat = randint(3, 9)
		
		self.plus = arcade.Sprite('images/plus.png')
		self.plus.set_position(100, 100)

		for i in range(1, self.total_cat):
			self.cat_sprites.append(arcade.Sprite('images/' + str(randint(1, 12)) + '.png'))
			self.cat_sprites[i - 1].set_position(randint(150, 850), randint(250, 475))

	def on_draw(self):
		arcade.start_render()

		for sprite in self.cat_sprites:
			sprite.draw()

		self.plus.draw()

if __name__ == '__main__':
	window = MainScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()