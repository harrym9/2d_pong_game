from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        if self.xcor() < 380 and self.ycor() < 280:
            new_x = self.xcor() + 12
            new_y = self.ycor() + 9
            self.goto(new_x, new_y)
