# In this implementation we show how the tower of hanoi could be done through turtle graphics
# This was initially part of the question, and we added it as we thought it would be a nice touch
# Regardless the code to the work pertaining to our proposal is also in the repo called HanoiTowers.py

# Importing the necessary modules
# Turtle is imported here for the interface where we can see the algorithm solving the tower of hanoi
import turtle
import time

# Creating the window where users will be able to visualize the game
win = turtle.Screen()
win.setup(800, 600)
win.title('Tower of Hanoi')
win.bgcolor('white')
win.tracer(0)

# Create our turtles ( objects of the turtle class )
base = turtle.Turtle()
base.color('grey')
base.shape('square')
base.up()
base.goto(0, -200)
base.shapesize(1, 35)

# Creating the pin ( this is where the discs start )
# We 3 pins ( start, auxilliary, and finish)
class Pin(turtle.Turtle):
    def __init__(self, xpos):
        super().__init__(shape='square')
        self.xpos = xpos
        self.up()
        self.color('grey')
        self.shapesize(10,1)
        self.goto(self.xpos, -100)
        self.count = 0
        self.pos_list = [-180, -160, -140, -120, -100]
        self.discs = []


# Creating the discs
class Disc(turtle.Turtle):
    def __init__(self, xpos, ypos, size, color):
        super().__init__(shape='square')
        self.xpos = xpos
        self.ypos = ypos
        self.size = size
        self.color(color)
        self.up()
        self.shapesize(1, self.size)
        self.goto(self.xpos, self.ypos)

# functions to move the discs
def move_disc(disc, pin):
    while disc.ycor()<100:
        disc.goto(disc.xcor(),disc.ycor()+5)
        win.update()
    disc.goto(pin.xcor(),100)
    win.update()
    while disc.ycor()>pin.pos_list[pin.count]:
        disc.goto(disc.xcor(),disc.ycor()-5)
        win.update()
    time.sleep(0.01)

# rules for movign the discs
def move(f,t):
    print(f'Move disc from {f} to {t}!')
    if f == 'A':
        topDisc = pin1.discs[-1]
        start_pin = pin1
    elif f == 'B':
        topDisc = pin2.discs[-1]
        start_pin = pin2
    elif f == 'C':
        topDisc = pin3.discs[-1]
        start_pin = pin3

    if t == 'A':
        pin = pin1
    elif t == 'B':
        pin = pin2
    elif t == 'C':
        pin = pin3
        
    move_disc(topDisc, pin)
    start_pin.count -= 1
    start_pin.discs.pop()
    pin.count += 1
    pin.discs.append(topDisc)

# Towers of hanoi game algorithm
def hanoi(n,f,h,t):
    if n == 0:
        pass
    else:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

pin1 = Pin(-200)
pin2 = Pin(0)
pin3 = Pin(200)

# Asking the user how many discs they want to play
# The higher the number of discs the more challenging

stack_num = int(input("Please insert the number of stacks you want your tower to have! not more than 7"))
while stack_num > 7:
    stack_num = int(input("the number entered was too high"))

disc_list = []
if stack_num == 1:
    disc1 = Disc(-200, -180, 11, 'orange')
    disc_list.append(disc1)
    print('appended')
elif stack_num == 2:
    disc1 = Disc(-200, -180, 11, 'orange')
    disc2 = Disc(-200, -160, 9.5, 'blue')
    disc_list.extend([disc1, disc2])
    print('appended')
elif stack_num == 3:
    disc1 = Disc(-200, -180, 11, 'orange')
    disc2 = Disc(-200, -160, 9.5, 'blue')
    disc3 = Disc(-200, -140, 8, 'red')
    disc_list.extend([disc1, disc2, disc3])
    print('appended')
elif stack_num == 4:
    disc1 = Disc(-200, -180, 11, 'orange')
    disc2 = Disc(-200, -160, 9.5, 'blue')
    disc3 = Disc(-200, -140, 8, 'red')
    disc4 = Disc(-200, -120, 6.5, 'yellow')
    disc_list.extend([disc1, disc2, disc3, disc4])
    print('appended')
elif stack_num == 5:
    disc1 = Disc(-200, -180, 11, 'orange')
    disc2 = Disc(-200, -160, 9.5, 'blue')
    disc3 = Disc(-200, -140, 8, 'red')
    disc4 = Disc(-200, -120, 6.5, 'yellow')
    disc5 = Disc(-200, -100, 5, 'green')
    disc_list.extend([disc1, disc2, disc3, disc4, disc5])
    print('appended')
elif stack_num == 6:
    disc1 = Disc(-200, -180, 11, 'orange')
    disc2 = Disc(-200, -160, 9.5, 'blue')
    disc3 = Disc(-200, -140, 8, 'red')
    disc4 = Disc(-200, -120, 6.5, 'yellow')
    disc5 = Disc(-200, -100, 5, 'green')
    disc6 = Disc(-200, -80, 3.5, 'purple')
    disc_list.extend([disc1, disc2, disc3, disc4, disc5, disc6])
    print('appended')
elif stack_num == 7:
    disc1 = Disc(-200, -180, 11, 'orange')
    disc2 = Disc(-200, -160, 9.5, 'blue')
    disc3 = Disc(-200, -140, 8, 'red')
    disc4 = Disc(-200, -120, 6.5, 'yellow')
    disc5 = Disc(-200, -100, 5, 'green')
    disc6 = Disc(-200, -80, 3.5, 'purple')
    disc7 = Disc(-200, -60, 2, 'pink')
    disc_list.extend([disc1, disc2, disc3, disc4, disc5, disc6, disc7])
    print('appended')


# Initialising the pins
pin1.count = stack_num
pin1.discs = disc_list

# game play
hanoi(stack_num, 'A', 'B', 'C')
