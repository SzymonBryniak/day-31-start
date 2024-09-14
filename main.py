import tkinter
from tkinter import *
from PIL import Image, ImageTk
import time
BACKGROUND_COLOR = "#B1DDC6"


class FlashCards(tkinter.Tk):
    img_front = (Image.open("./images/card_front.png"))
    img_button_left = (Image.open("./images/wrong.png"))
    img_button_right = (Image.open("./images/right.png"))
    resized_front = img_front.resize((400, 305))
    resized_button_left = img_button_left.resize((50, 50))
    resized_button_right = img_button_right.resize((50, 50))

    def __init__(self):
        super().__init__()
        # self.window = Tk()
        self.title('Flashly')
        self.config(pady=20, padx=20, bg=BACKGROUND_COLOR)
        self.geometry('496x396')
        self.new_image = ImageTk.PhotoImage(self.resized_front)
        self.new_button_left = ImageTk.PhotoImage(self.resized_button_left)
        self.new_button_right = ImageTk.PhotoImage(self.resized_button_right)
        self.canvas = tkinter.Canvas()
        self.start_front()
        self.red_button()
        self.green_button = Button(image=self.new_button_right, highlightthickness=0, command=print('test'))
        self.green_button.place(x=275, y=305)
        self.update_card()
        self.mainloop()

    def update_card(self):
        with open('./data/french_words.csv') as words:
            headings = words.readline()
            heading_french = headings.split(',')[0]
            heading_english = headings.split(',')[1]
            self.canvas.create_text(220, 100, text=heading_french, fill="black", font=('Helvetica 15 bold'))
            self.canvas.create_text(220, 150, text=heading_french, fill="black", font=('Helvetica 15 bold'))
        return self

    def start_front(self):
        with open('./data/french_words.csv') as words:
            headings = words.readline()
            heading_french = headings.split(',')[0]
            heading_english = headings.split(',')[1]
            self.canvas.create_text(220, 100, text=heading_french, fill="black", font=('Helvetica 15 bold'))
            self.canvas.create_text(220, 150, text=heading_french, fill="black", font=('Helvetica 15 bold'))
        canvas = tkinter.Canvas(width=450, height=305, bg=BACKGROUND_COLOR)
        canvas.create_image(220, 150, image=self.new_image)
        text1 = canvas.create_text(220, 150, text="HELLO WORLD", fill="black", font=('Helvetica 15 bold'))
        canvas.grid(column=0, row=0, columnspan=1)
        return self

    def red_button(self):
        self.update_card()
        button_left = Button(image=self.new_button_left, highlightthickness=0)
        button_left.config(height=50, width=50)
        button_left.place(x=97, y=305)
        # button_left.grid(column=0, row=1, sticky='w')
        return self

    def green_button(self):
        button_right = Button(image=self.new_button_right, highlightthickness=0, command=self.update_card)
        button_right.place(x=275, y=305)
        # button_right.grid(column=1, row=1)
        return self


game_start = FlashCards()

