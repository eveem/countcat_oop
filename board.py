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

		self.decrease_sprite = []
		self.increase_sprite = []
		for i in range(2):
			self.decrease_sprite.append(ModelSprite('images/minus.png', model=self.world.decrease_button[i]))
			self.increase_sprite.append(ModelSprite('images/plus.png', model=self.world.increase_button[i]))

		self.cats_sprite = []
		for cat in self.world.cats:
			self.cats_sprite.append(ModelSprite('images/CAT' + str(randint(1, 12)) + '.png', model=cat))

	def on_draw(self):
		arcade.start_render()

		for cat in self.cats_sprite:
			cat.draw()

		for button_index in range(2):
			self.decrease_sprite[button_index].draw()
			self.increase_sprite[button_index].draw()

	def on_key_press(self, key, key_modifiers):
		self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__':
	window = MainScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()