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
 _______  _______  _______  _______  ___  ______   _______  _______ 
|   _   ||   _   ||       ||       ||   ||   _  \ |   _   ||   _   |
|   1___||.  1___||.|   | ||.|   | ||.  ||.  |   ||.  |___||   1___|
|____   ||.  __)_ `-|.  |-'`-|.  |-'|.  ||.  |   ||.  |   ||____   |
|:  1   ||:  1   |  |:  |    |:  |  |:  ||:  |   ||:  1   ||:  1   |
|::.. . ||::.. . |  |::.|    |::.|  |::.||::.|   ||::.. . ||::.. . |
`-------'`-------'  `---'    `---'  `---'`--- ---'`-------'`-------'
                                                                    
    ''', Colors.black_to_red, interval=0.001)

def print_menu():
    Write.Print(r'''
    ---------- 𝒮𝐸𝒯𝒯𝐼𝒩𝒢𝒮 𝑀𝐸𝒩𝒰 ----------
          1- CLEAN OUTPUT FOLDER
          2- CLEAR INPUT FOLDER
          3- CLEAR CACHE
          4- RESET [ ! ]
          5- CHANGE USERNAME
          6- CHANGE PASSWORD
          7- EXIT
    ---------------------------------------

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
cache_folder = os.path.join("data/cache")
file_path = os.path.join("data", "setted.txt")

def clear_folder(folder_path):
    """Delete all files and subdirectories inside the given folder."""
    try:
        # Check if the folder exists
        if os.path.exists(folder_path):
            # Loop through the folder's contents
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                
                # If it's a file, delete it
                if os.path.isfile(file_path):
                    os.remove(file_path)
                
                # If it's a directory, remove it (and all its contents)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
        else:
            print(f"Folder not found: {folder_path}")
    
    except Exception as e:
        print(f"Error while clearing the folder: {e}")

def main():
    print_title()
    print_menu()
    Write.Print(f"| {username} | >> ", Colors.black_to_red)  # Solo la stampa del prompt
    scelta = input()
    if scelta == "1":
        Write.Print(f"| {username} | >> Cleaning Output Folder..", Colors.black_to_red)
        time.sleep(1.5)
        clear_folder(output_folder)
        Write.Print(f"\n| {username} | >> Output Folder Cleaned!", Colors.white_to_green)
        time.sleep(1.5)
        os.system("cls")
        main()
    if scelta == "2":
        Write.Print(f"| {username} | >> Cleaning Input Folder..", Colors.black_to_red)
        time.sleep(1.5)
        clear_folder(input_folder)
        Write.Print(f"| {username} | >> Input Folder Cleaned!", Colors.white_to_green)
        time.sleep(1.5)
        os.system("cls")
        main()
    if scelta == "3":
        Write.Print(f"| {username} | >> Clearing Cache..", Colors.black_to_red)
        time.sleep(1.5)
        clear_folder(cache_folder)
        Write.Print(f"| {username} | >> Cache Cleared!", Colors.white_to_green)
        time.sleep(1.5)
        os.system("cls")
        main()
    if scelta == "4":
        Write.Print(f"| {username} | >> Insert your password to continue: ", Colors.black_to_red)
        password = input()
        if password == password:
            Write.Print(f"| {username} | >> Do you want to reset the tool? [1] Yes [2] No >> ", Colors.black_to_red)
            scelta = input()
            if scelta == "1":
                Write.Print(f"| {username} | >> Resetting Tool..", Colors.black_to_red)
                time.sleep(1.5)
                os.system("cls")
                os.remove(file_path)
                os.rmdir(output_folder)
                os.rmdir(input_folder)
                os.rmdir(cache_folder)

                os.system("python data/setting/set.py")
            if scelta == "2":
                Write.Print(f"| {username} | >> Going Back..", Colors.black_to_red)
                time.sleep(1.5)
                os.system("cls")
                main()
        else:
            Write.Print(f"| {username} | >> Wrong Password!", Colors.white_to_red)
            time.sleep(1.5)
            os.system("cls")
            main()
    if scelta == "5":
        Write.Print(f"| {username} | >> Insert your password to continue: ", Colors.black_to_red)
        password = input()
        if password == password:
            Write.Print(f"| {username} | >> Enter your new username: ", Colors.black_to_red)
            new_username = input()
            Write.Print(f"| {username} | >> Changing Username..", Colors.black_to_red)
            time.sleep(1.5)
            with open(file_path, "w") as file:
                file.write(f"username={new_username}\npassword={password}")
            Write.Print(f"| {username} | >> Username Changed!", Colors.white_to_green)
            time.sleep(1.5)
            os.system("cls")
            main()
        else:
            Write.Print(f"| {username} | >> Wrong Password!", Colors.white_to_red)
            time.sleep(1.5)
            os.system("cls")
            main()
    if scelta == "6":
            Write.Print(f"| {username} | >> Insert your password to continue: ", Colors.black_to_red)
            password = input()
            if password == password:
                Write.Print(f"| {username} | >> Enter your new password: ", Colors.black_to_red)
                new_password = input()
                Write.Print(f"| {username} | >> Changing Password..", Colors.black_to_red)
                time.sleep(1.5)
                with open(file_path, "w") as file:
                    file.write(f"username={username}\npassword={new_password}")
                Write.Print(f"| {username} | >> Password Changed!", Colors.white_to_green)
                time.sleep(1.5)
                os.system("cls")
                main()
    if scelta == "7":
            Write.Print(f"| {username} | >> Exiting..", Colors.black_to_red)
            time.sleep(1.5)
            os.system("cls")
            os.system("python main.py")
            exit()

main()

