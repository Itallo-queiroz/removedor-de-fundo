from rembg import remove
from PIL import Image
import flet as ft
import os

def main(page: ft.Page):
    page.title = "Removedor de Fundo de Imagem"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    campo_imagem = ft.TextField(
        label='Informe o nome da imagem com a extensão (ou "Enter" para encerrar):',
        width=400
    )

    def acao(e):
        imagem = campo_imagem.value
        if imagem:
            try:
                # Verifica se o arquivo existe
                if not os.path.exists(imagem):
                    page.add(ft.Text('Erro: A imagem não foi encontrada.', color='red'))
                    page.update()
                    return

                # Prepara o nome da nova imagem
                nova_img = f'nova_{imagem}'
                
                # Abre a imagem original
                original = Image.open(imagem)
                
                # Remove o fundo
                img_sem_fundo = remove(original, bgcolor=(255, 255, 255, 255))
                
                # Salva a nova imagem
                img_sem_fundo.save(nova_img)
                page.add(ft.Text(f'Imagem salva como: {nova_img}', color='green'))
            except Exception as ex:
                page.add(ft.Text(f'Erro: {ex}', color='red'))
        else:
            page.add(ft.Text('Por favor, informe um nome de imagem.', color='red'))

        campo_imagem.value = ""  # Limpa o campo após a ação
        page.update()

    botao = ft.ElevatedButton(
        'Retirar fundo',
        bgcolor='green',
        color='white',
        elevation=10,
        on_click=acao
    )

    page.add(
        ft.Row(
            [ft.Text('Removedor de fundo!', size=40, weight='bold')],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        campo_imagem,
        ft.Row(
            [botao],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.update()

ft.app(main)

