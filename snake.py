# EVERYTHING RELATED TO OUR 'SNAKE' WILL BE HERE
from turtle import Turtle

# constant value of the initial snake positions
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)] 

# other snake constants
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():
    
    # initializing the snake
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    # creating the method to create a new snake(initially)
    def create_snake(self):
        '''Function will create a new snake with three blocks of squares.'''
        for position in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.penup()
            new_segment.color('#0af21d')
            new_segment.goto(position)
            self.segments.append(new_segment)
            
    # creating the move method to move the snake
    def move(self):
        '''Function will move the snake forward in the direction created.'''
         # logic behind turning of our snake
        for seg_num in range(len(self.segments) - 1, 0, -1): # looping thru last block to 1st
            new_x = self.segments[seg_num - 1].xcor() # getting x_cor of 2nd last block
            new_y = self.segments[seg_num - 1].ycor() # getting y_cor of 2nd last block
            self.segments[seg_num].goto(new_x, new_y) # last block will go to pos of 2nd last
    
        # moving the snake(1st block) forward
        self.head.forward(MOVE_DISTANCE)
        
    # moving in different directions (Up, Down, Left, Right)
    # snake can not move in reverse direction
    def up(self):
        # if moving in the down, it can't move in the up direction
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)