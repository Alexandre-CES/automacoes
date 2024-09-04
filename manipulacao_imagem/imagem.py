from PIL import Image
import math

def Main():
    # Carrega a imagem
    with Image.open('imagens/arvore.jpg') as img:

        img = img.convert('L')

        # Obtém os dados dos pixels da original
        pixels = img.load()

        # Obtém as dimensões da imagem
        largura, altura = img.size

        Gx = [
            [1,0,-1],
            [2,0,-2],
            [1,0,-1]
        ]

        Gy = [
            [1,2,1],
            [0,0,0],
            [-1,-2,-1]
        ]

        #Para não alterar a original
        img_resultado = Image.new('L', (largura, altura))
        pixels_resultado = img_resultado.load()

        #iterar sob todos os pixels da imagem
        for y in range(1,altura - 1):
            for x in range(1,largura - 1):
                GxSum = 0
                GySum = 0

                #captar pixels adjacentes
                for i in range(3):
                    for j in range(3):
                        GxSum += Gx[i][j] * pixels[x + j - 1, y + i - 1]
                        GySum += Gy[i][j] * pixels[x + j - 1, y + i - 1]

                G = math.sqrt(GxSum**2 + GySum**2)

                G = int(G / math.sqrt(2 * (255**2)) * 255)

                pixels_resultado[x,y] = G

        img_resultado.save('arvore_sobel.jpg')

Main()