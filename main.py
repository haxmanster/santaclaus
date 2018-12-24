import datetime
today = datetime.date.today().strftime("%j")
day = int(today)
dedline = 359 - day
print("Santa Claus time ", dedline, " days left :]")
