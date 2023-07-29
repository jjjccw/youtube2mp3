from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import confirm
from prompt_toolkit.patch_stdout import patch_stdout
from tqdm import tqdm
def yt2mp3_prompt(msg: str):
    try:
        with patch_stdout():
            return(prompt(message=f"yt2mp3  - {msg}"))
    except KeyboardInterrupt:
        print("Quitting...")
        exit()
        
        
def yt2mp3_confirm(msg: str):
    try:
        with patch_stdout():
            return(confirm(message=f"yt2mp3  - {msg}", suffix="? (Y/n) > "))
    except KeyboardInterrupt:
        print("Quitting...")
        exit()
        
