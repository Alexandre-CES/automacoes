from PIL import Image
import math

def Main():

    image_file = input('Nome do arquivo da imagem: ')

    print('Qual filtro deseja?: ')
    print('[0]Cancelar - [1]Sobel')
    filter_opt = choose_opt(0,1)
    if filter_opt == 0:
        return

    # Carrega a imagem
    with Image.open(f'imagens/{image_file}') as img:

        img_result = None

        if filter_opt == 1:
            
            img_result = sobel(img)

        img_result.save('resultado.jpg')

def choose_opt(min,max):
    opt = 0
    while True:
        opt = int(input())
        try:
            if opt >= min and opt <= max:
                break
            else:
                print('Opção inválida, tente novamente: ')

        except ValueError:
            print('Opção inválida, tente novamente: ')

    return opt

def sobel(img):

    #grayscale
    img = img.convert('L')

    # Obtém os dados dos pixels da original
    pixels = img.load()

    # Obtém as dimensões da imagem
    largura, altura = img.size

    #Cópia da original
    img_result = Image.new('L', (largura, altura))
    pixels_result = img_result.load()
    
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

            pixels_result[x,y] = G
        
    return img_result

Main()