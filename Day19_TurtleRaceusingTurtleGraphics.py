import random
from turtle import Turtle, Screen

color_list = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
screen = Screen()
screen.listen()
screen.setup(height=400, width=500)
user_choice = screen.textinput(title="Make a bet", prompt="Which turtle can win?Choose a color(VIBGYOR):")
race_contenders = []
i = 0
for y in range(-90, 91, 30):
    new_y = y
    contender = Turtle("turtle")
    contender.color(color_list[i])
    i += 1
    contender.penup()
    contender.goto(x=-230, y=new_y)
    race_contenders.append(contender)
game_on = False

if user_choice:
    game_on = True

while game_on:
    for turtle in race_contenders:
        if turtle.xcor() >= 230:
            game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"Congratulations! {winning_color} turtle won the game")
            else:
                print(f"Bad Luck! {winning_color} turtle won the game")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
