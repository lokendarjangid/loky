import pyttsx3
import datetime
import speech_recognition as sr 
import platform

class voice:
    def __init__(self) -> None:
        if platform.system() == 'Linux':
            self.engine = pyttsx3.init('nsss')
        elif platform.system() == 'Windows':
            self.engine = pyttsx3.init('sapi5')
        else:
            raise Exception("Unsupported platform")
        voices = self.engine.getProperty('voices')
        # print(voices[3].id)
        self.engine.setProperty('voice', voices[0].id)

    def speak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()
    
    def printandspeak(self,result):
        print(result + "\n")
        self.speak(result)
    
    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            self.speak("Good Morning!")

        elif 12 <= hour < 18:
            self.speak("Good Afternoon!")

        else:
            self.speak("Good Evening!")

        self.speak("I am Loki Sir. Please tell me how may I help you")

    def takeCommand(self):
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
            return command_user

        except Exception:
            # print(e)
            print("Say that again please...")
            self.takeCommand()
        return "None"

    def take_command_start(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("...")
            # r.pause_threshold = 1
            audio = r.listen(source)

        try:
            # print("checking...")
            command_user = r.recognize_google(audio, language='en-in')
            # print(f"User said: {command_user}\n")
            return command_user

        except Exception:
            # print(e)
            self.take_command_start()
        return "None"