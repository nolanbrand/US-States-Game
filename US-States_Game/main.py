import turtle
import pandas
from printed_state_name import Printed_State_Name

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

states_data = pandas.read_csv('50_states.csv')

user_correct_list = []
user_needed_states_list = []
game_continue = True
while game_continue:
    answer_state = screen.textinput(title=f'{len(user_correct_list)}/50 States Correct',
                                    prompt='Write a State name: ').title()

    if answer_state == "Exit":
        for i in range(len(states_data)):
            if states_data.state[i] not in user_correct_list:
                user_needed_states_list.append(states_data.state[i])

        break

    for i in range(len(states_data)):
        if answer_state in user_correct_list:
            continue
        if answer_state == states_data.state[i]:
            user_correct_list.append(answer_state)
            printed_state_name = Printed_State_Name(states_data.state[i], states_data.x[i], states_data.y[i])

    if len(user_correct_list) == 50:
        end_text = Printed_State_Name('ALL 50 STATES GUESSED CORRECTLY!!', 0, 350)

missing_states_dict = {
    "Missing States": user_needed_states_list
}

missing_states_df = pandas.DataFrame(missing_states_dict)

missing_states_df.to_csv('Remaining_States.csv')
