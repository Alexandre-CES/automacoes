from PIL import Image
import random

# Carrega a imagem
with Image.open('imagens/vermelho_azul.jpg') as img:

    # Obtém os dados dos pixels
    pixels = img.load()

    # Obtém as dimensões da imagem
    largura, altura = img.size

    for x in range(largura):
        for y in range(altura):
            r, g, b = pixels[x, y]

            min_color = min(r,g,b)
            max_color = max(r,g,b)

            #Quase um filtro de smurf

            if min_color == r and max_color == b:
                pixels[x,y] = (max_color, g, min_color)
            elif min_color == b and max_color == r:
                pixels[x,y] = (min_color, g, max_color)

            elif min_color == g and max_color == r:
                pixels[x,y] = (max_color, b, min_color)
            elif min_color == r and max_color == g:
                pixels[x,y] = (min_color, b, max_color)
             
            elif min_color == g and max_color == b:
                pixels[x,y] = (max_color, r, min_color)
            elif min_color == b and max_color == g:
                pixels[x,y] = (min_color, r, max_color)
            
            else:
                pixels[x,y] = (max_color, max_color, max_color)

    img.save('teste.jpeg')