import requests
import json
import time
from win32com.client import Dispatch

def speak(s):
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(s)

data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=287730a184914969995fae4db3559d3c")
result=data.json()
print(result['status'])
# print(result)

news=result['articles']

speak("Welcome to the my News Channel")
speak("Here are the top ten news of the awesome country India")
speak("So our first news is ")
for i in range(0,10):
    print(i)
    print(news[i]['description'])
    speak(news[i]['description'])
    if i>=9:
        break
    time.sleep(2)
    if i == 8:
        speak("So our last news for today is ")
    else:
        speak("Moving To Our next news")


speak("Thanks for listening ! Have a nice day")
speak("Keep coding")