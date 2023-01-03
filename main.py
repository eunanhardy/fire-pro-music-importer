import click
from pytube import YouTube
from pydub import AudioSegment
import os
import sys
from platform import uname


def is_wsl() -> bool:
    return 'microsoft-standard' in uname().release

def path_file(ext,filename,root) -> str:
    return os.path.join(root,f'{filename}.{ext}')

def validateGamePath(bgm_path):
    if not os.path.isdir(bgm_path):
        alt_path = str(input("WARNING: We were unable to detect your music folder. Please paste the path in now. \n>>"))
    if os.path.isdir(alt_path):
        bgm_path = alt_path
    else:
        print("Could not locate direcotry. Exiting... soz")
        sys.exit()
def downloadFile(url,path):
    yt_ref = YouTube(url)
    audio_stream = yt_ref.streams.filter(only_audio=True).first()
    print(f'Video Found: {yt_ref.title}')
    print('Downloading....')
    download_file = audio_stream.download(output_path=path)
    print(f'download {yt_ref.title} - Complete')
    return download_file
    

def inline(bgm_path,padding):
    url = str(input("Enter The Video URL: \n>>"))
    input_filename = str(input("Please enter the name of the mp3 file you want to save to bgm folder: \n>>"))
    download_file = downloadFile(url,bgm_path)
    mp4_audio = AudioSegment.from_file(download_file,format="mp4")

    mp3_path = path_file("mp3",input_filename,bgm_path)
    silence = AudioSegment.silent(duration=padding*1000)
    full_track = AudioSegment.empty()
    full_track += silence + mp4_audio
    full_track.export(mp3_path,format="mp3")

    os.remove(download_file)
    print(f'audio saved to {mp3_path}')

def importFile(file):
    with open(file,"rw"):
        print("Hello")
    print("import file")

@click.command()
@click.option('--file',default=None,help="Import music to fire pro via csv file. Example of csv entry would look like \n<YOUTUBE_URL>, <NameOfFile>")
@click.option('--padding-length',default=1,help="Standard padding of 1 second of silance to ensure it sounds correct in game. Change to whatever you like,\n\n NOTE: does not apply for imports")
def run(file,padding_length):
    BGM_PATH = ""
    if not is_wsl():
        BGM_PATH = r"C:\\Program Files (x86)\Steam\steamapps\common\Fire Prowrestling World\BGM"
    else:
        BGM_PATH = r"/mnt/c/Program Files (x86)/Steam/steamapps/common/Fire Prowrestling World/BGM"
    
    if not None:
        importFile(file)
    
    inline(BGM_PATH,padding_length)
    

if __name__ == "__main__":
    run()