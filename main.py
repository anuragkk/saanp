from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("My Snake Game")
screen.tracer(0)
game_is_on = True

my_snake = Snake()
my_food = Food()
my_score = Scoreboard()

screen.listen()
screen.onkey(my_snake.go_up, "Up")
screen.onkey(my_snake.go_down, "Down")
screen.onkey(my_snake.go_left, "Left")
screen.onkey(my_snake.go_right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_score.update_scoreboard()
    my_snake.move_snake()

    # Detect collision with food
    if my_snake.head.distance(my_food) < 25:
        my_score.increase_score()
        my_food.refresh()
        for i in range(30):
            my_snake.extend_snake()

    # Detect collision with the wall
    if my_snake.touched_wall():
        my_score.final_score()

        game_is_on = False


screen.update()


screen.exitonclick()


