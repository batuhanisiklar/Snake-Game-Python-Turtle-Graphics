from turtle import Turtle

alignment = "center"
font = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}", align=alignment, font=font)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=alignment, font=font)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
