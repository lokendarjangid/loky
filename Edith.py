import pyttsx3  # pip install pyttsx3
import main
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import math

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[3].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Edith Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command_user = r.recognize_google(audio, language='en-in')
        print(f"User said: {command_user}\n")

    except Exception:
        # print(e)    
        print("Say that again please...")
        return "None"
    return command_user


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('2022bcaaidslokendar10792@poornima.edu.in', 'poornima777')
    server.sendmail('2022bcaaidslokendar10792@poornima.edu.in', to, content)
    server.close()


def printandspeak(result):
    print(result + "\n")
    speak(result)


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        command_user = takeCommand().lower()

        # Logic for executing tasks based on command_user
        if 'wikipedia' in command_user:
            speak('Searching Wikipedia...')
            command_user = command_user.replace("wikipedia", "")
            results = wikipedia.summary(command_user, sentences=2)
            speak("According to Wikipedia")
            printandspeak(results)

        elif 'open youtube' in command_user:
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

        elif 'play music' in command_user:
            music_dir = 'C:\\Users\\Lenovo\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in command_user:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in command_user:
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email' in command_user:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "amansharma5105Email@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        elif 'add' in command_user:
            split = command_user.split()
            addition = main.addition(int(split[1]), int(split[3]))
            printandspeak(f"The sum is {str(addition)}")

        elif 'subtract' in command_user:
            split = command_user.split()
            substract = main.subtract(int(split[3]), int(split[1]))
            printandspeak(f"The subtraction is {str(substract)}")

        elif 'area of circle' in command_user:
            printandspeak("What is radius of circle")
            radius = takeCommand().lower()
            area = main.area_of_circle(int(radius))
            printandspeak(f"Area of Circle is {str(area)}")

        elif 'perimeter of circle' in command_user:
            printandspeak("What is radius of circle")
            radius = takeCommand().lower()
            perimeter = main.perimeter_of_circle(float(radius))
            printandspeak(f"Perimeter of circle is {str(perimeter)}")

        elif 'factorial' in command_user:
            split = command_user.split()
            value = int(split.index("of")) + 1
            factorial = main.factorial(int(split[value]))
            printandspeak(f"Factorial is {str(factorial)}")

        elif 'square root' in command_user:
            split = command_user.split()
            value = int(split.index("of")) + 1
            square_root = math.sqrt(int(split[value]))
            printandspeak(f"Square root is {str(square_root)}")


        elif 'bye' in command_user:
            break
