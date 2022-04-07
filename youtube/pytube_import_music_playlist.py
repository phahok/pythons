# Install Pytube library
# pip install pytube

# Upgrade python pip
# /usr/bin/python3.6 -m pip install --upgrade pip

# DVD Jovem Novo
# https://www.youtube.com/playlist?list=PLdKdSz4_lV0rcBygal6Pb4CYL2YQDpNGK

from pytube import YouTube
from pytube import Playlist

import os

print("##YOUTUBE DOWNLOADS ##\n\nBaixe e converta videos Youtube \nBy José Renato Ferreira\n\n")

link = input("Insira o Link Playlist Music: ")

yt = Playlist(link)

for url in yt.video_urls:
    ys = YouTube(url)
    print("Titulo = ", ys.title)
    v = ys.streams.get_audio_only()
    out_file = v.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

print("Downloads concluidos!")
