from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-80, 230)
        self.write(arg=self.l_score, align="center", font=("Courier,", 50, "normal"))
        self.goto(80, 230)
        self.write(arg=self.r_score, align="center", font=("Courier,", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
