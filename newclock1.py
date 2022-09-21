from calendar import month
import time
from tkinter import*
import pyglet
from datetime import datetime 
import time 
pyglet.font.add_file('digital-7.ttf')
pyglet.font.add_file('degrassi front.TTF')
pyglet.font.add_file('degrassi back.TTF')
fc="#f900b7"
bc="#185bf7"
local_time = time.localtime()

def get_tiem():
    tim=datetime.now()
    timee=tim.strftime("%I:%M:%S  %p:")
    weekday=tim.strftime("%A")
    day=tim.day
    date=tim.date
    month=tim.strftime("%b")
    year=tim.strftime("%Y")
    
 
 #   year=local_time.tm_year
  #  day=local_time.tm_mday
   # number=local_time.tm_yday
    #month=local_time.tm_mon
    l1.config(text=timee)
    l1.after(200,get_tiem)
    l2.config(text=weekday + "  "+ str(day) + "/" +str(month)+" / "+ str(year))






win=Tk()
win.title("hey this is a  title")
win.geometry('510x150')
win.configure(bg="black")



l1=Label(font=("digital-7 85"),bg="black",fg=fc)
l1.pack()
l1.grid(row=0,column=0,sticky=NW)
l2=Label(text=" Sat,Sep,29",font=("digital-7 15"),bg="black",fg=fc,padx=5)
l2.grid(row=1,column=0,sticky=NW)

get_tiem()








win.resizable(width=False,height=False)
win.mainloop()