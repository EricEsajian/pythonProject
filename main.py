import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

import turtle

tim = turtle.Turtle()
tim.write("Some Text", font=("Times New Roman", 80, "bold"))

window.mainloop()