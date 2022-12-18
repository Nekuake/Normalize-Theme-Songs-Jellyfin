import os
import fnmatch
from pydub import AudioSegment  #For information on how to set pydub up: https://github.com/jiaaro/pydub#installation

def gather_files(folder, pattern):
    file_list = []
    for root, dirs, files in os.walk(folder):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                file_list.append(filename)
    return file_list

def normalize_audio(file_list, percent):
    for file in file_list:
        audio = AudioSegment.from_file(file, format='mp3')
        normalized_audio = audio.normalize(headroom=percent)
        normalized_audio.export(file, format='mp3')
        print("Normalizing "+ file)

def main():
    folder = 'path/to/shows/folder'  #Remember to put three quotes if it's a Windows path
    pattern = 'theme.mp3'
    files = gather_files(folder, pattern)
    percent = 20.0
    normalize_audio(files, percent)

main()