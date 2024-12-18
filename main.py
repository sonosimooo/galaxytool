import subprocess
import requests
import os
import time
from pystyle import Colors, Write
from tqdm import tqdm

file_path = os.path.join("data", "setted.txt")
version = "0.1.0"
max_value = 100

# Funzione per ottenere l'ultimo commit remoto
def get_remote_commit():
    url = "https://api.github.com/repos/sonosimooo/galaxytool/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        return commits[0]["sha"]
    else:
        Write.Print("Errore nel recupero dei dati dal repository GitHub", Colors.red)
        return None

# Funzione per ottenere il commit locale
def get_local_commit():
    try:
        result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        Write.Print("Errore nel recupero del commit locale", Colors.red)
        return None

# Funzione per fare il pull se ci sono aggiornamenti
def check_for_updates(): 
    Write.Print("\nChecking for updates...", Colors.green)
    for i in tqdm(range(100), desc="Loading", ascii=True, ncols=75):
        time.sleep(0.05)
    
    remote_commit = get_remote_commit()
    if remote_commit is None:
        Write.Print("Impossible verify updtes!", Colors.red)
        return
    
    local_commit = get_local_commit()
    if local_commit is None:
        Write.Print("Impossible to get the commit.", Colors.red)
        return

    if remote_commit != local_commit:
        Write.Print("\nNew Update found! Updating...", Colors.green)
        subprocess.run(['git', 'pull'])
        Write.Print("\nUpdate Completed!", Colors.green)
        os.system("cls")
        os.system("python main.py")
        
    else:
        Write.Print("\nThe repostory is updated!", Colors.green)

def print_title():
    Write.Print(r'''
 _______  _______  ___      _______   ___ ___   ___ ___    _______  _______  _______  ___     
|   _   ||   _   ||   |    |   _   | (   Y   ) |   Y   |  |       ||   _   ||   _   ||   |    
|.  |___||.  1   ||.  |    |.  1   |  \  1  /  |   1   |  |.|   | ||.  |   ||.  |   ||.  |    
|.  |   ||.  _   ||.  |___ |.  _   |  /  _  \   \_   _/   `-|.  |-'|.  |   ||.  |   ||.  |___ 
|:  1   ||:  |   ||:  1   ||:  |   | /:  |   \   |:  |      |:  |  |:  1   ||:  1   ||:  1   |
|::.. . ||::.|:. ||::.. . ||::.|:. |(::. |:.  )  |::.|      |::.|  |::.. . ||::.. . ||::.. . |
`-------'`--- ---'`-------'`--- ---' `--- ---'   `---'      `---'  `-------'`-------'`-------'
                                                                                              
    ''', Colors.black_to_red, interval=0.001)

def print_menu():
    Write.Print(r'''
    ---------- 𝑀𝐸𝒩𝒰 ---------- 𝒪𝒯𝐻𝐸𝑅 𝒞𝒪𝑀𝑀𝒜𝒩𝒟𝒮---- [! MORE FEATURES WILL BE ADDED IN FUTURE UPDATES ]
          1- YOUTUBE TOOLS         U - Check updates
          2- HACK TOOLS            V - Check Version          
          3- DISCORD TOOLS         E - Exit
          4- SETTINGS
    ----------------------------------------------------

''', Colors.black_to_red, interval=0.00001)

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
    os.system("cls")
    """Main menu logic."""
    username = settings.get("username", "User")
    print_title()
    print_menu()
    Write.Print(f"| {username} | >> ", Colors.black_to_red)
    choice = input().strip()

    if choice == "1":
        Write.Print(f"| {username} | >> Loading Youtube Tools...", Colors.black_to_red)
        time.sleep(1.5)
        os.system("cls")
        os.system("python data/youtube/youtube.py")
    if choice == "2":
        Write.Print(f"| {username} | >> Loading Hack Tools...", Colors.black_to_red)
        time.sleep(1.5)
        os.system("cls")
        Write.Print(f"| {username} | >> Insert the password to continue.", Colors.black_to_red)
        password = input()
        if password == settings.get("password"):
            os.system("cls")
            os.system("python data/hack/hack.py")
        else:
            Write.Print(f"| {username} | >> Wrong Password!", Colors.red)
            time.sleep(1.5)
            os.system("cls")
            main_menu(settings)
    if choice == "3":
        Write.Print(f"| {username} | >> This Function is under maintance.", Colors.black_to_red)
        main_menu(settings)
    elif choice == "4":
        Write.Print(f"| {username} | >> Loading Settings...", Colors.black_to_red)
        time.sleep(1.5)
        os.system("cls")
        os.system("python data/setting/setting.py")
    elif choice == "u":
        check_for_updates()  # Aggiungi il controllo aggiornamenti qui
        main_menu(settings)
    elif choice == "v":
        Write.Print(f"| {username} | >> Version: {version}", Colors.black_to_red)
        time.sleep(1.5)
        os.system("cls")
        main_menu(settings)
    elif choice == "e":
        Write.Print(f"| {username} | >> Exiting...", Colors.black_to_red)
        time.sleep(1.5)
        exit()
    else:
        Write.Print(f"| {username} | >> Invalid choice. Try again!", Colors.red)
        time.sleep(1)
        main_menu(settings)

def main():
    settings = load_settings()

    # Controllo aggiornamenti all'avvio
    check_for_updates()

    main_menu(settings)

if __name__ == "__main__":
    if not os.path.exists(file_path):
        Write.Print("| System | >> Settings file not found. Launching setup...", Colors.red)
        os.system("python data/setting/set.py")
    main()
