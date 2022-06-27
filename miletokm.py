from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)

# Label

intro_label = Label(text="Enter the value to convert")
intro_label.grid(column=2, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=3, row=1)

desc_label = Label(text="is equal to")
desc_label.grid(column=0, row=2)

result_label = Label(text="0")
result_label.grid(column=2, row=2)

km_label = Label(text="km")
km_label.grid(column=3, row=2)

# entry

input_field = Entry(width=10)
input_field.grid(column=2, row=1)

# button


def button_clicked():
    miles_input = float(input_field.get())
    km_result = 0
    if miles_input > 0:
        km_result = round(miles_input * 1.60934, 2)
    result_label.config(text=km_result)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)


# Open window
window.mainloop()
