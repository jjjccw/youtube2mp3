from prompt_toolkit import prompt, HTML
from prompt_toolkit.shortcuts import confirm
from prompt_toolkit.patch_stdout import patch_stdout
from tqdm import tqdm
from pytube import YouTube
import pytube.request
from time import sleep

def yt2mp3_prompt(msg: str):
    try:
        with patch_stdout():
            return(prompt(message=f"yt2mp3  - {msg}"))
    except KeyboardInterrupt:
        print("yt2mp3  - Quitting...")
        exit()
        
        
def yt2mp3_confirm(msg: str):
    try:
        with patch_stdout():
            return(confirm(message=f"yt2mp3  - {msg}", suffix="? (Y/n) > "))
    except KeyboardInterrupt:
        print("yt2mp3  - Quitting...")
        exit()
        
        
def yt2mp3_print(msg: str, end: str = "\n"):
    try:
        with patch_stdout():
            print(f"yt2mp3  - {msg}", end=end)
    except KeyboardInterrupt:
        print("yt2mp3  - Quitting...")
        exit()
        

def progress_function(stream, chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining)/stream.filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50-progress)
    # cant use our normal yt2mp3 print since we patch stdout
    print(f"yt2mp3  - Downloading: [{status}] {percent}%", end='\r')

def complete_function(stream, file_path):
    print('Video download completed')
        