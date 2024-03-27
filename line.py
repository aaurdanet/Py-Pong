from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.pendown()
        self.goto(0, -300)
        self.width(5)


    def drawing(self):
        for _ in range(0, 70):
            self.setheading(90)
            self.color("white")
            self.pendown()
            self.forward(10)
            self.color("black")
            self.forward(10)
