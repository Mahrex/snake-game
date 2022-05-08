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
        '''Function will update the scoreboard with the current score'''
        self.write(f'SCORE: {self.score}', align=ALIGNMENT,font=FONT)
        
    # game over condition
    def game_over(self):
        '''Function will say game-over after any collision'''
        self.goto(0,0)
        self.write('GAME OVER.', align=ALIGNMENT,font=FONT)
        
    # increasing the score everytime snake eats a food
    def increase_score(self):
        '''Function will add 1 point with the current score on the scoreboard'''
        self.score += 1
        self.clear()
        self.update_scoreboard()