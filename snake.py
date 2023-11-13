MOVE_DISTANCE=20
from turtle import Turtle

class Snake():

    def __init__(self):
        self.count=3
        self.segments=[]
        for i in range(self.count):
            self.add(i)
        self.head=self.segments[0]

    def add(self,position):
        timmy=Turtle("square")
        timmy.penup()
        timmy.color("white")
        timmy.goto(-(position*20),0)
        self.segments.append(timmy)

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x=self.segments[i-1].xcor()
            new_y=self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
            
    def extend(self):
        self.add(self.count)  
