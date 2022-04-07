from pytube import YouTube
from pytube.cli import on_progress

import os

print("##YOUTUBE DOWNLOADS ##\n\nBaixe audios de videos Youtube \nBy José Renato Ferreira\n\n")

link = input("Insira o link do video: ")

yt = YouTube(link, on_progress_callback = on_progress)

print("Titulo = ", yt.title)
print("Baixando...")

ys = yt.streams.get_audio_only()
out_file = ys.download()
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

