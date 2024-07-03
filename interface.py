from functions import Functions

import flet as ft

def main(page: ft.Page):

    #configuração do app
    #tamanho da tela
    page.window_width = 320
    page.window_height = 480


    #titulo do app
    page.title = "Indico interface placehold"
    # alinhamento
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    #funcionalidades:
    def download_file(e):
        pass
    def update_tumb(e):
        capa_video.src = Functions.load_thumb(url_field.value)
        page.update()
        print(url_field.value)
    #construindo a interface
    #controllers | widget
    #seleção:
    title_options = ft.Text('escolha entre: ', size = 20, weight = ft.FontWeight.BOLD)
    mp4_selection = ft.Checkbox(label = 'mp4')
    mp3_selection = ft.Checkbox(label = 'mp3')
    url_field = ft.TextField(hint_text = 'Insira a URL aqui!',
        height = 35, width = 150, on_change=update_tumb)
    capa_video = ft.Image(src = 'tumb.jpg', width = 200, height = 150)
    bt_download = ft.ElevatedButton(text = 	'Download', on_click=download_file)

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
ft.app(target = main)