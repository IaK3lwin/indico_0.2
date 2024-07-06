import flet as ft

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

    

system_current: str = Functions.get_sistem().lower()
user_name: str = Functions.get_name_user()
caminho:str = ''
folder_path: str = 'undefined'
items = []
print(system_current)


#storage/emulated/0/Music

def main(page: ft.Page):
    
    #configuração do app
    #tamanho da tela
    page.window_width = 320
    page.window_height = 480


    #titulo do app
    page.title = "Indico interface placehold"
    # alinhamento
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    #funções necessárias:
    def check_path():
        if mp3_selection.value:
            folder_path = 'Music/Indigo'
        elif mp3_selection.value == False:
            folder_path = 'Video'
    def say_error(text:str):
        page.title = text
        page.update()
    #Eventos:
    def download_file(e):
        if mp3_selection.value:
            folder_path = 'Music/Indigo'
        elif mp3_selection.value == False:
            folder_path = 'Video'
        try:
            if system_current == 'windows':
                caminho = f'C:/Users/{user_name}/{folder_path}'
            else:
                caminho = 'storage/emulated/0/Music'
                if folder_path == 'Video':
                    caminho = 'storage/emulated/0/DCIM/Indigo'
            
            #baixando.....
            if mp3_selection.value:
                if url_field.value != '':
                    Functions.download_mp3(url_field.value, caminho)
                    items.append(ft.Text('download iniciado', color='#008000'))
                    page.add(
                        ft.ListView(items, auto_scroll=True)
                    )
                    page.update()
                else:
                    say_error("url vazia")
            elif mp4_selection.value:
                if url_field.value != '':
                    Functions.download_mp4(url_field.value, caminho)
                    items.append(ft.Text('download iniciado', color='#008000'))
                    page.add(
                        ft.ListView(items, auto_scroll=True)
                    )
                    page.update()
                else:
                    say_error("url vazia")
            else:
                say_error('selecione entre mp4 ou mp3')
        except:
            page.tittle = 'ocorreu um erro ao baixar'
    
    def update_tumb(e):
        try:
            capa_video.src = Functions.load_thumb(url_field.value)
            page.update()
        except:
            url_field.hint_text = 'Url Invalida'
        
    
    #construindo a interface
    #controllers | widget
    #seleção:
    title_options = ft.Text('escolha entre: ', size = 20, weight = ft.FontWeight.BOLD)
    mp4_selection = ft.Checkbox(label = 'mp4')
    mp3_selection = ft.Checkbox(label = 'mp3')
    url_field = ft.TextField(hint_text = 'Insira a URL aqui!',
        height = 50, width = 150, on_change=update_tumb, multiline=False)
    capa_video = ft.Image(src = 'tumb.jpg', width = 200, height = 150)
    bt_download = ft.ElevatedButton(text = 	'Download', on_click=download_file,
                                    icon=ft.Icon(ft.icons.DOWNLOAD))
    #container armazena a HOME
  
    page.add(
            ft.Row(
				[title_options],
				alignment = ft.MainAxisAlignment.CENTER
				),
			ft.Row(
				[mp4_selection, mp3_selection],alignment = ft.MainAxisAlignment.CENTER
				),
			ft.Row(
				[url_field],
				alignment = ft.MainAxisAlignment.CENTER
				),
			ft.Row(
				[capa_video],
				alignment = ft.MainAxisAlignment.CENTER
				),
			ft.Row(
				[bt_download],
				alignment = ft.MainAxisAlignment.CENTER
				)
		)
    page.add(
        ft.Row(
            [ft.Text(
                f'using: {system_current}',
                text_align=ft.TextAlign.START,
                color='#4F4F4F'
                )],
            alignment=ft.MainAxisAlignment.START
        )
    )
ft.app(target = main)