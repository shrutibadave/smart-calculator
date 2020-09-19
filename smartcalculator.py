
#programme of smart calculator

def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def mull(x,y):
    return(x*y)
def div(x,y):
    return(x/y)
m={}
p=0


import pyttsx3
import speech_recognition as sr
from trial3 import predict
engine=pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)


engine.say("Hello,My name is smart calculator")
engine.say("In which way do you want to give input")
print("Hello,My name is smart calculator")
print("In which way do you want to give input")
engine.runAndWait()
print("1.By typing\n2.By speaking")
d=int(input())
if d==1:
    print("Enter operation do you want to perform")
    c=input()
    y=predict(c)
    print(y)
if d==2:


    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("say something.....")
        audio = r.listen(source)
    try:
     text = r.recognize_google(audio)
     m=predict(text)
     engine.say(m)


     engine.runAndWait()

    except Exception:
     engine.say("Something went wrong")






