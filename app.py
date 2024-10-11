from rembg import remove
from PIL import Image

while True:
    try:
        imagem = input('Informe o nome da imagem com a extenção ou "enter" para encerrar o programa.')
        if imagem:
            nova_img = f"nova_{imagem}.png"
            original = Image.open(imagem)
            img_sem_fundo = remove(original)
            img_sem_fundo.save(nova_img)
            continue
        else:
            ...
    except Exception as e:
        print(f'Não foi possivel remover a imagem. {e}. ')
    finally:
        break