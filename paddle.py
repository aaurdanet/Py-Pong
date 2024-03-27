from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.goto(x, y)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_y = self.ycor() + 20
        new_x = self.xcor()
        self.goto(new_x, new_y)

    def down(self):
        new_y = self.ycor() - 20
        new_x = self.xcor()
        self.goto(new_x, new_y)
