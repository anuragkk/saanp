from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color("blue")
            new_turtle.goto(x=i * (-20), y=0)
            self.segments.append(new_turtle)

    def move_snake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def touched_wall(self):

        x = self.head.xcor()
        y = self.head.ycor()

        if x > 290 or x < -290 or y > 290 or y < -290:
            self.clear_snake()

    def clear_snake(self):
        for segment in self.segments:
            segment.goto(5000, 5000)
