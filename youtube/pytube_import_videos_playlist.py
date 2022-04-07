from pytube import YouTube
from pytube import Playlist

from pytube.cli import on_progress

print("##YOUTUBE DOWNLOADS ##\n\nBaixe e converta videos Youtube \nBy José Renato Ferreira\n\n")

link = input("Insira o link playlist de videos: ")

yt = Playlist(link)

for url in yt.video_urls:
    ys = YouTube(url)
    print("Titulo = ", ys.title)
    v = ys.streams.get_highest_resolution()
    v.download()
    print("Baixando...")
