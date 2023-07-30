from pytube import YouTube
import pytube.request
from tqdm import tqdm
from time import sleep

pytube.request.default_range_size = 5242880 # 5 mb chunk size

def progress_function(stream, chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining)/stream.filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50-progress)
    print('Downloading: [{}] {}%'.format(status, percent), end='\r')

def complete_function(stream, file_path):
    print('Download completed!')

# Get the audio stream
yt = YouTube('https://www.youtube.com/watch?v=gAsNvXDsrGA', on_progress_callback=progress_function, on_complete_callback=complete_function)
stream = yt.streams.filter(only_audio=True).first()

# Download the audio stream
stream.download(output_path='/home/jacob/Downloads')