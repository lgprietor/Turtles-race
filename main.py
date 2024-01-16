
from tkinter import messagebox
import turtle as t
import random

color = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_objects = []
# # Turtle 1
# timmy = t.Turtle(shape = "turtle")
# timmy.penup()
# timmy.color(color[0])

# Creando un listado de tortugas


# timmy.goto(x=-230, y=0)

is_race_on = False
screen = t.Screen()

screen.setup(height=400, width=500)

user_input_validated = False

while not user_input_validated:

    user_bet = (screen.textinput(title = "Turtle Race - Bet Game", prompt = "Welcome to Turtle Race - Bet Race \n\n "
                                                                            "Please write one of the following options:"
                                                                            "\n\n red \n orange \n yellow \n green "
                                                                            "\n blue \n purple")
                .lower())

    if ((user_bet == "red") or (user_bet == "orange") or (user_bet == "yellow") or (user_bet == "green") or
            (user_bet == "blue") or (user_bet == "purple")):

        user_input_validated = True

    else:

        messagebox.showinfo("Error","Please write a valid option")

for i in range(len(color)):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = -100+(40*i))
    turtle_objects.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_objects:
        if turtle.xcor() > 230:
            is_race_on = False
            if user_bet == turtle.color()[1]:
                messagebox.showinfo("Results", f"The winner is {turtle.color()[1]}. You have won")
                break
            else:
                messagebox.showinfo("Results", f"The winner is {turtle.color()[1]}. Sorry, You lose")
                break

        random_pace = random.randint(0, 10)
        turtle.forward(random_pace)














screen.exitonclick()