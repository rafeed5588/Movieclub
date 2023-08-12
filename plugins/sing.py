from pytube import YouTube
from yt_dlp import YoutubeDL



class Descargar:

    def __init__(self,path) -> None:
        self.path = path
    
    def get_song(self,link:str):
        '''Download mp3 songs from youtube [Pytube]'''
        
        yt = YouTube(
            url=link
        )

        opts = {
            'format': 'bestaudio',
            'quiet' : True,
            'outtmpl':f'{self.path}{yt.title.replace("/","|")}-{yt.video_id}.mp3'
        }


        with YoutubeDL(opts) as dl:
            dl.download([link])

        return yt
