import tkinter
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.geometry('800x526')
my_image = PhotoImage(file="./images/wrong.png")
button = Button(image=my_image, highlightthickness=0)
button.grid()
tkinter.mainloop()
