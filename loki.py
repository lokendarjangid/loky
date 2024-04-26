import re
import s_functions as sf
from flask import Flask, render_template, request, redirect, session
import voice_work
import webbrowser
import os
from keyboard import volumeup,volumedown
import datetime
import requests
import mixer
from NewsRead import latestnews
import pyautogui
import speedtest
from Dictapp import openappweb, closeappweb
from bs4 import BeautifulSoup

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

voice_p = voice_work.voice()

def commands(command_user):
    prompt_text = str(command_user)

    # open commands
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
    
    elif "open" in command_user:
        openappweb(command_user)

    elif "close" in command_user:
        closeappweb(command_user)   
        
    elif "wikipedia" in command_user:
        sf.searchWikipedia(command_user)

    # play,pause,mute,volume increase and decrease youtube
    elif "pause" in command_user:
        pyautogui.press("k")
        voice_p.speak("video paused")

    elif "play" in command_user:
        pyautogui.press("k")
        voice_p.speak("video played")

    elif "mute" in command_user:
        pyautogui.press("m")
        voice_p.speak("video muted")

    elif "volume up" in command_user:
        voice_p.speak("Turning volume up,sir")
        volumeup()

    elif "volume down" in command_user:
        voice_p.speak("Turning volume down, sir")
        volumedown()

    # reminder of anything
    elif "remember that" in command_user:
        rememberMessage = command_user.replace("remember that","")
        rememberMessage = command_user.replace("jarvis","")
        voice_p.speak("You told me to remember that"+rememberMessage)
        remember = open("Remember.txt","a")
        remember.write(rememberMessage)
        remember.close()

    elif "what do you remember" in command_user:
        remember = open("Remember.txt","r")
        voice_p.speak("You told me to remember that" + remember.read())

    # read new 
    elif "news" in command_user:
        latestnews()
    
    # calculator
    elif "calculate" in command_user:
        from Calculatenumbers import WolfRamAlpha
        from Calculatenumbers import Calc
        command_user = command_user.replace("calculate","")
        command_user = command_user.replace("jarvis","")
        Calc(command_user)
    
    # send whatsapp message to anyone
    elif "whatsapp" in command_user:
        from Whatsapp import sendMessage
        sendMessage()

    elif 'the time' in command_user:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        return (f"Sir, the time is {strTime}")

    # genereate random passoword for privacy
    elif 'random password' in command_user:
        try:
            length = int(re.search(r'\d+', command_user).group())

        except AttributeError:
            length = 8

        password = sf.passwordgenerator(int(length))
        return (f"Your password is {str(password)}")
    
    # give tempature of jaipur
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
    
    # shutdown the system
    elif "shutdown the system" in command_user:
        voice_p.speak("Are You sure you want to shutdown")
        shutdown = input("Do you wish to shutdown your computer? (yes/no)")
        if shutdown == "yes":
            os.system("shutdown /s /t 1")
        elif shutdown == "no":
            pass
    
    # schedule the day
    elif "schedule my day" in command_user:
        tasks = [] #Empty list 
        voice_p.speak("Do you want to clear old tasks (Plz speak YES or NO)")
        command_user = voice_p.takeCommand().lower()
        if "yes" in command_user:
            file = open("tasks.txt","w")
            file.write(f"")
            file.close()
            no_tasks = int(input("Enter the no. of tasks :- "))
            i = 0
            for i in range(no_tasks):
                tasks.append(input("Enter the task :- "))
                file = open("tasks.txt","a")
                file.write(f"{i}. {tasks[i]}\n")
                file.close()
        elif "no" in command_user:
            i = 0
            no_tasks = int(input("Enter the no. of tasks :- "))
            for i in range(no_tasks):
                tasks.append(input("Enter the task :- "))
                file = open("tasks.txt","a")
                file.write(f"{i}. {tasks[i]}\n")
                file.close()
    
    elif "show my schedule" in command_user:
        file = open("tasks.txt","r")
        content = file.read()
        file.close()
        mixer.init()
        mixer.music.load("notification.mp3")    
        mixer.music.play()
        notification.notify(
            title = "My schedule :-",
            message = content,
            timeout = 15
            )

    #  open any app function
    elif "open" in command_user:   #EASY METHOD
        command_user = command_user.replace("open","")
        command_user = command_user.replace("jarvis","")
        pyautogui.press("super")
        pyautogui.typewrite(command_user)
        pyautogui.sleep(2)
        pyautogui.press("enter")   
    
    # Internet speed test
    elif "internet speed" in command_user:
        wifi  = speedtest.Speedtest()
        upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
        download_net = wifi.download()/1048576
        print("Wifi Upload Speed is", upload_net)
        print("Wifi download speed is ",download_net)
        voice_p.speak(f"Wifi download speed is {download_net}")
        voice_p.speak(f"Wifi Upload speed is {upload_net}")
    
    # IPL score
    elif "ipl score" in command_user:
        from plyer import notification  #pip install plyer
        url = "https://www.cricbuzz.com/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text,"html.parser")
        team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
        team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
        team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
        team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

        a = print(f"{team1} : {team1_score}")
        b = print(f"{team2} : {team2_score}")

        notification.notify(
            title = "IPL SCORE :- ",
            message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
            timeout = 15
        )
    
    # game rock paper scissor
    elif "play a game" in command_user:
        from game import game_play
        game_play()

    # take screenshot
    elif "screenshot" in command_user:
        im = pyautogui.screenshot()
        im.save("ss.jpg")
    
    # click my picture
    elif "click my photo" in command_user:
        pyautogui.press("super")
        pyautogui.typewrite("camera")
        pyautogui.press("enter")
        pyautogui.sleep(2)
        voice_p.speak("SMILE")
        pyautogui.press("enter")

    # translator function
    elif "translate" in command_user:
        from Translator import translategl
        command_user = command_user.replace("jarvis","")
        command_user = command_user.replace("translate","")
        translategl(command_user)

    # exit the program
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


def alarm(command_user):
    '''This is alarm function for alarm to active.'''
    timehere = open("Alarmtext.txt","a")
    timehere.write(command_user)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    app = Flask(__name__)
    app.secret_key = "433e732fe46eb93bed8f0392"
    @app.route('/', methods=['GET', 'POST'])
    def main():
        if request.method == 'POST':
            task_content = request.form['ask']
            try:
                return redirect('/')
            except:
                return 'There was an issue connecting to Gemini.'
        else:
            return render_template('index.html')
    voice_p.wishMe()
    while True:
        commander()
