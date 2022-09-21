from tkinter.ttk  import *
from tkinter import *
from pygame import mixer
from datetime import datetime 
from time import sleep

#redundant time checker to see if the program works 
tim=datetime.now()
hour=tim.strftime("%H")
min=tim.strftime("%M")
sec=tim.strftime("%S")
print(hour,min,sec) 

#window for gui
win=Tk()
win.title("egg")
win.geometry('50x50')


mixer.init()    
alarm()
win.mainloop()
