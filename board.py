import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class MainScreen(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)
		arcade.set_background_color(arcade.color.AERO_BLUE)

	def on_draw(self):
		arcade.start_render()

if __name__ == '__main__':
	window = MainScreen(SCREEN_HEIGHT, SCREEN_WIDTH)
	arcade.run()