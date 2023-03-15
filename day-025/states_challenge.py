import turtle
import pandas

FONT = ("Verdana", 8, "normal")

points = 0

screen = turtle.Screen()

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
guessed_states = []

while not points >= 50:
    screen.title(f"{points}/{50} U.S. States Game")
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

    if answer_state.lower() == "exit":
        break

    state_row = data[data["state"].str.casefold() == answer_state.casefold()]
    if len(state_row) == 1:
        points += 1
        turtle_write = turtle.Turtle()
        turtle_write.penup()
        turtle_write.hideturtle()
        turtle_write.goto(float(state_row.x), float(state_row.y))
        turtle_write.write(arg=state_row.state.item(), align="center", font=FONT)
        guessed_states.append(state_row.state.item())

states_to_learn = []
for state in data["state"].to_list():
    if state not in guessed_states:
        states_to_learn.append(state)

pandas.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
