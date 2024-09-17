from tkinter import *
from time import *

window= Tk()
#----------
def updateTime():
   timeVar= strftime("%H:%M:%S")
   timeDisplay.config(text=timeVar)
   timeDisplay.after(1000,updateTime)
   #auto update timeDisplay every 1000ms= 1s

    #day
   dayVar= strftime("%A")
   dayDisplay.config(text= dayVar)
    #date
   dateVar = strftime("%B:%d, %Y")
   dateDisplay.config(text=dateVar)
#----------
timeDisplay= Label(window, font=("Arial", 12),
                fg="grey", bg="black")

dayDisplay= Label(window, font=("Arial", 12),
                fg="grey", bg="black")

dateDisplay= Label(window, font=("Arial", 12),
                fg="grey", bg="black")
#----------
timeDisplay.pack()
dayDisplay.pack()
dateDisplay.pack()
#----------
updateTime()
#----------
window.mainloop()
