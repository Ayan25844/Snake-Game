import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.shape("circle")
        self.speed("fastest")
        self.shapesize(0.5,0.5)
        self.refresh()
        
    def refresh(self):
        x_cor=random.randint(-275,275)
        y_cor=random.randint(-275,275)
        self.goto(x_cor,y_cor)