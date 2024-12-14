from turtle import Screen
import time, snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game!")
snake = snake.Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score()
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 or snake.head.xcor() < -290:
        scoreboard.reset()
        snake.new_snake()
        # game_on = False
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.new_snake()
            # game_on = False
# scoreboard.game_over()
screen.exitonclick()
