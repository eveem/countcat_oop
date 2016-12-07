import arcade.key
from random import randint

class Model:
	def __init__(self, world, x, y):
		self.world = world
		self.x = x
		self.y = y

class Button(Model):
	def __init__(self, world, x, y):
		super().__init__(world, x, y, 0)

	def 