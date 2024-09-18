import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.tolist()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another"
                                                                                             " state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in states and answer_state not in guessed_states:
        pen = turtle.Turtle()
        pen.penup()
        pen.hideturtle()
        state_data = data[data.state == answer_state]
        pen.goto(state_data.x.item(), state_data.y.item())
        pen.color("black")
        pen.write(answer_state)
        guessed_states.append(answer_state)

s = set(guessed_states)
states_to_learn = [x for x in states if x not in s]
new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")

print(states_to_learn)
turtle.mainloop()
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
