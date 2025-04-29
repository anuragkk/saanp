from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        # Properly calling the constructor of the parent class
        super().__init__()

        self.shape("circle")  # Set the food shape directly
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        # This method places the food at a random position
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

    def get_food(self):
        return self
