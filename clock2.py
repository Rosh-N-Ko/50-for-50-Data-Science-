import time 
from tkinter import Tk  
from tkinter import Label

'''steps imvolved
1.Make a gui 
2.insert specifications 
pack 
2. get time method 
3.recursion of method
4.call method  
'''

def get_time():
    tim=time.strftime("%I<<%M<<%S<<%p")
    clock.config(text=tim)
    clock.after(2,get_time)


app=Tk()
app.title("hey i  clock also ")
clock=Label(app,font=("Calibri",40),fg="black",bg="pink")
clock.pack()
get_time()
app.mainloop()
