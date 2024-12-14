from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score_count = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.setposition(0, 250)
        self.score()

    def reset(self):
        if self.score_count > self.high_score:
            self.high_score = self.score_count
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score_count = 0

    def score(self):
        self.clear()
        self.write(arg=f"Score:{self.score_count}  High Score:{self.high_score}", align=ALIGNMENT, font=FONT)
        self.score_count += 1

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)
