import pytube
from pytube import Playlist
from pytube import YouTube
import os
import socket
import string
import random

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
clear()

print('''
                                                          
,--.   ,--.                                                    
|   `.'   | ,---.  ,---. ,--.--.,-----. ,---.  ,--,--.,--,--,  
|  |'.'|  || .-. :| .-. :|  .--'`-.  / | .-. :' ,-.  ||      \ 
|  |   |  |\   --.\   --.|  |    /  `-.\   --.\ '-'  ||  ||  | 
`--'   `--' `----' `----'`--'   `-----' `----' `--`--'`--''--' 

                Meerzean's Video Downloader


''')

print('''
Example video link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Example playlist link: https://www.youtube.com/playlist?list=PLLmgM5Ozkh95ETZegzy-dNicJ_oBX-o_m

Download Playlist: 1
Download Video: 2
''')

option= input("Select: ")
if option=="1":
    video=input("Enter playlist link: ")
    playlist = Playlist(''.join(video))
    videoCount=0
    downloadedCount=1
    for i in playlist.videos:
        videoCount=videoCount+1
    clear()
    for i in playlist.videos:
        i.streams.get_highest_resolution().download()
        print("(" + str(videoCount) + "/" + str(downloadedCount) + ")" + " Downloading: "+i.title)
        downloadedCount=downloadedCount+1
    print("Downloaded all videos.")
elif option=="2":
    video=input("Enter video link: ")
    if len(video) > 42 and len(video) < 44:
        yt=pytube.YouTube(''.join(video))
        print("Downloading: "+ yt.title)
        yt.streams.get_highest_resolution().download()
        print("Download finished.")
    else:
        print("You entered link wrong. If link contains something like '?t=1' delete it and try again.")
