import os
import time
import requests
from yt_dlp import YoutubeDL
from pystyle import Write, Colors
import re

# Get the username

file_path = os.path.join("data", "setted.txt")

with open(file_path, 'r') as file:
            # Read the file line by line
            for line in file:
                # Strip any leading/trailing whitespace characters and split by '='
                if line.startswith("username="):
                    username = line.strip().split('=')[1]
                elif line.startswith("password="):
                    password = line.strip().split('=')[1]

# Define output directories
output_folder = os.path.join("data/output")
cache_folder = os.path.join("data/cache")

# Create the 'output' and 'cache' directories if they don't exist
os.makedirs(output_folder, exist_ok=True)
os.makedirs(cache_folder, exist_ok=True)

def print_title():
    Write.Print(r'''
 ___ ___  _______    _______  ___ ___  ___ ___  ___ ___  _______   ______   _______  ___  ___       
|   Y   ||       |  |       ||   Y   ||   Y   ||   Y   ||   _   \ |   _  \ |   _   ||   ||   |      
|   1   ||.|   | |  |.|   | ||.  1   ||.  |   ||.      ||.  1   / |.  |   ||.  1   ||.  ||.  |      
 \_   _/ `-|.  |-'  `-|.  |-'|.  _   ||.  |   ||. \_/  ||.  _   \ |.  |   ||.  _   ||.  ||.  |___   
  |:  |    |:  |      |:  |  |:  |   ||:  1   ||:  |   ||:  1    \|:  |   ||:  |   ||:  ||:  1   |  
  |::.|    |::.|      |::.|  |::.|:. ||::.. . ||::.|:. ||::.. .  /|::.|   ||::.|:. ||::.||::.. . |  
  `---'    `---'      `---'  `--- ---'`-------'`--- ---'`-------' `--- ---'`--- ---'`---'`-------'  
                                                                                                                                                                                                                                                                                                        
    ''', Colors.black_to_red, interval=0.001)

def get_video_info(url):
    """Get video information using yt-dlp."""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(url, download=False)

def clean_filename(filename):
    """Clean the filename by removing invalid characters."""
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def save_thumbnail(thumbnail_url, video_title):
    """Download the video thumbnail and save it to the cache folder."""
    clean_title = clean_filename(video_title)
    thumbnail_filename = os.path.join(cache_folder, f"{clean_title}_thumbnail.jpg")
    
    try:
        response = requests.get(thumbnail_url)
        response.raise_for_status()  # Check if the request was successful
        
        # Save the thumbnail image in the cache folder
        with open(thumbnail_filename, 'wb') as f:
            f.write(response.content)
        
        Write.Print(f"Thumbnail saved successfully: {thumbnail_filename}", Colors.white_to_green)
        time.sleep(1.5)
        os.system("cls")
        os.system("python data\youtube\youtube.py")
        return thumbnail_filename
        
        

    except requests.exceptions.RequestException as e:
        Write.Print(f"Error downloading the thumbnail: {e}", Colors.red)
        main()

def main():
    os.system("cls")
    time.sleep(1.5)
    print_title()
    Write.Print(f"| {username} | >> Enter Video URL: ", Colors.black_to_red)
    link = input()

    try:
        video_info = get_video_info(link)
        thumbnail_url = video_info.get('thumbnail', None)
        
        if thumbnail_url:
            thumbnail_filename = save_thumbnail(thumbnail_url, video_info['title'])
        else:
            Write.Print(f"Thumbnail not available for the video.", Colors.red)
            main()
    except Exception as e:
        Write.Print(f"| {username} | >> Error retrieving video information: {e}", Colors.red)
        main()

# Run the main function
if __name__ == "__main__":
    main()
