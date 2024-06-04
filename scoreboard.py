from turtle import Turtle, Screen
screen = Screen()
ALIGNMENT = 'Center'
FONT = ('Courier', 22, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        self.count = 0
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 250)
        self.write(f'Score :: {self.count}', align=ALIGNMENT, font=FONT)
    
    def gameover(self):
        screen.clearscreen()
        screen.bgcolor('black')
        self.hideturtle()
        self.goto(0, 250)
        self.color('white')
        self.write(f'Score :: {self.count}', align=ALIGNMENT, font=FONT)
        self.goto(0, 0)
        self.write(f':: Game Over ::', align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.clear()
        self.hideturtle()
        self.count += 1
        self.write(f'Score :: {self.count}', align=ALIGNMENT, font= FONT)
        