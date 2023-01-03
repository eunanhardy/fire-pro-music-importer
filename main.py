from pytube import YouTube
from pydub import AudioSegment
import os
import sys
from platform import uname

def is_wsl() -> bool:
    return 'microsoft-standard' in uname().release

def path_file(ext,filename,root) -> str:
    return os.path.join(root,f'{filename}.{ext}')

if not is_wsl():
    BGM_PATH = r"C:\\Program Files (x86)\Steam\steamapps\common\Fire Prowrestling World\BGM"
else:
    BGM_PATH = r"/mnt/c/Program Files (x86)/Steam/steamapps/common/Fire Prowrestling World/BGM"

yt_ref = YouTube(str(input("Enter The Video URL: \n>>")))
audio_stream = yt_ref.streams.filter(only_audio=True).first()
print(audio_stream)

print(f'Video Found: {yt_ref.title}')
input_filename = str(input("Please enter the name of the mp3 file you want to save to bgm folder: \n>>"))

if not os.path.isdir(BGM_PATH):
    alt_path = str(input("WARNING: We were unable to detect your music folder. Please paste the path in now. \n>>"))
    if os.path.isdir(alt_path):
        BGM_PATH = alt_path
    else:
        print("Could not locate direcotry. Exiting... soz")
        sys.exit()


mp3_path = path_file("mp3",input_filename,BGM_PATH)

download_file = audio_stream.download(output_path=BGM_PATH)
mp4_audio = AudioSegment.from_file(download_file,format="mp4")


silence = AudioSegment.silent(duration=1000)
full_track = AudioSegment.empty()
full_track += silence + mp4_audio
full_track.export(mp3_path,format="mp3")

os.remove(download_file)


print(f'audio saved to {mp3_path}')

