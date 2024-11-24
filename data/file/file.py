import os
import time
from pystyle import Write, Colors

# Path configuration
file_path = os.path.join("data", "setted.txt")
input_folder = os.path.join("data", "input")
output_folder = os.path.join("data", "output")

def print_title():
    Write.Print(r'''
 _______  ___  ___      _______    _______  _______  _______  ___      _______ 
|   _   ||   ||   |    |   _   |  |       ||   _   ||   _   ||   |    |   _   |
|.  1___||.  ||.  |    |.  1___|  |.|   | ||.  |   ||.  |   ||.  |    |   1___|
|.  __)  |.  ||.  |___ |.  __)_   `-|.  |-'|.  |   ||.  |   ||.  |___ |____   |
|:  |    |:  ||:  1   ||:  1   |    |:  |  |:  1   ||:  1   ||:  1   ||:  1   |
|::.|    |::.||::.. . ||::.. . |    |::.|  |::.. . ||::.. . ||::.. . ||::.. . |
`---'    `---'`-------'`-------'    `---'  `-------'`-------'`-------'`-------'
                                                                               
    ''', Colors.black_to_red, interval=0.001)

def print_menu():
    Write.Print(r'''
    ---------- 𝐹𝐼𝐿𝐸 𝒯𝒪𝒪𝐿𝒮 𝑀𝐸𝒩𝒰 ---------- 
          1- CONVERT FILES
          2- CREATE FILES
          3- MODIFY FILES
          4- DELETE FILES
          5- SEARCH FILES
          6- COPY FILES
          7- MOVE FILES
          8- RENAME FILES
          9- FOLDER MANAGER
          10- EXIT
    ----------------------------

''', Colors.black_to_red)
    
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

def main_menu(settings):
    """Main menu logic."""
    username = settings.get("username", "User")
    password = settings.get("password", "")
    print_title()
    print_menu()
    Write.Print(f"| {username} | >> ", Colors.black_to_red)
    choice = input().strip()
    if choice == "1":
        os.system("python data/file/convert.py")
    elif choice == "2":
        os.system("python data/file/create.py")
    elif choice == "3":
        os.system("python data/file/modify.py")
    elif choice == "4":
        os.system("python data/file/delete.py")
    elif choice == "5":
        os.system("python data/file/search.py")
    elif choice == "6":
        os.system("python data/file/copy.py")
    elif choice == "7":
        os.system("python data/file/move.py")
    elif choice == "8":
        os.system("python data/file/rename.py")
    elif choice == "9":
        os.system("python data/file/folder.py")
    elif choice == "10":
        Write.Print(f"| {username} | >> Exiting...", Colors.black_to_red)
        time.sleep(1.5)
        os.system("cls")
        os.system("python main.py")

main_menu(load_settings())

