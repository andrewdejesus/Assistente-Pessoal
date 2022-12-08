import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import os
import time


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'brazil')

def talk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



def run_alexa():
    try: 
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            time.sleep(0.5)
            command = listener.recognize_google(voice, language='pt-BR')
            command = command.lower()

        if "alexa" in command:
            command = command.replace("alexa", "")
            if 'pesquisar' in command:
                command = command.replace("pesquisar", "")
                if 'sobre' in command:
                    command = command.replace("sobre", "")
                    wikipedia.set_lang("pt")
                    info = wikipedia.summary(command,3)
                    talk(info)


            elif 'tocar' in command:
                song = command.replace("tocar", "")
                talk('Tocando música')
                pywhatkit.playonyt(song)
            
            elif 'desligar' in command:
                command = command.replace("desligar", "")
                if "computador" in command:
                    command = command.replace("computador", "")
                    os.system("shutdown /s /t 1")

            elif 'reiniciar' in command:
                command = command.replace("reiniciar", "")
                if "computador" in command:
                    command = command.replace("computador", "")
                    os.system("shutdown /r /t 1")
            

            
            else:
                talk("Desculpe, não entendi")
        

    except:
        pass

    

while True:
    run_alexa()
