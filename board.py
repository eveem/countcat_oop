import arcade
import arcade.sound
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
		
		self.end = False
		arcade.set_background_color(arcade.color.BABY_PINK)

		self.world = World(width, height)

		self.win_sprite = []
		self.win_sprite.append(arcade.Sprite('images/left_win.png', scale=0.5))
		self.win_sprite.append(arcade.Sprite('images/right_win.png', scale=0.5))

		self.decrease_sprite = []
		self.increase_sprite = []
		for i in range(2):
			self.decrease_sprite.append(ModelSprite('images/minus.png', model=self.world.decrease_button[i]))
			self.increase_sprite.append(ModelSprite('images/plus.png', model=self.world.increase_button[i]))
			self.win_sprite[i].set_position(500, 300)

		self.paw_sprite = []
		for i in range(10):
			self.paw_sprite.append(ModelSprite('images/paw.png', scale=0.3, model=self.world.paws[i]))

		self.cats_sprite = []
		for i in range(self.world.TOTAL_CAT):
			self.cats_sprite.append(ModelSprite('images/CAT' + str(randint(2, 12)) + '.png', model=self.world.cats[i]))

		self.warning_sprite = arcade.Sprite('images/warning.png', scale=0.8)
		self.warning_sprite.set_position(500, 565)

		self.ending_cat = arcade.Sprite('images/CAT1.png', scale=1.5)
		self.ending_cat.set_position(500, 275)

	def on_draw(self):
		arcade.start_render()
		
		self.warning_sprite.draw()

		for i in range(2):
			if self.world.winning[i]:
				self.ending_cat.draw()
				self.win_sprite[i].draw()
				self.end = True
				break

		if self.end == False:
			if self.world.correct:
				self.cats_sprite = []
				for i in range(self.world.TOTAL_CAT):
					self.cats_sprite.append(ModelSprite('images/CAT' + str(randint(2, 12)) + '.png', model=self.world.cats[i]))
				self.world.correct = False

			for cat in self.cats_sprite:
				cat.draw()

			for button_index in range(2):
				self.decrease_sprite[button_index].draw()
				self.increase_sprite[button_index].draw()

			for i in range(0, self.world.point[0]):
				self.paw_sprite[i].draw()

			for i in range(5, 5 + self.world.point[1]):
				self.paw_sprite[i].draw()		

			self.number_left = ModelSprite('images/' + str(self.world.number_count[0]) + '.png', model=self.world.number[0])
			self.number_right = ModelSprite('images/' + str(self.world.number_count[1]) + '.png', model=self.world.number[1])

			self.number_left.draw()
			self.number_right.draw()

	def on_key_press(self, key, key_modifiers):
		self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__':
	window = MainScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()