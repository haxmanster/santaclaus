from tkinter import *
from datetime import datetime


def santaclaus():
    today = datetime.today().strftime("%j")
    ending_day_of_current_year = int(datetime.now().date().replace(month=12, day=25).strftime("%j"))
    return ending_day_of_current_year - int(today)

for days in str(santaclaus()):
    print(days[:0])



