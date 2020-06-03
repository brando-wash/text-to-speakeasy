import os
import tkinter as tk
from gtts import gTTS
from playsound import playsound


win = tk.Tk()
win.title("text to speech")
win.geometry("250x70")

def text_to_speech():
    text = entry.get()
    speech = gTTS(text=text, lang="en")
    speech.save(r'C:\Users\Brandon\CODE\python-portfolio\speech.mp3')
    playsound(r'C:\Users\Brandon\CODE\python-portfolio\speech.mp3')
    os.remove(r'C:\Users\Brandon\CODE\python-portfolio\speech.mp3')

label = tk.Label(win,text="Enter Text :")
label.grid(row=0,column=0)

entry = tk.Entry(win)
entry.grid(row=1, column=1)

button = tk.Button(win, text="Go", command=text_to_speech)
button.grid(row=1, column=2)

win.mainloop()