#
# from tkinter import messagebox
# import turtle as t
# import random
#
# color = ["red", "orange", "yellow", "green", "blue", "purple"]
# turtle_objects = []
# # # Turtle 1
# # timmy = t.Turtle(shape = "turtle")
# # timmy.penup()
# # timmy.color(color[0])
#
# # Creando un listado de tortugas
#
#
# # timmy.goto(x=-230, y=0)
#
# is_race_on = False
# screen = t.Screen()
#
# screen.setup(height=400, width=500)
#
# user_input_validated = False
#
# while not user_input_validated:
#
#     user_bet = (screen.textinput(title = "Turtle Race - Bet Game", prompt = "Welcome to Turtle Race - Bet Race \n\n "
#                                                                             "Please write one of the following options:"
#                                                                             "\n\n red \n orange \n yellow \n green "
#                                                                             "\n blue \n purple")
#                 .lower())
#
#     if ((user_bet == "red") or (user_bet == "orange") or (user_bet == "yellow") or (user_bet == "green") or
#             (user_bet == "blue") or (user_bet == "purple")):
#
#         user_input_validated = True
#
#     else:
#
#         messagebox.showinfo("Error","Please write a valid option")
#
# for i in range(len(color)):
#     new_turtle = t.Turtle(shape="turtle")
#     new_turtle.color(color[i])
#     new_turtle.penup()
#     new_turtle.goto(x = -230, y = -100+(40*i))
#     turtle_objects.append(new_turtle)
#
# if user_bet:
#     is_race_on = True
#
# while is_race_on:
#     for turtle in turtle_objects:
#         if turtle.xcor() > 230:
#             is_race_on = False
#             if user_bet == turtle.color()[1]:
#                 messagebox.showinfo("Results", f"The winner is {turtle.color()[1]}. You have won")
#                 break
#             else:
#                 messagebox.showinfo("Results", f"The winner is {turtle.color()[1]}. Sorry, You lose")
#                 break
#
#         random_pace = random.randint(0, 10)
#         turtle.forward(random_pace)

# screen.exitonclick()

import turtle as t
import random
from tkinter import messagebox


screen = t.Screen()
screen.setup(height=400, width=500)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

is_user_guess_ok = False

while not is_user_guess_ok:

    user_guess = screen.textinput("Turtle Race - Bet Game", "Welcome to turtle race - bet game. "
                                                            "Please write of the following colors: \n\n Red\n Orange \n"
                                                            "Yellow \n Green \n Blue \n Purple").lower()

    if (user_guess == "red" or user_guess == "orange" or user_guess == "yellow" or user_guess == "green" or
            user_guess == "blue" or user_guess == "purple"):

        is_user_guess_ok = True

    else:

        messagebox.showinfo(title="Error",message="Please write a valid option")


for i in range(len(colors)):
    new_turtle = t.Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100+(40*i))
    turtles.append(new_turtle)

game_off = False

while not game_off:
    for turtle in turtles:
        random_pace = random.randint(0,10)
        turtle.forward(random_pace)
        if turtle.xcor() >= 230:
            game_off = True
            if user_guess == turtle.fillcolor():
                messagebox.showinfo(title="Results", message=f"You have won. The turtle {turtle.fillcolor()} is the "
                                                             f"winner")
                break
            else:
                messagebox.showinfo(title="Results",
                                    message=f"You have lost. The turtle {turtle.fillcolor()} is the winner")
                break




















screen.exitonclick()
















































