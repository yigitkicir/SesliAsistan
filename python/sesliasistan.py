
from encodings import utf_8
import re
from tracemalloc import stop
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice
import webbrowser
import numpy as np
import cv2

r = sr.Recognizer()
def record(ask=False):
    with sr.Microphone() as source:
        if(ask):
                print(ask)    
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            speak(" Anlayamadım")
        except sr.RequestError:
            speak(" Sistem çalışmıyor")
        return voice
        
        



def response(voice):
        
    if "merhaba" in voice:
        speak("merhaba patron")
    if "nasılsın" in voice:
        speak("işe hazırım")


#sistem kapatma        
    if "sistemi kapat" in voice:
        speak("iyi günler")
        exit()      

#Hanhi günde olduğumuz
    if "hangi gündeyiz" in voice:
     
        today=time.strftime("%A")
        today.capitalize()
        if today=="Monday":
            today="Pazartesi"

        elif today=="Tuesday":
                today="Salı"
        
        elif today=="Wednesday":
                today="Çarşamba"

        elif today=="Thursday":
                today="Perşembe"

        elif today=="Friday":
                today="Cuma"

        elif today=="Saturday":
                today="Cumartesi"

        elif today=="Sunday":
                today="Pazar"  
        speak(today)
        print(today)
      
#Saatin kaçı gösterdiği               

    if  "saat kaç"  in voice:
        selection=["Saat şuan:","Saat tam"]
        clock=datetime.now().strftime("%H:%M") 
        selection=random.choice(selection)
        speak(selection+clock)    

#Googleda arama
    if "google'da ara" in voice:
        speak("Ne aramamı istersin")
        search=record()
        url="https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} İçin bulduğum arama sonuçları".format(search))

#Not etme
    if"not et" in voice:
        speak("dosya ismi ne olsun")
        txtfile=record()+".txt"
        speak("ne kaydetmek istiyorsun")
        thetext=record()
        f=open(txtfile, "w", encoding="utf_8")
        f.writelines(thetext)
        f.close()
#Kamera
    if "kamera"in voice:
        os.system('sudo modprobe bcm2835-v412')
        kamera=cv2.VideoCapture(0)
        while True:
            tf,görüntü=kamera.read()
            cv2.imshow('Görüntü',görüntü)
            if cv2.waitKey(25) & 0xFF==ord('ç'):
                    break


    
   
            




def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    # speeding()
    playsound(file)
    os.remove(file)

#Uyandırma
def test (wake):
    if "arthur" in wake:
        speak("dinliyorum")
        wake =record()
        if wake!='':
         voice=wake.lower()
         print(wake.capitalize())
         response(voice)




while True:
    wake = record()
    if wake != '':
        wake=wake.lower()
        print(wake.capitalize())       
        test(wake)


