from prompt_toolkit import prompt, HTML
from prompt_toolkit.shortcuts import confirm
from prompt_toolkit.patch_stdout import patch_stdout
from tqdm import tqdm
from pytube import YouTube
from time import sleep
import sys

def yt2mp3_prompt(msg: str):
    try:
        return(prompt(message=f"yt2mp3  - {msg}"))
    except KeyboardInterrupt:
        print("yt2mp3  - Quitting...")
        exit()
        
        
def yt2mp3_confirm(msg: str):
    try:
        return(confirm(message=f"yt2mp3  - {msg}", suffix="? (Y/n) > "))
    except KeyboardInterrupt:
        print("yt2mp3  - Quitting...")
        exit()
        
        
def yt2mp3_print(msg: str, end: str = "\n"):
    try:
        print(f"yt2mp3  - {msg}", end=end)
    except KeyboardInterrupt:
        print("yt2mp3  - Quitting...")
        exit()
        

class ProgressBar(tqdm):
    def update_to(self, bytes_transferred):
        self.update(bytes_transferred - self.n)  # will also set self.n = bytes_transferred
        
def progress_wrapper(pbar):
    def progress_callback(stream, chunk, bytes_remaining):
        bytes_transferred = stream.filesize - bytes_remaining
        pbar.update_to(bytes_transferred)
    return progress_callback

def complete_function(stream, file_path):
    print('yt2mp3  - Video download completed ')
