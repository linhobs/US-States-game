import pandas as pd
import turtle

# // screen setup
screen = turtle.Screen()
screen.title("U.S State Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
guessed_states = []
states_to_learn = []
# getting hold of csv Data
state_data = pd.read_csv("50_states.csv")
state_list = state_data.state.to_list()
# user input'
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 states guessed", prompt="Guess a state name")
    cleaned_answer = answer.title()
    # check if answer is in list of states
    if cleaned_answer == "Exit":
        for state in state_list:
            if state not in guessed_states:
                states_to_learn.append(state)
        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    if cleaned_answer in state_list:
        # go to that location and write state name
        guessed_states.append(cleaned_answer)
        guessed_state = state_data[state_data.state == cleaned_answer]
        name = turtle.Turtle()
        name.hideturtle()
        name.penup()
        name.goto(int(guessed_state.x), int(guessed_state.y))
        name.write(cleaned_answer, align='center')
turtle.mainloop()
