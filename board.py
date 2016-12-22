import arcade
from random import randint

from models import World

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class ModelSprite(arcade.Sprite):
	def __init__(self, *args, **kwargs):
		self.model = kwargs.pop('model', None)

		super().__init__(*args, **kwargs)

	def sync_with_model(self):
		if self.model:
			self.set_position(self.model.x, self.model.y)

	def draw(self):
		self.sync_with_model()
		super().draw()

class MainScreen(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)
		
		arcade.set_background_color(arcade.color.BABY_PINK)

		self.world = World(width, height)

		# self.decrease_button = ModelSprite('images/minus.png', model=self.world.button)
		# self.increase_button = ModelSprite('images/plus.png', model=self.world.button)

		self.cats_sprite = []
		for cat in self.world.cats:
			self.cats_sprite.append(ModelSprite('images/CAT' + str(randint(1, 12)) + '.png', model=cat))

		# self.check_left = 0
		# self.check_right = 0

		# start = randint(0, 9)
		# self.score_left = start
		# self.score_right = start
		# self.cat_sprites = []

		# self.total_cat = randint(3, 9)
		
		# self.plus_left = arcade.Sprite('images/plus.png')
		# self.minus_left = arcade.Sprite('images/minus.png')
		# self.plus_left.set_position(300, 75)
		# self.minus_left.set_position(100, 75)

		# self.plus_right = arcade.Sprite('images/plus.png')
		# self.minus_right = arcade.Sprite('images/minus.png')
		# self.plus_right.set_position(900, 75)
		# self.minus_right.set_position(700, 75)

		# for i in range(1, self.total_cat):
		# 	self.cat_sprites.append(arcade.Sprite('images/CAT' + str(randint(1, 12)) + '.png'))
		# 	self.cat_sprites[i - 1].set_position(randint(150, 850), randint(250, 475))

	def on_draw(self):
		arcade.start_render()

		for cat in self.cats_sprite:
			cat.draw()

		# self.plus_left.draw()
		# self.minus_left.draw()

		# self.plus_right.draw()
		# self.minus_right.draw()

		# self.number_left = arcade.Sprite('images/' + str(self.score_left) + '.png')
		# self.number_left.set_position(200, 75)
		# self.number_left.draw()

		# self.number_right = arcade.Sprite('images/' + str(self.score_right) + '.png')
		# self.number_right.set_position(800, 75)
		# self.number_right.draw()

		# arcade.draw_text(str(self.check_left), self.width - 60, self.height - 60, arcade.color.BLACK, 20)
		# arcade.draw_text(str(self.check_right), self.width - 60, self.height - 60, arcade.color.BLACK, 20)

	def on_key_press(self, key, key_modifiers):
		self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__':
	window = MainScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()