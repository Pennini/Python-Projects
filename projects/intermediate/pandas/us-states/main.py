import turtle as tr
import pandas as pd

screen = tr.Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height=600)
image = "blank_states_img.gif"
screen.addshape(image)

tr.shape(image)

# Get the coordinates where you click on the screen
# def get_mouse_click_cor(x, y):
#     print(x, y)

# tr.onscreenclick(get_mouse_click_cor)
# tr.mainloop()

answer_state = screen.textinput(title="Guess the state", prompt="What's the state name you want to try?")
                                
df_states = pd.read_csv("50_states.csv")

answer = answer_state.title()
if answer in list(df_states["state"]):
    x_ans = int(df_states[df_states["state"] == answer]["x"])
    y_ans = int(df_states[df_states["state"] == answer]["y"])
    tr.goto(x_ans, y_ans)
    tr.write(answer, align="center", font=["Arial", 8, "normal"])


screen.exitonclick()
