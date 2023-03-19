from tkinter import *


def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I'm a label", font=("Arial", 24, "bold"))
my_label["text"] = "new text"
my_label.config(text="New text")
my_label.config(padx=10, pady=10)
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# Button2
button2 = Button(text="Click me", command=button_clicked)
# button.pack()
button2.grid(column=2, row=0)

# Entry
input = Entry()
# input.pack()
input.grid(column=3, row=2)
print(input.get())

window.mainloop()
