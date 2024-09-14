import tkinter
from tkinter import *
from PIL import Image, ImageTk
BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title('Flashly')
window.config(pady=20, padx=20, bg=BACKGROUND_COLOR)
window.geometry('496x396')

img_front = (Image.open("./images/card_front.png"))
img_button_left = (Image.open("./images/wrong.png"))
img_button_right = (Image.open("./images/right.png"))

resized_image = img_front.resize((400, 305))
new_image = ImageTk.PhotoImage(resized_image)

resized_button_left = img_button_left.resize((50, 50))
new_button_left = ImageTk.PhotoImage(resized_button_left)

resized_button_right = img_button_right.resize((50, 50))
new_button_right = ImageTk.PhotoImage(resized_button_right)

canvas = tkinter.Canvas(window, width=450, height=305, bg=BACKGROUND_COLOR)


def start_card():
    canvas.create_image(220, 150, image=new_image)
    canvas.create_text(220, 150, text="Game Start", fill="black", font=('Helvetica 15 bold'))
    canvas.grid(column=0, row=0, columnspan=1)


def update_card():
    with open('./data/french_words.csv') as words:
        word = words.readline()
        split = word.split(',')[1]
        print(split)
        canvas.create_text(220, 100, text=split, fill="black", font=('Helvetica 15 bold'))


def red_button():
    update_card()


def green_button():
    pass



button_left = Button(image=new_button_left, highlightthickness=0)
button_left.config(height=50, width=50)
button_left.place(x=97, y=305)
# button_left.grid(column=0, row=1, sticky='w')

button_right = Button(image=new_button_right, highlightthickness=0, command=red_button)
button_right.place(x=275, y=305)
# button_right.grid(column=1, row=1)

start_card()

tkinter.mainloop()
