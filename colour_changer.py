from tkinter import *
from tkinter import messagebox

window = Tk()

window.geometry("900x650")
window.title("Colour Changer")
window.config(background="lightgreen")

title = Label(window, text="Colour Changer", font=("arial", 35), bg="lightgreen")
title.place(x=280, y=30)

enter_colour = Label(window, text="Enter a colour in the box below:", bg="lightgreen", font=("arial", 15))
enter_colour.place(x=150, y=150)

input_colour = Entry(window, width=40, font=("arial", 15))
input_colour.place(x=150, y=180)

colourbox = Listbox(window, width=70, height=18, font=("arial", 10))
colourbox.place(x=150, y=300)

colourbox.insert(END, "red")
colourbox.insert(END, "blue")
colourbox.insert(END, "green")
colourbox.insert(END, "yellow")
colourbox.insert(END, "pink")
colourbox.insert(END, "orange")
colourbox.insert(END, "purple")
colourbox.insert(END, "lightblue")


def add_colour():
    added_colour = input_colour.get()
    colourbox.insert(END, added_colour)
    input_colour.delete(0, END)
    messagebox.showinfo("Colour Added", "Your Colour Has Been Added")


def delete_colour():
    selected_value = colourbox.curselection()
    for i in selected_value:
        colourbox.delete(i)


def change_colour():
    selected_value = colourbox.curselection()
    for i in selected_value:
        chosen_colour = colourbox.get(i)
        window.config(background=chosen_colour)
        title.config(bg=chosen_colour)
        enter_colour.config(bg=chosen_colour)


add_button = Button(window, text="Add", font=("arial", 15), command=add_colour)
add_button.place(x=150, y=230)

delete_button = Button(window, text="Delete", font=("arial", 15), command=delete_colour)
delete_button.place(x=230, y=230)

change_button = Button(window, text="Change Colour", font=("arial", 15), command=change_colour)
change_button.place(x=330, y=230)

window.mainloop()