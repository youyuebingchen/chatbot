import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import sys


# 让AI讲话
def speak(str):
    print(str)
    tts = gTTS(text=str,lang="en")
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def recordaudio():
    # 记录下音频
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    # 用google api转化音频
    data= ""
    try:
        data = r.recognize_google(audio)
        print("you said:"+data)
    except sr.UnknowValueError:
        print("google speech could not understand audio")
    except sr.reguestError as e:
        print("could not request results fron google speech recognition service:{0}".format(e))
    return data

def jarvis():
    while True:
        data = recordaudio()
        if "how are you" in data:
            speak("I am fine")
        if "what time is it" in data:
            speak(ctime())
        if "where is" in data:
            data =data.split(" ")
            location = data[2]
            speak("Hold on tony, I will show you where"+location+"is")
            os.system("open -a safari http://www.google.com/maps/place/"+location+"/&amp;")
        if "bye" in data:
            speak("bye bye")
            break
time.sleep(2)
speak("hi tony, what can i do for you ?")
jarvis()

