from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
word_french = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except:
    data = pd.read_csv("data/french_words.csv")

words_dict = data.to_dict(orient="records")

def know():
    global word_french
    try:
        words_dict.remove(word_french)
    except ValueError:
        canvas.itemconfig(language, fill="black", text="Congratulations!")
        canvas.itemconfig(word, fill="black", text="")
        canvas.itemconfig(canvas_image, image=card_front)
    else:
        words_to_learn = pd.DataFrame(words_dict)
        words_to_learn.to_csv("data/words_to_learn.csv", index=False)
        random_word()


def random_word():
    global word_french, flip_timer
    window.after_cancel(flip_timer)
    word_french = random.choice(words_dict)
    canvas.itemconfig(language, fill="black", text="French")
    canvas.itemconfig(word, fill="black", text=word_french["French"])
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(language, fill="white", text="English")
    canvas.itemconfig(word, fill="white", text=word_french["English"])
    canvas.itemconfig(canvas_image, image=card_back)

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
word = canvas.create_text(400, 263, text="", fill="black", font=(FONT, 60, "bold"))
language = canvas.create_text(400, 150, text="", fill="black", font=(FONT, 40, "italic"))
canvas.grid(column=0, row=0, columnspan=2)


right_img = PhotoImage(file="./images/right.png")
right = Button(image=right_img, highlightthickness=0, command=know)
right.grid(column=1, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_img, highlightthickness=0, command=random_word)
wrong.grid(column=0, row=1)

random_word()

window.mainloop()