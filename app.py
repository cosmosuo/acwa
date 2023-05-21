import speech_recognition as sr
from tts import speak
from chat import chat

r = sr.Recognizer()
mic = sr.Microphone()


def listen(lang="en-US"):
    with mic as source:
        try:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            return r.recognize_google(audio, language=lang)
        except sr.UnknownValueError:
            return "" #empty string as error

byeWords = ("bye", "goodbye","exit", "quit","close","Stop")

def askAI(lang="en-US"):
    while True:
        speak("Say somethin i'm giving up on you")
        text = listen(lang)
        if text == "":
            speak("Sorry, I did not understand you.")
            continue
        elif text.lower() in byeWords:
            speak("finally, leave")
            break
        aiResp = chat(text)
        speak(aiResp)

askAI()