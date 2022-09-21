from tkinter import Tk
from tkinter import Label
import time 

def get_time():
    tim=time.strftime("%I:%M:%S  %p")
    clock.config(text=tim)
    clock.after(5,get_time)
    
    
main=Tk()
main.title("hi i CLOCK ")
clock=Label(main,font=("Baskerville",70),fg="pink",bg="black")
clock.pack()
get_time()
main.mainloop()