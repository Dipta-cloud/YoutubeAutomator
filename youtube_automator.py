from tkinter import *
from PIL import Image,ImageTk
import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import os
import pyautogui
import webbrowser



def onclick():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 180)

    def speak(audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()

    def take_command():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=300, phrase_time_limit=5)

            try:
                print("Recognising.....")
                text = r.recognize_google(audio, language="en-in")
                print(f"User Said {text}")

            except Exception as e:
                # speak("Say That Again Please....")
                return "none"
            return text

    def wish_me():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour <= 12:
            speak("Good morning")
        elif hour >= 12 and hour <= 16:
            speak("Good afternoon")
        else:
            speak("Good evening")
        speak("I am melody , Please tell me the song you want to hear")

    if __name__ == "__main__":
        wish_me()
        while True:
            text = take_command().lower()
            if "play" in text:
                song = text.replace("play", '')
                speak("playing" + song)
                pywhatkit.playonyt(song)
            elif "close" in text:
                speak("closing")
                os.system("taskkill/f /im chrome.exe")
            elif "pause it" in text:
                pyautogui.click(505, 320, 1)
            elif "start" in text:
                pyautogui.click(505, 320, 1)
            elif "goodbye" in text:
                speak("bye sir, hope to assist you soon,take care")
                quit()
def onclick2():
    webbrowser.open_new(r'c:\Users\hp\Desktop\My_App\instructions.pdf')


root = Tk()
root.title("Desi Tech")
root.geometry('700x500')
load = Image.open('d1.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root, image = render)
img.place(x=0, y=0)
img1 = PhotoImage(file='start.png')
b = Button(root, image = img1, bd=0, bg = "#F5F5F5", activebackground = "#F5F5F5", command=onclick )
b.place(x=405, y=200)
img2 = PhotoImage(file='USER GUIDE.png')
b1 = Button(root, image = img2, bd=0, bg = "#F5F5F5", activebackground = "#F5F5F5", command=onclick2 )
b1.place(x=198, y=200)
img3 = PhotoImage(file='YouTube-Automator.png')
b2 = Button(root, image = img3, bd=0, bg = "#F5F5F5", activebackground = "#F5F5F5" )
b2.place(x=50, y=400)
img4 = PhotoImage(file='Desi-Tech.png')
b3 = Button(root, image = img4, bd=0, bg = "#F5F5F5", activebackground = "#F5F5F5" )
b3.place(x=150, y=0)
root.mainloop()








