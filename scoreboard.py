# EVERYTHING RELATED TO OUR 'SCORE' WILL BE HERE
from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    
    # initializing the scoreboard object
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('#ffffff')
        self.penup()
        self.hideturtle()
        self.goto(0,315)
        self.update_scoreboard()
        
    # updating the scoreboard
    def update_scoreboard(self):
        self.write(f'SCORE: {self.score}', align=ALIGNMENT,font=FONT)
        
    # increasing the score everytime snake eats a food
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()