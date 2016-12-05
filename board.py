import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class MainScreen(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)
		arcade.set_background_color(arcade.color.BABY_PINK)

		self.cat_sprites = []
		for i in range(1, 13):
			self.cat_sprites.append(arcade.Sprite('images/' + str(i) + '.png'))
			

	def on_draw(self):
		arcade.start_render()
		
		for sprite in self.cat_sprites:
			sprite.draw()

if __name__ == '__main__':
	window = MainScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()