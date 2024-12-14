from turtle import Turtle
import random
COLOR = ["pink", "blue", "teal", "orange", "red", "yellow", "green", "violet", "purple"]


class Food(Turtle):
    def __init__ (self):
        super().__init__()
        self.penup()
        self.color("pink")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)
        self.color(COLOR[random.randint(0, 8)])
