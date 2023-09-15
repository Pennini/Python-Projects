from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]

    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password_gen = "".join(password_list)

    password.delete(0, END)
    password.insert(END, string=password_gen)
    pyperclip.copy(password_gen)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    var = [website, email, password]
    new_data = {
        website.get(): {
            "email": email.get(),
            "password": password.get()
        }
    }

    with open("password.json", "w") as file:
        info = ""
        for entry in var:
            value = entry.get()
            if not value:
                messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
                return
            info += value + " | "
        info += "\n"
        
        
        is_ok = messagebox.askokcancel(title=var[0].get(), message=f"These are the details entered:\nE-mail: {var[1].get()}\nPassword: {var[2].get()}\nIs it ok to save?")

        if is_ok:
            json.dump(new_data, file)

            for entry in var:
                if entry == email:
                    continue
                entry.delete(0, END)
            var[0].focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
locker = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website = Entry(width=52)
website.focus()
website.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email = Entry(width=52)
email.insert(END, string="andrepennini@gmail.com")
email.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password = Entry(width=33)
password.grid(column=1, row=3)

generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(column=2, row=3, columnspan=1)

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()