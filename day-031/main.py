from tkinter import Tk, PhotoImage, Button, Canvas
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

word_dict = {}
task_id = ""
data_frame = None


def known_word():
    word_list.remove(word_dict)
    updated_data_frame = pandas.DataFrame.from_records(word_list)
    updated_data_frame.to_csv("data/words_to_learn.csv", index=False)

    next_card()


def next_card():
    global word_dict, task_id
    if not task_id == "":
        window.after_cancel(task_id)

    word_dict = random.choice(word_list)
    french_word = word_dict.get("French")

    canvas.itemconfig(card_background, image=card_image_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")

    task_id = window.after(3000, flip_the_card)


def flip_the_card():
    english_word = word_dict.get("English")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")
    canvas.itemconfig(card_background, image=card_image_back)


try:
    data_frame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_frame = pandas.read_csv("data/french_words.csv")
finally:
    word_list = data_frame.to_dict(orient="records")

window = Tk()
window.title("Flashy")
window.configure(pady=50, padx=50, background=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, background=BACKGROUND_COLOR, highlightthickness=0)
card_image_front = PhotoImage(file="images/card_front.png")
card_image_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 260, image=card_image_front)
card_title = canvas.create_text(400, 160, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 253, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
button_right = Button(image=right_image, highlightthickness=0, command=known_word)
button_right.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)

next_card()

window.mainloop()
