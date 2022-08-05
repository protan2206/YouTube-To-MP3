# importing modules 
from __future__ import unicode_literals
import youtube_dl
import sys

# getting links using running command 
links = sys.argv[1:]

# function to download yt audios
def Download(link):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'{link}'])
    except:
        pass

if __name__ == "__main__":
    if len(links) > 0 :
        for link in links:
            Download(link)
            print("[+] Video Download Compleate")
    else :
        print("[!] Command Error \n[!] Command Example : python3 main.py link link\n")