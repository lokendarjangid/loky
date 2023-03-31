import re
import s_functions
import chatgpt
import voice_work
import wikipedia  # pip install wikipedia
import webbrowser
import os
import datetime
import requests
import random

voice_p = voice_work.voice()
chat = chatgpt.Chatgpt()


def commands(command_user):
    prompt_text = str(command_user)
    # Logic for executing tasks based on command_user
    if 'wikipedia' in command_user:
        voice_p.speak('Searching Wikipedia...')
        command_user = command_user.replace("wikipedia", "")
        results = wikipedia.summary(command_user, sentences=2)
        voice_p.speak("According to Wikipedia")
        return results

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
        # print(songs)
        os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs))]))

    elif 'the time' in command_user:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        return (f"Sir, the time is {strTime}")

    elif 'open code' in command_user:
        codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'random password' in command_user:
        try:
            length = int(re.search(r'\d+', command_user).group())

        except AttributeError:
            length = 8

        password = s_functions.passwordgenerator(int(length))
        return (f"Your password is {str(password)}")

    elif 'bye' in command_user or 'stop' in command_user or 'exit' in command_user:
        voice_p.printandspeak("Bye Sir, have a good day.")
        exit()

    elif 'generate image' in command_user:

        response = chat.generate_image(prompt_text=prompt_text)
        for image in response['data']:
            # print(image['url'])
            img_data = requests.get(image['url']).content
            command_user = command_user.replace("generate image", "")
            if 'of' in command_user:
                command_user = command_user.replace("of", "")
            # os.chdir('images')1
            os.chdir("images")
            fname = os.path.join(os.getcwd(), str(command_user)+'.jpg')
            with open(fname, 'wb') as handler:
                handler.write(img_data)
            os.chdir("..")
            return "Image generated"

    elif 'write code' in command_user or 'write a code' in command_user or 'write program' in command_user:
        response = chat.write_code(prompt_text=prompt_text)

        for choice in response['choices']:
            print(choice['text'])
            return"Here is code"

    else:
        response = chat.text_out(prompt_text=prompt_text)

        for choice in response['choices']:
            voice_p.printandspeak(choice['text'])
            # s_functions.intotxtfile(prompt_text, choice['text'])
            if choice['text'].find('?') != -1:
                commander()
            else:
                pass


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
