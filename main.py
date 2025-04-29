from snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.title("My Snake Game")
screen.tracer(0)
game_is_on = True

my_snake = Snake()

screen.listen()  # Make the screen listen for key events
screen.onkey(my_snake.go_up, "Up")
screen.onkey(my_snake.go_down, "Down")
screen.onkey(my_snake.go_left, "Left")
screen.onkey(my_snake.go_right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move_snake()

    if my_snake.touched_wall():
        my_snake.clear_snake()
        my_snake = Snake()  # Create a new snake when wall is touched
