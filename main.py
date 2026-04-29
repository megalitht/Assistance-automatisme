import speech_recognition as sr
def ecouter():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Ajustement du bruit ambiant... patiente 1 seconde...")
        recognizer.adjust_for_ambient_noise(source)
        
        print("Je suis a votre écoute...")
        audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio, language="fr-FR")
        print("Vous avez dit : " + text)
        return text
    
    except sr.UnknownValueError:
        print("Désolé, je n'ai pas compris ce que vous avez dit.")
        return None
    
    except sr.RequestError as e:
        print("Erreur de service de reconnaissance vocale : {0}".format(e))
        return None
    
ecouter()
