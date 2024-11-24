import os
import time
from yt_dlp import YoutubeDL
import matplotlib.pyplot as plt
from colorama import Fore
from pystyle import Write, Colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import re


file_path = os.path.join("data", "setted.txt")

with open(file_path, 'r') as file:
            # Read the file line by line
            for line in file:
                # Strip any leading/trailing whitespace characters and split by '='
                if line.startswith("username="):
                    username = line.strip().split('=')[1]
                elif line.startswith("password="):
                    password = line.strip().split('=')[1]

# Directory di salvataggio
output_folder = os.path.join("data/output")
cache_folder = os.path.join("data/cache")

# Crea la cartella 'cache' se non esiste
if not os.path.exists(cache_folder):
    os.makedirs(cache_folder)

def print_title():
    Write.Print(r'''
 ___ ___  ___  ______    _______  _______    _______  _______  _______  _______  _______ 
|   Y   ||   ||   _  \  |   _   ||   _   |  |   _   ||       ||   _   ||       ||   _   |
|.  |   ||.  ||.  |   \ |.  1___||.  |   |  |   1___||.|   | ||.  1   ||.|   | ||   1___|
|.  |   ||.  ||.  |    \|.  __)_ |.  |   |  |____   |`-|.  |-'|.  _   |`-|.  |-'|____   |
|:  1   ||:  ||:  1    /|:  1   ||:  1   |  |:  1   |  |:  |  |:  |   |  |:  |  |:  1   |
 \:.. ./ |::.||::.. . / |::.. . ||::.. . |  |::.. . |  |::.|  |::.|:. |  |::.|  |::.. . |
  `---'  `---'`------'  `-------'`-------'  `-------'  `---'  `--- ---'  `---'  `-------'
                                                                                                                                                                                                           
    ''', Colors.black_to_red, interval=0.001)

def get_video_info(url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(url, download=False)

def clean_filename(filename):
    # Remove or replace invalid characters for file names on Windows
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def generate_graph(views, likes, duration, comments):
    # Crea un grafico a barre per visualizzare le statistiche
    categories = ['Views', 'Likes', 'Duration (s)', 'Comments']
    values = [views, likes, duration, comments]

    plt.figure(figsize=(6, 4))
    plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'])
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.title('Video Statistics')
    
    # Salva il grafico come immagine nella cartella cache
    graph_filename = os.path.join(cache_folder, 'video_stats_graph.png')
    plt.savefig(graph_filename)
    plt.close()
    return graph_filename

def save_stats_to_pdf(video_info):
    title = video_info.get('title', 'Title not available')
    views = video_info.get('view_count', 0)
    duration = video_info.get('duration', 0)
    likes = video_info.get('like_count', 0)
    comments = video_info.get('comment_count', 0)

    # Clean the video title to create a valid file name
    clean_title = clean_filename(title)

    # Generate the graph
    graph_filename = generate_graph(views, likes, duration, comments)

    # Create the PDF
    pdf_filename = os.path.join(output_folder, f"{clean_title}_stats.pdf")
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Title
    c.setFont("Helvetica", 14)
    c.drawString(30, 750, f"Video Statistics: {title}")
    
    # Text data
    c.setFont("Helvetica", 12)
    c.drawString(30, 730, f"Title: {title}")
    c.drawString(30, 710, f"Views: {views}")
    c.drawString(30, 690, f"Duration: {duration} seconds")
    c.drawString(30, 670, f"Likes: {likes}")
    c.drawString(30, 650, f"Comments: {comments}")

    # Inserisci il grafico nel PDF
    c.drawImage(graph_filename, 30, 400, width=500, height=250)

    # Save the PDF
    c.save()

    Write.Print(f"| {username} | >> File {pdf_filename} saved in the output folder.", Colors.white_to_green)
    time.sleep(1.5)
    os.system("cls")
    os.system("python youtube.py")

def main():
    os.system("cls")
    time.sleep(1.5)
    print_title()
    Write.Print(f"| {username} | >> Link: ", Colors.black_to_red)
    link = input()

    try:
        video_info = get_video_info(link)
        save_stats_to_pdf(video_info)  # Salva le informazioni nel PDF
    except Exception as e:
        Write.Print(f"| {username} | >> Errore durante il recupero delle informazioni del video: {e}", Colors.red)
        main()

main()
