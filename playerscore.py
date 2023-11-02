from turtle import Turtle

FONT = ('Courier', 24, 'normal')
ALIGNMENT = "center"


class PlayerScore(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.shape('square')
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write_score()

    def write_score(self):
        self.write(arg=self.score, move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()
