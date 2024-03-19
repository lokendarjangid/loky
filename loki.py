import re
import s_functions as sf
import voice_work
import wikipedia  # pip install wikipedia
import webbrowser
import os
import datetime
import requests
import random
from bs4 import BeautifulSoup

voice_p = voice_work.voice()

def commands(command_user):
    prompt_text = str(command_user)
    # Logic for executing tasks based on command_user
    if 'open youtube' in command_user:
        webbrowser.open("youtube.com")

    elif 'open google' in command_user:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in command_user:
        webbrowser.open("stackoverflow.com")

    elif 'open amazon' in command_user:
        webbrowser.open("amazon.com")

    elif 'open flipkart' in command_user:
        webbrowser.open("flipkart.com")

    elif 'open whatsapp' in command_user:
        webbrowser.open("whatsapp.com")

    elif "google" in command_user:
        sf.searchGoogle(command_user)
        
    elif "youtube" in command_user:
        sf.searchYoutube(command_user)
        
    elif "wikipedia" in command_user:
        sf.searchWikipedia(command_user)

    elif 'play music' in command_user:
        music_dir = 'C:\\Users\\Lenovo\\Music'
        songs = os.listdir(music_dir)
        # print(songs)
        os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs))]))

    elif 'the time' in command_user:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        return (f"Sir, the time is {strTime}")

    elif 'open vs code' in command_user:
        codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'random password' in command_user:
        try:
            length = int(re.search(r'\d+', command_user).group())

        except AttributeError:
            length = 8

        password = sf.passwordgenerator(int(length))
        return (f"Your password is {str(password)}")
        
    elif "temperature" in command_user:
        search = "temperature in jaipur"
        url = f"https://www.google.com/search?q={search}"
        r  = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div", class_ = "BNeawe").text
        voice_p.speak(f"current{search} is {temp}")

    elif "weather" in command_user:
        search = "temperature in jaipur"
        url = f"https://www.google.com/search?q={search}"
        r  = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div", class_ = "BNeawe").text
        voice_p.speak(f"current{search} is {temp}")

    elif 'bye' in command_user or 'stop' in command_user or 'exit' in command_user:
        voice_p.printandspeak("Bye Sir, have a good day.")
        exit()

    else :
        voice_p.printandspeak("command not found")

def commander():
    command_user = voice_p.takeCommand().lower()
    result  = commands(command_user)
    try:
        voice_p.printandspeak(result)
    except:
        pass
    print("----------------------------------")


if __name__ == "__main__":
    voice_p.wishMe()
    while True:
        # if 1:
        # loki_listen = voice_p.take_command_start().lower()
        # if "loki" in loki_listen:
        #     voice_p.speak("Yes")
        commander()
        # else:
        #     pass
