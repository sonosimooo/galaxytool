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
import glob
import shutil

def print_title():
    Write.Print(r'''
 ___ ___  _______  _______  ___ ___     _______  _______  _______  ___      _______ 
|   Y   ||   _   ||   _   ||   Y   )   |       ||   _   ||   _   ||   |    |   _   |
|.  1   ||.  1   ||.  1___||.  1  /    |.|   | ||.  |   ||.  |   ||.  |    |   1___|
|.  _   ||.  _   ||.  |___ |.  _  \    `-|.  |-'|.  |   ||.  |   ||.  |___ |____   |
|:  |   ||:  |   ||:  1   ||:  |   \     |:  |  |:  1   ||:  1   ||:  1   ||:  1   |
|::.|:. ||::.|:. ||::.. . ||::.| .  )    |::.|  |::.. . ||::.. . ||::.. . ||::.. . |
`--- ---'`--- ---'`-------'`--- ---'     `---'  `-------'`-------'`-------'`-------'
                                                                                                                                      
    ''', Colors.black_to_red, interval=0.001)

def print_menu():
    Write.Print(r'''
    ---------- 𝐻𝒜𝒞𝒦 𝑀𝐸𝒩𝒰 ---------- [! MORE FEATURES WILL BE ADDED IN FUTURE UPDATES ]
          1- DDOS
          2- START A TEST SERVER          
          3- EXIT
    -----------------------------------

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

def load_settings():
    """Loads settings from the settings file."""
    settings = {'username': 'User', 'password': ''}  # Default values
    try:
        with open(file_path, 'r') as file:
            for line in file:
                key, value = line.strip().split('=', 1)
                settings[key] = value
    except FileNotFoundError:
        os.system("python data/setting/set.py")
    return settings

input_folder = os.path.join("data/input")
output_folder = os.path.join("data/output")
cache_folder = os.path.join("data/cache")
file_path = os.path.join("data", "setted.txt")

def main_menu(settings):
    os.system("cls")
    """Main menu logic."""
    username = settings.get("username", "User")
    print_title()
    print_menu()
    Write.Print(f"| {username} | >> ", Colors.black_to_red)
    choice = input().strip()
    if choice == "1":
         Write.Print(f"| {username} | >> Loading DDOS Tool...", Colors.black_to_red)
         time.sleep(1.5)
         os.system("cls")
         os.system("python data/hack/ddos.py")
    if choice == "2":
         Write.Print(f"| {username} | >> Loading Server Test...", Colors.black_to_red)
         time.sleep(1.5)
         os.system("cls")
         os.system("python data/hack/test_server.py")      
    if choice == "3":
         Write.Print(f"| {username} | >> Exiting...", Colors.black_to_red)
         time.sleep(1.5)
         os.system("cls")
         os.system("python main.py")
    
def main():
    settings = load_settings()


    main_menu(settings)

main()
