from turtle import Screen

HEIGHT = 600
WIDTH = 800
BACKGROUND_COLOR = "black"
class GameScreen(Screen):
    def __init__(self):
        super().__init__()
        self.setup(height = HEIGHT, width = WIDTH)
        self.bgcolor(BACKGROUND_COLOR)

game_screen = GameScreen()
game_screen.exitonclick()