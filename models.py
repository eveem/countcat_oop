import arcade.key
from random import randint

class Model:
	def __init__(self, world, x, y):
		self.world = world
		self.x = x
		self.y = y

class Cat(Model):
	def __init__(self, world, x, y):
		super().__init__(world, x, y)

class Button(Model):
	def __init__(self, world, x, y):
		super().__init__(world, x, y)

class Number(Model):
	def __init__(self, world, x, y):
		super().__init__(world, x, y)

class Paw(Model):
	def __init__(self, world, x, y):
		super().__init__(world, x, y)

class World:
	TOTAL_CAT = randint(1, 9)

	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.decrease_button = []
		self.increase_button = []
		self.decrease_button.append(Button(self, 100, 100))
		self.decrease_button.append(Button(self, 700, 100))
		self.increase_button.append(Button(self, 300, 100))
		self.increase_button.append(Button(self, 900, 100))

		self.cats = []
		for i in range(World.TOTAL_CAT):
			cat = Cat(self, randint(150, 850), randint(250, 475))
			self.cats.append(cat)

		self.paws = []
		x_pos = 100
		for i in range(10):
			paw = Paw(self, x_pos, 23)
			self.paws.append(paw)
			if i == 4:
				x_pos = 650
			x_pos += 50

		self.number = []
		self.number.append(Number(self, 200, 100))
		self.number.append(Number(self, 800, 100))

		start_number = randint(0, 9)
		self.number_count = [start_number, start_number]
		self.point = [0, 0]

	def on_key_press(self, key, key_modiriers):
		if key == arcade.key.A:
			self.number_count[0] -= 1
		elif key == arcade.key.D:
			self.number_count[0] += 1

		if key == arcade.key.J:
			self.number_count[1] -= 1
		elif key == arcade.key.L:
			self.number_count[1] += 1

		for i in range(2):
			if self.number_count[i] > 9:
				self.number_count[i] = 0
			if self.number_count[i] < 0:
				self.number_count[i] = 9

		if key == arcade.key.S and self.number_count[0] == self.TOTAL_CAT:
			self.point[0] += 1

		if key == arcade.key.K and self.number_count[1] == self.TOTAL_CAT:
			self.point[1] += 1
