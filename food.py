# EVERYTHING RELATED TO OUR 'FOOD' WILL BE HERE
from turtle import Turtle
import random

# food class will inherit from turtle class
class Food(Turtle):
    
    # initializing the food object
    def __init__(self):
        super().__init__() # initializing everything to food class from turtle class
        self.shape('circle')
        self.color('#21aacc')
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.speed('fastest')
        self.refresh()
        
    # everytime food will be recreated at a different location
    def refresh(self):
        '''Function will produce a food at any random location on the screen'''
        random_x = random.randint(-600,600)
        random_y = random.randint(-325,325)
        self.goto(random_x,random_y)