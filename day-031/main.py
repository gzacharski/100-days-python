from tkinter import Tk, PhotoImage, Button, Canvas

BACKGROUND_COLOR = "#B1DDC6"


def button_clicked():
    print("Button was clicked")


window = Tk()
window.title("Flashy")
window.configure(pady=50, padx=50, background=BACKGROUND_COLOR)

card_image = PhotoImage(file="images/card_front.png")
canvas = Canvas(height=526, width=800, background=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 260, image=card_image)
canvas.create_text(400, 160, text="title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 253, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
button_right = Button(image=right_image, highlightthickness=0, command=button_clicked)
button_right.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0, command=button_clicked)
button_wrong.grid(row=1, column=0)

window.mainloop()
