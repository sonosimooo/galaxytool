import sys
import random 
import time
import json
import requests
import threading
import subprocess
import urllib
from colorama import Fore, Back, Style
from pystyle import Write, Colors
from yt_dlp import YoutubeDL
import os


file_path = os.path.join("data", "setted.txt")

with open(file_path, 'r') as file:
            # Read the file line by line
            for line in file:
                # Strip any leading/trailing whitespace characters and split by '='
                if line.startswith("username="):
                    username = line.strip().split('=')[1]
                elif line.startswith("password="):
                    password = line.strip().split('=')[1]

input_folder = os.path.join("data/input")
output_folder = os.path.join("data/output")


def print_title():
    Write.Print(r'''
 ___ ___  ___  ______    _______  _______    ______    _______  ___ ___  ______   ___      _______  _______  ______   
|   Y   ||   ||   _  \  |   _   ||   _   |  |   _  \  |   _   ||   Y   ||   _  \ |   |    |   _   ||   _   ||   _  \  
|.  |   ||.  ||.  |   \ |.  1___||.  |   |  |.  |   \ |.  |   ||.  |   ||.  |   ||.  |    |.  |   ||.  1   ||.  |   \ 
|.  |   ||.  ||.  |    \|.  __)_ |.  |   |  |.  |    \|.  |   ||. / \  ||.  |   ||.  |___ |.  |   ||.  _   ||.  |    \
|:  1   ||:  ||:  1    /|:  1   ||:  1   |  |:  1    /|:  1   ||:      ||:  |   ||:  1   ||:  1   ||:  |   ||:  1    /
 \:.. ./ |::.||::.. . / |::.. . ||::.. . |  |::.. . / |::.. . ||::.|:. ||::.|   ||::.. . ||::.. . ||::.|:. ||::.. . / 
  `---'  `---'`------'  `-------'`-------'  `------'  `-------'`--- ---'`--- ---'`-------'`-------'`--- ---'`------'  
                                                                                                                      

                                                                                                                                        
    ''', Colors.black_to_red, interval=0.001)


def get_video_info(url):
    ydl_opts = {
        'quiet': True,           # Disabilita i log standard
        'no_warnings': True,     # Disabilita gli avvisi
        'noprogress': True,      # Nasconde la barra di progresso
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
    return info_dict


def scarica_video(link):
    try:
        options = {
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Percorso di salvataggio
            'format': 'best',      # Scarica il formato migliore
            'quiet': True,         # Sopprime messaggi standard
            'no_warnings': True,   # Disabilita avvisi
            'noprogress': True,    # Nasconde la barra di progresso
            'logger': CustomLogger()  # Logger personalizzato
        }
        with YoutubeDL(options) as ydl:
            Write.Print(f"\n| {username} | >> Scaricando il video da: {link}\n", Colors.black_to_red)
            ydl.download([link])
            Write.Print(f"| {username} | >> Download completato! Lo puoi trovare nell output folder.\n", Colors.green_to_white)
            time.sleep(1.5)
            os.system("cls")
            os.system("python data\youtube\youtube.py")
    except Exception as e:
        Write.Print(f"| {username} | >> Errore: {e}\n", Colors.red_to_black)
        main()


class CustomLogger:
    """Logger personalizzato per silenziare tutti i messaggi."""
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def main():
    os.system("cls")
    time.sleep(1)
    print_title()
    Write.Print(f"| {username} | >> Link: ", Colors.black_to_red)
    link = input()
    try:
        video_info = get_video_info(link)
        titolo = video_info.get('title', 'Titolo non disponibile')
        autore = video_info.get('uploader', 'Autore non disponibile')
        durata = video_info.get('duration', 0)  # Durata in secondi
        visualizzazioni = video_info.get('view_count', 0)
    except:
        Write.Print(f"| {username} | >> Errore durante il recupero delle informazioni del video.", Colors.black_to_red)

    Write.Print(f'''
                Video Information
                \nTitle: {titolo}
                \nAuthor: {autore}
                \nDuration: {durata} seconds
                \nVisualizzazioni: {visualizzazioni}                
                ''', Colors.black_to_red)
    Write.Print(f"\n| {username} | >> Download Video? (y/n):", Colors.black_to_red)
    yn = input()
    if yn == "y":
        Write.Print(f"| {username} | >> Downloading...", Colors.black_to_red)
        time.sleep(1.5)
        scarica_video(link)

    if yn == "n":
        Write.Print(f"| {username} | >> Exiting...", Colors.black_to_red)
        time.sleep(1.5)
        os.system("cls")
        main()

main()