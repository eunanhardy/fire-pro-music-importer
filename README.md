# Fire Pro Wrestling Music Importer

### This is designed to make it easy to import custom music into fire pro wrestling world.

Requirements

- Python3
- pip (https://pip.pypa.io/en/stable/installation/)
- ffmpeg (https://ffmpeg.org/download.html)
- Run as Admin (Used because we are writing files to the steam direcotry which is protected)

## Install Dependencies

```
pip install
```

## Import one song at a time

```
python3 main.py
Enter The Video URL: <URL>
Please enter a name to assign the file: <NameOfFile>
```

## Import Multiple Songs at Once

Import via file is supported by this script. please use example.csv as a template. Then run command:

```
python3 main.py --file=Example.csv
```
