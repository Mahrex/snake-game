from turtle import Screen,Turtle
import time
from snake import *

# creating our screen and initializing it
screen = Screen()
screen.title('SNAKE GAME')
screen.setup(width=1250, height=699)
screen.tracer(0) # switching off the tracer method
screen.bgcolor('#000000')

# creating the snake object
snake = Snake()
SNAKE_SPEED = 0.09

# moving the snake by using user key-press
screen.listen()

# WASD keys to move snake
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

# arrow keys to move snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# moving our snake to any directions
game_on = True

while game_on:
    screen.update()
    time.sleep(SNAKE_SPEED)
    
    snake.move()
        
    
# our game screen wont be closed until we close it manually
screen.exitonclick()