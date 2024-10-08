import tkinter
from tkinter import *

import pandas
from PIL import Image, ImageTk
import random
import time
BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title('Flashly')
window.config(pady=20, padx=20, bg=BACKGROUND_COLOR)
window.geometry('496x396')

img_front = (Image.open("./images/card_front.png"))
img_back = (Image.open('./images/card_back.png'))
img_button_left = (Image.open("./images/wrong.png"))
img_button_right = (Image.open("./images/right.png"))

resized_image = img_front.resize((400, 305))
front_image = ImageTk.PhotoImage(resized_image)

resized_image = img_back.resize((400, 305))
back_image = ImageTk.PhotoImage(resized_image)

resized_button_left = img_button_left.resize((50, 50))
new_button_left = ImageTk.PhotoImage(resized_button_left)

resized_button_right = img_button_right.resize((50, 50))
new_button_right = ImageTk.PhotoImage(resized_button_right)

canvas = tkinter.Canvas(window, width=450, height=305, bg=BACKGROUND_COLOR, highlightthickness=0)

random_index = 0
exclude = []

# todo: take out words guessed correctly


def start_card(del_text=0):
    canvas.create_image(220, 150, image=front_image)
    canvas.create_text(220, 150, text="Game Start", fill="black", font=('Helvetica 15 bold'))
    canvas.grid(column=0, row=0, columnspan=1)


def english_card(excl):
    global random_index
    canvas.create_image(220, 150, image=back_image)
    with open('./data/french_words.csv') as words:
        title_word = words.readline()
        title = title_word.split(',')[1]
        word = words.readlines()
        print(word)
    random_index = random.choice([i for i in range(len(word)) if i not in exclude])
    canvas.create_text(220, 100, text=title, fill="black", font=('Helvetica 15 bold'))
    canvas.create_text(220, 130, text=word[random_index].split(',')[1].strip('\n'), fill="black", font=('Helvetica 15 bold'))

    window.after(3000, lambda: french_card(excl))


def french_card(excl):
    global random_index, exclude, to_learn
    if excl == 1:
        exclude.append(random_index)
        print(exclude)
    canvas.create_image(220, 150, image=front_image)
    with open('./data/french_words.csv') as words:
        title_word = words.readline()
        title = title_word.split(',')[0]
        word = words.readlines()

    canvas.create_text(220, 100, text=title, fill="black", font=('Helvetica 15 bold'))
    canvas.create_text(220, 130, text=word[random_index].split(',')[0].strip('\n'), fill="black", font=('Helvetica 15 bold'))

    print(excl)

    group = random.choice([i for i in range(200, 1000) if i not in exclude])


button_left = Button(image=new_button_left, highlightthickness=0, command=lambda: english_card(0), borderwidth=0)
button_left.config(height=50, width=50)
button_left.place(x=97, y=305)
# button_left.grid(column=0, row=1, sticky='w')

button_right = Button(image=new_button_right, highlightthickness=0, command=lambda: english_card(1), borderwidth=0)
button_right.place(x=275, y=305)
# button_right.grid(column=1, row=1)

start_card()

tkinter.mainloop()
