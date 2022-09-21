from tkinter import Tk
from tkinter import Label
import time 
'''tkinter is used to make guis ,tk from tkinter makes a seperate window and label helps you display stuff
tkinter needs to run on a loop to stay on 
'''
sus=Tk()#run the program once 
sus.title("Hi i'm a new clock")

def get_time():
    tim=time.strftime("%I:%M:%S %p")
    clock.config(text=tim)
    clock.after(2,get_time)
    




clock=Label(sus,font=("Comic Sans",90),bg="black",fg="red")
clock.pack() 
get_time()

sus.mainloop()#run it multiple times 

