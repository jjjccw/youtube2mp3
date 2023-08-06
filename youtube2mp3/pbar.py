"""Simple progress bar wrapper for youtube2mp3"""

from tqdm import tqdm

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