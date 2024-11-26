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
from flask import Flask, render_template, request, redirect, url_for
import logging

# Function to display the custom title in the terminal
def print_title():
    Write.Print(r'''
 _______  _______  _______  ___ ___  _______  _______    _______  _______  _______  _______ 
|   _   ||   _   ||   _   \|   Y   ||   _   ||   _   \  |       ||   _   ||   _   ||       |
|   1___||.  1___||.  l   /|.  |   ||.  1___||.  l   /  |.|   | ||.  1___||   1___||.|   | |
|____   ||.  __)_ |.  _   1|.  |   ||.  __)_ |.  _   1  `-|.  |-'|.  __)_ |____   |`-|.  |-'
|:  1   ||:  1   ||:  |   ||:  1   ||:  1   ||:  |   |    |:  |  |:  1   ||:  1   |  |:  |  
|::.. . ||::.. . ||::.|:. | \:.. ./ |::.. . ||::.|:. |    |::.|  |::.. . ||::.. . |  |::.|  
`-------'`-------'`--- ---'  `---'  `-------'`--- ---'    `---'  `-------'`-------'  `---'  
    ''', Colors.black_to_red, interval=0.001)

# Function to display the menu and prompt for choice
def print_menu():
    Write.Print(r'''
    ---------- SERVER TEST ----------
          1- START SERVER
          2- EXIT
    ---------------------------------

''', Colors.black_to_red)

# Function to load settings from a file
file_path = os.path.join("data", "setted.txt")

with open(file_path, 'r') as file:
    for line in file:
        if line.startswith("username="):
            username = line.strip().split('=')[1]
        elif line.startswith("password="):
            password = line.strip().split('=')[1]

def load_settings():
    settings = {'username': 'User', 'password': ''}  # Default values
    try:
        with open(file_path, 'r') as file:
            for line in file:
                key, value = line.strip().split('=', 1)
                settings[key] = value
    except FileNotFoundError:
        os.system("python data/setting/set.py")
    return settings

# Function to start the Flask server
def start_server():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template("index.html")
    
    # Suppress Flask's default log messages
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)  # Suppresses the server logs

    Write.Print(f"\nRunning on: http://127.0.0.1:5000", Colors.white_to_green)
    
    # Start the Flask application with suppressed logs
    app.run(debug=False, use_reloader=False, host='127.0.0.1', port=5000)

# Function to listen for the 'stop' command to terminate the server
def listen_for_stop():
    while True:
        print("\nType !help for more commands." )
        user_input = input()
        if user_input.lower() == '!stop':
            Write.Print("\nStopping the server...", Colors.black_to_red)
            os.system("cls")
            time.sleep(1.5)
            os.system("python data/hack/hack.py")  # Terminate the program
        if user_input.lower() == '!help':
            Write.Print('''GALAXY TEST SERVER:
                        1- !stop : stop the server
                        2- !help: see this page
                        3- !new_page: ON MAINTAINCE
                        ''', Colors.black_to_red)
        

# Main menu for user to choose to start the server or exit
def main_menu(settings):
    os.system("cls")    
    print_title()
    print_menu()
    Write.Print(f"| {username} | >> Enter your choice: ", Colors.black_to_red)
    choice = input()
    if choice == "1":
        os.system("cls")
        # Start the Flask server in a separate thread
        server_thread = threading.Thread(target=start_server)
        server_thread.daemon = True
        server_thread.start()

        # Listen for the stop command
        listen_for_stop()
    elif choice == "2":
        os.system("cls")
        time.sleep(1.5)
        os.system("python data/hack/hack.py")
    else:
         Write.Print(f"| {username} | >> Invalid choice. Please try again.", Colors.black_to_red)
         time.sleep(1.5)
         main_menu(settings)

# Main entry point of the program
def main():
    settings = load_settings()
    main_menu(settings)

if __name__ == '__main__':
    main()
