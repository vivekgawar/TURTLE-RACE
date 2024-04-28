from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(height=500, width=500)
user_bet = screen.textinput(title="Make Your Bet", prompt="Who will win the race? Enter color")

race_is_on = False

# Making Turtles
tim1 = Turtle()
tim2 = Turtle()
tim3 = Turtle()
tim4 = Turtle()
tim5 = Turtle()
tim6 = Turtle()
turtles = [tim1, tim2, tim3, tim4, tim5, tim6]

# Giving them colours
tim1.color("red")
tim2.color("orange")
tim3.color("yellow")
tim4.color("green")
tim5.color("blue")
tim6.color("purple")

# Giving them shape
for i in turtles:
    i.shape("turtle")

# No doodling
for i in turtles:
    i.penup()

# Setting starting line
tim1.goto(-230, 100)
tim2.goto(-230, 70)
tim3.goto(-230, 40)
tim4.goto(-230, 10)
tim5.goto(-230, -20)
tim6.goto(-230, -50)

# LET THE RACE BEGIN
if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            if turtle.pencolor() == user_bet.lower():
                print(f"You won the bet! {turtle.pencolor()} turtle wins")
            else:
                print(f"You lost the bet! {turtle.pencolor()} turtle wins")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
