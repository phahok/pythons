from pytube import YouTube
from pytube.cli import on_progress

print("Baixe e converta videos Youtube \n By José Renato Ferreira\n")
link = input("Insira o link do video: ")

yt = YouTube(link, on_progress_callback = on_progress)

print("Titulo = ", yt.title)
print("Baixando...")

ys = yt.streams.get_highest_resolution()

ys.download()