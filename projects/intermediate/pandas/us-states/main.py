import turtle as tr
import pandas as pd

screen = tr.Screen()
screen.title("U.S. States Game")
screen.setup(width=700, height=500)
screen.tracer(0)
turtle = tr.Turtle()
turtle.penup()
turtle.hideturtle()

image = "blank_states_img.gif"
screen.addshape(image)

tr.shape(image)

# Get the coordinates where you click on the screen
# def get_mouse_click_cor(x, y):
#     print(x, y)

# tr.onscreenclick(get_mouse_click_cor)
# tr.mainloop()
df_states = pd.read_csv("50_states.csv")
lenght_game = len(df_states["state"])
count = 0
is_game_on = True
while is_game_on:
    screen.update()
    answer_state = screen.textinput(title="Guess the state", prompt="What's the state name you want to try?")
    answer = answer_state.title()

    if answer in list(df_states["state"]):
        count += 1
        state = df_states[df_states["state"] == answer]
        x_ans = int(state["x"])
        y_ans = int(state["y"])
        turtle.goto(x_ans, y_ans)
        turtle.write(answer, align="center", font=["Arial", 8, "normal"])

    if count == lenght_game:
        turtle.goto(-25,200)
        turtle.write("Congratulations, you've won", align="center", font=["Arial", 30, "normal"])
        is_game_on = False


screen.exitonclick()
