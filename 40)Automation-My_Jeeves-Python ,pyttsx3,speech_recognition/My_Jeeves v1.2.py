
'''
This is the explainer version of the project for you 
This project is my simple introduction to automation 
Here I plan to give voice activated commands for my day to day activities 
Possible updates 
a)Custom afternoon , morning and evening messages 
b)sending files tthrough and email 
c)learn more about using smtp and use that to get emails -from specific people 
        or suto reply etc. 
d)fix the wikipedia thing

'''

import speech_recognition as sr
import pyttsx3
import os 
import datetime as dt 
import wikipedia
import webbrowser
import smtplib




#here you are initialising the python engine  
engine=pyttsx3.init('sapi5')
#Here you are loading up the voices part of the library(Using the get function ) 
voices=engine.getProperty('voices')
#Here I am setting up the voice that I want 
engine.setProperty('voice',voices[1].id)

#Here I define a function that will accept my text that I give it  as a parameter And then say it with the help of the inbuilt library And then it it will accept my audio prompt to go ahead   
def talk(speech_text):
    engine.say(speech_text)
    engine.runAndWait()

    
#putting out  a conditional statement to help the bot declare a time 
def greetings():
    tim=dt.datetime.now()
    cur_hour=dt.datetime.now().hour
    hour=int(dt.datetime.now().hour)
    if (hour>12 and hour<18):
            talk('Good afternoon ')
    elif (hour>=18 and hour<=23):
            talk('Good evening')
    elif (hour>12 and hour>18 and hour<=23):
            talk('Congratulations for waking up /staying awake till now .I hope you have a good day .I thank you for your determined direction towards productivity .')
    elif hour<=4:
            talk('It  is late in the night .I hope you go to sleep as soon as possible  ')
    elif hour>4 and hour <12:
            talk('Good morning .It is a beautiful day.')
    else:
        talk('The concept of time has been destroyed.Please report this to the bureau as soon as possible ')         

talk('How may I help you?')    
    

def takecommand():
 #Here the variable input voice will work as the interface between the api and the program     
    a=sr.Recognizer()
#Here I'll set up the microphone as the source of the sound  ,
# tell the user that I'm listening and then store that information as the audio  

    with sr.Microphone() as source:
        print("Listening.... ")
        a.pause_threshold=1
        audio=a.listen(source)

#try to find text equivalents to wht is spoken by interfacing with the Google api and and setting the language as Indian English        
    try:
        print("Processing....")
        command=a.recognize_google(audio ,language='en-in')
        print(f"Is this what you have said:{command=}\n")

    except Exception as ex:
        print("Could you please say that again ")
        return "None" 

    return command 


#Using the smtp-Simple mail text protocol library  , I will send emails with the help of this function 
def send_mail(to,content ,file=0):
#initialise the server with the server number 
    server=smtplib.SMTP('smtp.gmail.com' ,587) 
    server.ehlo()
    server.starttls()
#write your login information 
    server.login('roshan.dan.koshy@gmail.com','mynameajeff69')
    server.login('rosserigert@gmail.com','insert password')
#Invoke the sendmail function  ,with the to emailis and the content set as arguments  
    server.sendmail('roshan.dan.koshy@gmail.com' ,to,content)
    server.close()


#This is the main function for python.When the main function of the program is invoked  , then start the proceedngs of the virtual assistant     
if __name__=='__main__':
    greetings()


    while True:
        command=takecommand().lower()


        if 'who is' in command:
            talk('Searching Wiki')
            command=command.replace("wikipedia"," ")
            results=wikipedia.summary(command,sentences=2)
            talk("According to Wikipedia" )
            print(results)
            talk (results)

        if 'open paint' in command:
            npath="C:\\WINDOWS\\system32\\mspaint.exe"
            os.startfile(npath)


        elif 'open pot' in command:
            npath="C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini64.exe"
            os.startfile(npath)

        elif 'what is the time ' in command:
            tim=dt.datetime.now().strftime("%H:%M:%S")
            talk(f"It is :{tim}")

        elif 'date and time' in command:
                    day=dt.datetime.now().strftime("%A")
                    date=dt.datetime.now().strftime("%e")
                    month=dt.datetime.now().strftime("%B")
                    year=dt.datetime.now().strftime("%Y")
                    
                    talk(f"Today is  :{day} , the {date} of {month} ,{year}")

        elif 'what is the date and time' in command:
                    tim=dt.datetime.now().strftime("%H:%M:%S")
                    talk(f"It is :")

            #https://www.y8.com/games/slope         
            
        elif 'What is the schedule for today' in command :
            pass
        
        elif 'open habitica' in command:
            pass    

            
        else:
            pass          

