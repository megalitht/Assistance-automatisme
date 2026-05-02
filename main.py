import speech_recognition as sr
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import keyboard



def ecouter(silencieux=False):
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1.0
    
    try:
        with sr.Microphone() as source:
            if not silencieux:
                print("Ajustement du bruit ambiant...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            if not silencieux:
                print("Je suis à votre écoute...")
                
            # La correction est ici : suppression du paramètre 'timeout=5'
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
            
        
            text = recognizer.recognize_google(audio, language="fr-FR")
            if not silencieux:
                print("Vous avez dit : " + text)
            return text
        
    except sr.UnknownValueError:
        if not silencieux:
            print("Désolé, je n'ai pas compris ce que vous avez dit.")
        return None
    except sr.RequestError as e:
        if not silencieux:
            print("Erreur de service : {0}".format(e))
        return None
    
while True:
    # 1. ÉCOUTE PASSIVE (Silencieuse)
    # On écoute en boucle sans rien afficher, jusqu'à entendre quelque chose
    appel = ecouter(silencieux=True)
    
    if appel and "Fabrice" in appel.lower():
        print("\nOui Monsieur ? Que puis-je faire pour vous ?")
        
        # 2. ÉCOUTE ACTIVE (Une seule fois après l'appel)
        text = ecouter(silencieux=False)
        
        if text:
            text_min = text.lower()
            
            # --- GESTION DE L'ANNULATION GLOBALE ---
            if "arrête" in text_min or "arrêt du programme" in text_min:
                print("Commande d'annulation détectée. Arrêt du programme.")
                break 
                
            # --- GESTION DE LA PLAYLIST ---
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
                
                #ouverture d'applications
                os.system("open -a 'Safari'")
                os.system("open -a 'Spotify'")
                os.system("open -a 'visual studio code'")
                
                #ouverture de lien
                os.system("open -u https://webetud.iut-blagnac.fr/login/index.php")
                os.system("open -u https://github.com")
                os.system("open -u https://gemini.google.com/app")
                
                
                
                            
            # --- GESTION DU SERVEUR ---
            elif ("connexion" in text_min or "connecte" in text_min) and "serveur" in text_min:
                print("Je me connecte a votre serveur personnel... veuillez patienter un instant !")
                
                os.system("open -a 'Terminal'")
                os.system("open -u ssh://antoine@100.99.83.6")
                
                print ("voulez-vous que je tape votre mot de passe automatiquement ?")
                if "oui" in text_min:
                    keyboard.write('os.environ.get("MOT_DE_PASSE_SERVEUR")')
                    keyboard.press_and_release('enter')
                    
                    print("Connexion établie avec le serveur !")
                else:
                    pass
                
                
                
                
                
            # --- GESTION DYNAMIQUE DES APPLICATIONS ---
            elif "ouvre" in text_min or "ouvrir" in text_min or "lance" in text_min:

                partie_apres_ouvre = text_min.split("ouvre")[1] if "ouvre" in text_min else text_min.split("ouvrir")[1] if "ouvrir" in text_min else text_min.split("lance")[1]
                
                app_string = partie_apres_ouvre.strip()

                applications = app_string.split(" et ")

                print(f"Très bien, ouverture de : {', '.join(applications)}...")
                for app in applications:
    
                    app_propre = app.strip()
                    
                    os.system(f'open -a "{app_propre}"')
                    
        

            # --- GESTION MESSAGES ---
            elif "message" in text_min:
                print("A qui voulez-vous envoyer un message ?")
                destinataire = ecouter()
                
                if destinataire:
                    dest_min = destinataire.lower()
                    
                    if "annule" in dest_min:
                        print("Envoi de message annulé. Retour au menu principal.")
                    else:
                        print(f"Quel est le message que vous souhaitez envoyer à {dest_min} ?")
                        contenu_message = ecouter()
                        
                        if contenu_message:
                            cont_min = contenu_message.lower()
                            
                            if "annule" in cont_min:
                                print("Envoi de message annulé. Retour au menu principal.")
                            else:
                                print(f"Message envoyé à {dest_min} : {contenu_message}")
                        else:
                            pass
                else:
                    pass
            
            
            elif "connecte" in text_min and "IUT" in text_min or "espace étudiant" in text_min:
                print("Je me connecte à votre espace étudiant de l'IUT... veuillez patienter un instant !")
                os.system("open -a 'Safari'")
                os.system("open -u https://webetud.iut-blagnac.fr/login/index.php")
                #temps d'attente reel pour que la page se charge, à ajuster selon la vitesse de connexion

                wait_time = 3
                
                print(f"Attente de {wait_time} secondes pour que la page se charge...")
                
                print("Voulez-vous que je remplisse automatiquement vos identifiants ?")
                
                if "oui" in text_min:
                    
                    keyboard.press_and_release('tab')
                    keyboard.write('os.environ.get("IDENTIFIANT_IUT")') 
                    keyboard.press_and_release('tab')
                    keyboard.write('os.environ.get("MOT_DE_PASSE_IUT")')
                    keyboard.press_and_release('enter') 
                
                else:
                    pass
        
    else:
        # S'il n'a rien entendu, il ne fait rien et la boucle recommence
        pass
