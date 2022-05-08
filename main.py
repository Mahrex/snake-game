from turtle import Screen,Turtle
import time
from snake import *
from food import *
from scoreboard import * 

# creating our screen and initializing it
screen = Screen()
screen.title('SNAKE GAME')
screen.setup(width=1250, height=700)
screen.tracer(0) # switching off the tracer method
screen.bgcolor('#000000')

# creating the snake object
snake = Snake()
SNAKE_SPEED = 0.09

# creating the food object
food = Food()

# creating the scoreboard object
scoreboard = Scoreboard()

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
    
    # free moving of the snake
    snake.move()
    
    # detecting if any collision with our food and get 1 point
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        # SNAKE_SPEED *= 0.2
        
    # detecting collision with our the wall
    if snake.head.xcor() > 630 or snake.head.xcor() < -630 or snake.head.ycor() > 350 or snake.head.ycor() < -350: # co-ordinates bug
        game_on = False
        scoreboard.game_over()
        
    # detecting collision with it's own tail
    # looping thru each of the segments (excluding the head) to know if distance b/w head and other segments is < N
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
    
# our game screen wont be closed until we close it manually
screen.exitonclick()