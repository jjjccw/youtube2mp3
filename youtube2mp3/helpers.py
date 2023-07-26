from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import confirm
from prompt_toolkit.patch_stdout import patch_stdout

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
        
# def on_progress(vid, chunk, bytes_remaining):
    # total_size = vid.filesize
    # bytes_downloaded = total_size - bytes_remaining
    # percentage_of_completion = bytes_downloaded / total_size * 100
    # totalsz = (total_size/1024)/1024
    # totalsz = round(totalsz,1)
    # remain = (bytes_remaining / 1024) / 1024
    # remain = round(remain, 1)
    # dwnd = (bytes_downloaded / 1024) / 1024
    # dwnd = round(dwnd, 1)
    # percentage_of_completion = round(percentage_of_completion,2)
# 
    print(f'Total Size: {totalsz} MB')
    # print(f'Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: {dwnd} MB, Remaining:{remain} MB')


