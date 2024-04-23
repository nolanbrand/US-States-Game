from turtle import Turtle


class Printed_State_Name(Turtle):
    def __init__(self, correct_state, state_x, state_y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(state_x, state_y)
        self.write(correct_state)

