from tkinter import *
from time import *

def update():
    timeString = strftime("%I:%M:%S %p")
    timeLabel.config(text=timeString)

    dayString = strftime("%A")
    dayLabel.config(text=dayString)

    dateString = strftime("%B %d %Y")
    dateLabel.config(text=dateString)

    window.after(1000,update)

window = Tk()

window.title("Clock using Python | by: Sophia Nicole Garcia")
window.config(background="pink")

timeLabel = Label(window,font=("Arial",50), fg="green",bg="pink")
timeLabel.pack()

dayLabel = Label(window,font=("Ink Free",25),bg="pink")
dayLabel.pack()

dateLabel = Label(window,font=("Ink Free",30),bg="pink")
dateLabel.pack()

update()

window.mainloop()