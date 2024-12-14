from turtle import Turtle
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.snake()
        self.head = self.segments[0]

    def snake(self):
        for i in START_POSITION:
            self.add_segment(i)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def new_snake(self):
        for i in self.segments:
            i.goto(1000, 1000)
        self.segments.clear()
        self.snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            a = self.segments[i-1].xcor()
            b = self.segments[i-1].ycor()
            self.segments[i].goto(a, b)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
