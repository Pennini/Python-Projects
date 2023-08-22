from tkinter import *

screen = Tk()
screen.config(padx=20, pady=20)
screen.title("Mile to Km converter")

miles = Entry(width=10)
miles.grid(column=1, row=0)
miles.insert(END, string="0")

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

km = Label(text="0")
km.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def calculate():
    miles_get = int(miles.get())
    km_converter = str(round(miles_get * 1.60934, 1)).replace(".", ",")
    km.config(text=km_converter)


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


screen.mainloop()
