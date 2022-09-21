from threading import Thread
from tkinter.ttk import *
from tkinter import *
from datetime import time 
from datetime import datetime 
from pygame import mixer
from time import sleep 
from PIL import Image, ImageTk

#colours
col1="#000000"
col2="#FF0000"
col3="#FFFFFF"

#window 
window=Tk()
window.title("Nightowl the clock ")
window.geometry('350x250')

#frame line
fr_line1=Frame(window,height=1,width=400, bg=col1)
fr_line1.grid(row=0,column=0)

fr_body=Frame(window,height=300,width=400,bg=col1)
fr_body.grid(row=1,column=0)


#image 
img=Image.open('icons8-owl-100.png')
img.resize((100,100))
img=ImageTk.PhotoImage(img)
fram_img=Label(fr_body,height=100,width=100,image=img,bg=col1)
fram_img.place(x=10,y=20)

#Alarm Label
alarm=Label(fr_body,text="Alarm",font=('Arial 25 bold'),fg=col2,bg=col1)
alarm.place(x=115,y=25)


#Hours
Hour=Label(fr_body,text="Hours",font=('Arial,7'),fg=col3,bg=col1)
Hour.place(x=115,y=70)
roll_h=Combobox(fr_body,height=5,width=5,font=('arial 10'))
roll_h.place(x=116,y=100)
roll_h['values']=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
roll_h.current(0)

#Minutes 
minute=Label(fr_body,text="minutes",font=('Arial,7'),fg=col3,bg=col1)
minute.place(x=175,y=70)
roll_m=Combobox(fr_body,height=5,width=5,font=('arial 10'))
roll_m.place(x=180,y=100)
roll_m['values']=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
roll_m.current(0)

#seconds 
seconds=Label(fr_body,text="seconds",font=('Arial,7'),fg=col3,bg=col1,padx=2)
seconds.place(x=245,y=70)
roll_s=Combobox(fr_body,height=5,width=5,font=('arial 10'))
roll_s.place(x=250,y=100)
roll_s['values']=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
roll_s.current(0)

def activate():
    t=Thread(target=alarm)
    t.start()
    
def deactivate ():
    print("deactivated",op.get())
    mixer.music.stop()
    op.set(0)
    
op=IntVar()

#activation button
rb1=Radiobutton(fr_body,value=1,fg=col2,font=('calibri 12 bold'),bg=col1,text="On",command=activate,variable=op )
rb1.place(x=116,y=170)




#sound player 
def sound():
    mixer.music.load('egg.mp3')
    mixer.music.play()
    op.set(0)
    #deactivation button 
    rb2=Radiobutton(fr_body,value=1,fg=col2,font=('calibri 12 bold'),bg=col1,text="Off",command=deactivate,variable=op )
    rb2.place(x=170 ,y=170)




#logic of the alarm 
def alarm():
    while(True):
        ctr=op.get()
        mh =roll_h.get()
        mm=roll_m.get()
        ms=roll_s.get()
        
        tim=datetime.now()
        hour=tim.strftime("%H")
        min=tim.strftime("%M")
        sec=tim.strftime("%S")
    
        if(ctr==1):
            print(op)
            if( mh==hour):
                if(mm==min):
                    if(ms==sec):
                        sound()
                        print("time has passed")    
            
        sleep(1)            
window.resizable(False,False)
mixer.init()
window.mainloop()

