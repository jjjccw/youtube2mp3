from prompt_toolkit import prompt, HTML
from prompt_toolkit.shortcuts import confirm
# from prompt_toolkit.patch_stdout import patch_stdout
from tqdm import tqdm

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
        