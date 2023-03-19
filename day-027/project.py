from tkinter import Entry, Label, Button, Tk


def calculate():
    miles = float(entry.get())
    ratio = 1.609344
    km = miles * ratio
    result_label.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=150, width=250)
window.config(padx=20, pady=20)

entry = Entry()
entry.grid(column=1, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=10, pady=10)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=10, pady=10)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

km_label = Label(text="km")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

result_label = Label(text="0")
result_label.grid(column=1, row=1)
result_label.config(padx=10, pady=10)

window.mainloop()
