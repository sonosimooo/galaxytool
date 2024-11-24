import os
import time
from pystyle import Write, Colors

# Directory paths
input_folder = os.path.join("data/input")
output_folder = os.path.join("data/output")
cache_folder = os.path.join("data/cache")
file_path = os.path.join("data", "setted.txt")

def delete_files():
    os.remove(file_path)
    os.rmdir(output_folder)
    os.rmdir(input_folder)
    os.rmdir(cache_folder)

def create_files():
    # Create necessary folders and file
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    if not os.path.exists(cache_folder):
        os.makedirs(cache_folder)
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("username=None\npassword=None\n")

def ask_password(username):
    while True:
        Write.Print("Enter your password: ", Colors.black_to_red)
        password = input()
        Write.Print("Enter your password again: ", Colors.black_to_red)
        password_confirmation = input()

        if password == password_confirmation:
            Write.Print("Password set successfully!", Colors.white_to_green)
            try:
                # Writing username and password to the file
                with open(file_path, "w") as file:
                    file.write(f"username={username}\npassword={password}\n")
                Write.Print("Successfully set your username and password!", Colors.white_to_green)
                time.sleep(1.5)
                os.system("cls")
                Write.Print("Loading...", Colors.black_to_red)
                time.sleep(1.5)
                os.system("cls")
                Write.Print("Welcome to Galaxy Tool!", Colors.black_to_red)
                time.sleep(1.5)
                os.system("cls")
                os.system("python main.py")
                break
            except Exception as e:
                Write.Print(f"Error saving to file: {e}", Colors.red_to_black)
                break
        else:
            Write.Print("Passwords do not match. Please try again.", Colors.red_to_black)

def main():
    Write.Print("Welcome to Simo Tool!", Colors.black_to_red)
    time.sleep(1.5)
    os.system("cls")
    Write.Print("Loading...", Colors.black_to_red)
    time.sleep(1.5)
    os.system("cls")
    create_files()
    Write.Print("Enter your username: ", Colors.black_to_red)
    username = input().strip()
    if username:
        ask_password(username)
    else:
        Write.Print("Username cannot be empty. Restarting setup.", Colors.red_to_black)
        time.sleep(1.5)
        os.system("cls")
        main()

main()
