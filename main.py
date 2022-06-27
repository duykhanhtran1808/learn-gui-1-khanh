from tkinter import *

window = Tk()
window.title("Khanh Company - GUI 1")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label

my_label = Label(text="Welcome to the program. My name is Khanh")
# my_label.pack()
# my_label.place(x=20, y=20)
my_label.grid(column=2, row=0)
# my_label["text"] = "New one"
# my_label.config(text="Newer one")

status_label = Label(text="The result will be shown here")
# status_label.pack()
status_label.grid(column=2, row=4)

# entry

input_field = Entry(width=10)
# input_field.pack()
input_field.grid(column=0, row=2)

# button


def button_clicked():
    input_result = input_field.get()
    status_label.config(text=input_result)


button = Button(text="Hit now", command=button_clicked)
# button.pack()
button.grid(column=1, row=3)

# experiment

window.mainloop()
