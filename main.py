import tkinter

window = tkinter.Tk()
window.title("Khanh Company - GUI 1")
window.minsize(width=800, height=500)

# label

my_label = tkinter.Label(text="Welcome to the program. My name is Khanh", font=("Arial", 24, "bold"))
my_label.pack(side="left")

# experiment

window.mainloop()
