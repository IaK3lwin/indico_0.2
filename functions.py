from pytube import YouTube

import os

from platform import system

class Functions:

    def get_name_user() -> str:
        return os.getlogin()

    def get_sistem() -> str:
        return system()

    def load_thumb(url) -> str:
        try:
            return YouTube(url).thumbnail_url
        except 'pytube.exceptions.RegexMatchError':
            print('deu errado')
    
    def download_mp3(url: str, caminho: str) -> str:
        print(f'iniciou download mp3 no caminh0: {caminho}')
        try:
            video = YouTube(url)
            audio = video.streams.filter(only_audio=True).first()

            out_file = audio.download(output_path=caminho)

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(F'FINALIZADO: {caminho}')
        except:
            return 'ocorreu um erro!'
    
    def download_mp4(url: str, caminho) -> str:
        print(f'iniciou download mp4 no caminh0: {caminho}')
        try:
            video = YouTube(url).streams.filter(file_extension='mp4')
            video.first().download(output_path=caminho)
            print(F'FINALIZADO: {caminho}')
        except:
            return 'ocorreu um erro!'
