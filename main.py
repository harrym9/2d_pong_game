from turtle import Turtle, Screen

HEIGHT = 600
WIDTH = 800
BACKGROUND_COLOR = "black"

screen = Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong Game")

def up():
    turtle.forward(15)
def down():
    turtle.backward(15)

turtle = Turtle()
turtle.color("white")
turtle.shape("square")
turtle.shapesize(stretch_len=4)
turtle.setheading(90)
turtle.penup()
turtle.speed(0)
turtle.goto(x=(WIDTH // 2) - 30, y=0)


screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")




screen.exitonclick()
