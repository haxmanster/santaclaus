from tkinter import *
from datetime import datetime


def santaclaus():
    today = datetime.today().strftime("%j")
    ending_day_of_current_year = int(datetime.now().date().replace(month=12, day=24).strftime("%j"))
    return ending_day_of_current_year - int(today)


def pushit():
    napis = Label(window, text=santaclaus(), width=40, height=4, font=("Helvetica", 32), foreground="purple")
    if santaclaus() == 0:
        napis = Label(window, text="!!! MIKOŁAJ !!!", width=40, height=4, font=("Helvetica", 32), foreground="purple")
    napis.pack()
    button['bg'] = 'red'   #
    button['fg'] = 'white'  #


window = Tk()
window.geometry('300x150')
button = Button(window, text='Ile dni zostalo do mikolaja ?', command=pushit)
button.pack()  # wyświetlam przycisk

window.mainloop()
