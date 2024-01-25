from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
french_words = {}

try:
    word_data = pandas.read_csv("data/words_to_learn.csv")
except :
    original_data = pandas.read_csv("data/french_words.csv")
    french_words = original_data.to_dict(orient="records")
else:
    french_words = french_words.to_dict(orient="records")



def on_click():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(french_words)
    canvas.itemconfig(item1, text="French", fill="black")
    canvas.itemconfig(item, text=f'{random_word["French"]}', fill="black")
    canvas.itemconfig(can_img, image=new_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global random_word
    canvas.itemconfig(item1, text="English", fill="white")
    canvas.itemconfig(item, text=f'{random_word["English"]}', fill="white")
    canvas.itemconfig(can_img, image=old_img)


def is_know():
    french_words.remove(random_word)
    data = pandas.DataFrame(french_words)
    data.to_csv("data/words_to_learn.csv", index=False)

    on_click()

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

new_img = PhotoImage(file="./images/card_front.png")
old_img = PhotoImage(file="images/card_back.png")
can_img = canvas.create_image(410, 280, image=new_img)

item1 = canvas.create_text(400, 150, text="", font=('Ariel', 40, 'italic'))
item = canvas.create_text(400, 263, text="", font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2, pady=5, padx=5)

img_right = PhotoImage(file="./images/right.png")
right = Button(image=img_right, highlightthickness=0, command=is_know)
right.grid(row=1, column=0)

img_wrong = PhotoImage(file="./images/wrong.png")
wrong = Button(image=img_wrong, highlightthickness=0, command=on_click)
wrong.grid(row=1, column=1)








on_click()
window.mainloop()
