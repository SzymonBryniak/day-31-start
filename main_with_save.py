import tkinter
from tkinter import *
from PIL import Image, ImageTk
import random
import pandas
import time
import pandas
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

counter_english = [0]
counter_french = [0]
random_index = 0
exclude = []
to_learn = {}
load_words = './data/french_words.csv'
# to_learn.csv can be loaded by replacing the file path
# in the "load_words" variable with the file path of the to_lear.csv.



try:
    to_learn_df = pandas.read_csv('./data/to_learn.csv', index_col=0)
    # to_learn_df = to_learn_df.loc[:, ~to_learn_df.columns.str.contains('^Unnamed')]
except FileNotFoundError:
    to_learn_df = pandas.DataFrame({'French': {}, 'English': {}, 'Index': {}})


def start_card(del_text=0):
    canvas.create_image(220, 150, image=front_image)
    canvas.create_text(220, 150, text="Game Start", fill="black", font=('Helvetica 15 bold'))
    canvas.grid(column=0, row=0, columnspan=1)


def english_card(excl):
    global counter_english, random_index
    canvas.create_image(220, 150, image=back_image)
    with open(load_words) as words:
        title_word = words.readline()
        title = title_word.split(',')[1]
        word = words.readlines()
    random_index = random.choice([i for i in range(len(word)) if i not in to_learn_df])
    random_word_to_exclude = word[random_index]
    random_word = random_word_to_exclude.split(',')[1].strip('\n')

    canvas.create_text(220, 100, text=title, fill="black", font=('Helvetica 15 bold'))
    canvas.create_text(220, 130, text=random_word, fill="black", font=('Helvetica 15 bold'))

    french_word_to_learn = random_word_to_exclude.strip('\n').split(',')[0]
    english_word_to_learn = random_word_to_exclude.strip('\n').split(',')[1]
    to_learn_df.loc[len(exclude), 'French'] = french_word_to_learn
    to_learn_df.loc[len(exclude), 'English'] = english_word_to_learn
    to_learn_df.loc[len(exclude), 'Index'] = int(random_index)

    if excl == 1:
        to_learn_df.drop(index=to_learn_df.index[-1], axis=0, inplace=True)
    to_learn_df.to_csv('./data/to_learn.csv', index=False)  # option index=False will save the file without the index column.
    window.after(3000, lambda: french_card())


def french_card():
    global counter_french, random_index, exclude, to_learn_df
    canvas.create_image(220, 150, image=front_image)
    with open(load_words) as words:
        title_word = words.readline()
        title = title_word.split(',')[0]
        word = words.readlines()
        word_object = word[random_index].split(',')[0].strip('\n')
        exclude.append(random_index)
    canvas.create_text(220, 100, text=title, fill="black", font=('Helvetica 15 bold'))
    canvas.create_text(220, 130, text=word_object, fill="black", font=('Helvetica 15 bold'))


button_left = Button(image=new_button_left, highlightthickness=0, command=lambda: english_card(0), borderwidth=0)
button_left.config(height=50, width=50)
button_left.place(x=97, y=305)
button_right = Button(image=new_button_right, highlightthickness=0, command=lambda: english_card(1), borderwidth=0)
button_right.place(x=275, y=305)


start_card()
tkinter.mainloop()
