# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import Canvas, PhotoImage, Tk

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

photo_image = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=photo_image)
canvas.pack()

window.mainloop()
