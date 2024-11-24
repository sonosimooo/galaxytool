import os
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
from pytube import YouTube

def print_title():
    Write.Print(r'''
 ___ ___  _______  ___ ___  _______  ___ ___  _______   _______    _______  _______  _______  ___      _______ 
|   Y   ||   _   ||   Y   ||       ||   Y   ||   _   \ |   _   |  |       ||   _   ||   _   ||   |    |   _   |
|   1   ||.  |   ||.  |   ||.|   | ||.  |   ||.  1   / |.  1___|  |.|   | ||.  |   ||.  |   ||.  |    |   1___|
 \_   _/ |.  |   ||.  |   |`-|.  |-'|.  |   ||.  _   \ |.  __)_   `-|.  |-'|.  |   ||.  |   ||.  |___ |____   |
  |:  |  |:  1   ||:  1   |  |:  |  |:  1   ||:  1    \|:  1   |    |:  |  |:  1   ||:  1   ||:  1   ||:  1   |
  |::.|  |::.. . ||::.. . |  |::.|  |::.. . ||::.. .  /|::.. . |    |::.|  |::.. . ||::.. . ||::.. . ||::.. . |
  `---'  `-------'`-------'  `---'  `-------'`-------' `-------'    `---'  `-------'`-------'`-------'`-------'                                                                                                                 

    ''', Colors.black_to_red, interval=0.001)

def print_menu():
    Write.Print(r'''
    ---------- 𝒴𝒪𝒰𝒯𝒰𝐵𝐸 𝒯𝒪𝒪𝐿𝒮 ----------
          1- DOWNLOAD VIDEO
          2- DOWNLOAD AUDIO
          3- YOUTUBE STATS
          4- DOWNLOAD MINIATURE
          5- EXIT
    ----------------------------

''', Colors.black_to_red)
    

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

def main():
    print_title()
    print_menu()
    Write.Print(f"| {username} | >> ", Colors.black_to_red)  # Solo la stampa del prompt
    scelta = input()
    if scelta == "1":
        Write.Print(f"| {username} | >> Loading Download Video..", Colors.black_to_red)
        time.sleep(1.5)
        os.system("cls")
        os.system("python data/youtube/download_video.py")
    if scelta == "2":
        Write.Print(f"| {username} | >> Loading Download Audio..", Colors.black_to_red)
        time.sleep(1.5)
        os.system("cls")
        os.system("python data/youtube/download_audio.py")
    if scelta == "3":
        Write.Print(f"| {username} | >> Loading Youtube Stats..", Colors.black_to_red)
        time.sleep(1.5)
        os.system("cls")
        os.system("python data/youtube/youtube_stats.py")
    if scelta == "4":
        Write.Print(f"| {username} | >> Loading Download Miniature..", Colors.black_to_red)
        time.sleep(1.5)
        os.system("cls")
        os.system("python data/youtube/copertina.py")
    if scelta == "5":
        Write.Print(f"| {username} | >> Exiting...", Colors.black_to_red)
        time.sleep(1.5)
        os.system("cls")
        os.system("python main.py")

main()