import random
import string
import voice_work
import pywhatkit
import webbrowser
import wikipedia

voice_p = voice_work.voice()
def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        voice_p.speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            voice_p.speak(result)

        except:
            voice_p.speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        voice_p.speak("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        voice_p.speak("Done, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        voice_p.speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query,sentences = 2)
        voice_p.speak("According to wikipedia..")
        print(results)
        voice_p.speak(results)

# password_generator

def passwordgenerator(passlen=8):
    """This is normal password generator which help to generate password.
    Digits, special letters, uppercase, lowercase letters are use to generate
    password."""

    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation
    # print(s3)
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    return ("".join(random.sample(s, passlen)))

def intotxtfile(question ,text):
    with open("output.txt", 'a') as f:
        f.write("\n\nQuestion: "+question+"\n")
        f.write("Answer: ")
        for i in text:
            f.write(i)