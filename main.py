import speech_recognition as sr
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth






def ecouter():
    # On appelle la variable 'recognizer'
    recognizer = sr.Recognizer()
    
    recognizer.pause_threshold = 2.0
    
    with sr.Microphone() as source:
        print("Ajustement du bruit ambiant... veuillez patienter...")
        recognizer.adjust_for_ambient_noise(source, duration = 0.5)
        
        print("Je suis a votre écoute...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        
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
    
print("Démarrage de l'assistant...")

# On lance une boucle qui tournera en permanence
while True:
    # 1. L'assistant écoute la commande principale (à l'intérieur de la boucle !)
    text = ecouter()
    
    if text:
        text_min = text.lower()
        
        # --- GESTION DE L'ANNULATION GLOBALE ---
        # Si on dit annule ici, le 'break' casse la boucle while et le programme s'arrête.
        if "annule" in text_min or "annulation" in text_min:
            print("Commande d'annulation détectée. Arrêt du programme.")
            break 
            
        # --- GESTION DE LA PLAYLIST ---
        # Note : On utilise 'elif' (sinon si) pour que les actions ne se mélangent pas
        elif "playlist" in text_min:
            print("Quelle est votre mood actuelle ?")
            playlist = ecouter()
            
            if playlist:
                play_min = playlist.lower()
                
                # On permet aussi d'annuler juste le choix de la playlist
                if "annule" in play_min:
                    print("Choix de la playlist annulé. Retour au menu principal.")
                elif "jeu" in play_min or "jeux" in play_min:
                    print("Voici votre playlist de jeu !")
                elif "travail" in play_min:
                    print("Voici votre playlist de travail !")
                elif "jazz" in play_min:
                    print("Voici votre playlist dédiée au Jazz !")
                else:
                    print("Désolé, je n'ai pas compris votre mood.")
            else:
                pass
                
        # --- GESTION DU TRAVAIL ---
        elif "travail" in text_min:
            print("J'arrange votre espace de travail... veuillez patienter un instant !")
            os.system("open -a 'Safari'")
            os.system("open -a 'Spotify'")
            os.system("open -a 'visual studio code'")
            
            #ouverture de lien
            os.system("open -u https://webetud.iut-blagnac.fr/login/index.php")
            os.system("open -u https://github.com")
            os.system("open -u https://gemini.google.com/app")
            
            
            
            
            # C'est ici qu'on mettra les commandes os.system("open -a ...")
            
        # --- GESTION DU SERVEUR ---
        elif ("connexion" in text_min or "connecte" in text_min) and "serveur" in text_min:
            print("Je me connecte a votre serveur personnel... veuillez patienter un instant !")
            
    else:
        # S'il n'a rien entendu, il ne fait rien et la boucle recommence
        pass
    



