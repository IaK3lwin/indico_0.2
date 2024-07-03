from pytube import YouTube
import os
class Functions:

    def load_thumb(url) -> str:
        return YouTube(url).thumbnail_url
    
    def download_mp3(self, url: str):
        video = YouTube(url)
        audio = video.streams.filter(only_audio=True).first()

        out_file = audio.download(output_path='Indico/downloadsMp3')

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    
    def download_mp4(self, url: str) -> str:
        video = YouTube(url).streams.filter(file_extension='mp4')
        #arquivo = video.first().download(output_path='Indico/downloadsMp4')
        return YouTube(url).thumbnail_url

Functions().download_mp4('https://youtu.be/I0Hj8vfscn0')