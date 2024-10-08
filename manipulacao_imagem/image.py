from PIL import Image
import math

def Main():

    img_file = input('Nome do arquivo da imagem: ')

    print('Qual filtro deseja?: ')
    print('[0]Cancelar - [1]Suavizar - [2]Sobel - [3]Inverter - [4]Vermelho - [5]Sepia')
    filter_opt = choose_opt(0,5)
    if filter_opt == 0:
        return

    # Carrega a imagem
    with Image.open(f'images/{img_file}') as img:

        img_result = None
        img_file_name = img_file.split('.')[0]
        effect_name = None

        if filter_opt == 1:
            img_result = smooth(img)
            effect_name = 'suavizar'
        elif filter_opt == 2:
            img_result = sobel(img)
            effect_name = 'sobel'
        elif filter_opt == 3:
            img_result = invert(img)
            effect_name = 'inverter'
        elif filter_opt == 4:
            img_result = turn_red(img)
            effect_name = 'vermelho'
        elif filter_opt == 5:
            img_result = sepia(img)
            effect_name = 'sepia'

        img_result.save(f'resultados/{img_file_name}-{effect_name}.jpg')

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

def smooth(img):

    # Obtém os dados dos pixels da original
    pixels = img.load()

    # Obtém as dimensões da imagem
    width, height = img.size

    #Cópia da original
    img_result = Image.new('RGB', (width, height))
    pixels_result = img_result.load()

    for y in range(1,height - 1):
        for x in range(1,width - 1):
            sum_r, sum_g, sum_b = 0,0,0
            for i in range(3):
                for j in range(3):
                    r, g, b = pixels[x + j - 1, y + i - 1]
                    sum_r += r
                    sum_g += g
                    sum_b += b

            pixels_result[x, y] = (int(sum_r / 9), int(sum_g / 9), int(sum_b / 9))

    return img_result

def sobel(img):

    #grayscale
    img = img.convert('L')

    # Obtém os dados dos pixels da original
    pixels = img.load()

    # Obtém as dimensões da imagem
    width, height = img.size

    #Cópia da original
    img_result = Image.new('L', (width, height))
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
    for y in range(1,height - 1):
        for x in range(1,width - 1):
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

def invert(img):
    # Obtém os dados dos pixels da original
    pixels = img.load()

    # Obtém as dimensões da imagem
    width, height = img.size

    #Cópia da original
    img_result = Image.new('RGB', (width, height))
    pixels_result = img_result.load()

    for y in range(1,height - 1):
        for x in range(1,width - 1):  
            r,g,b = pixels[x,y]
            pixels_result[x,y] = (255 - r, 255 - g, 255 - b)

    return img_result

def turn_red(img):
    # Obtém os dados dos pixels da original
    pixels = img.load()

    # Obtém as dimensões da imagem
    width, height = img.size

    #Cópia da original
    img_result = Image.new('RGB', (width, height))
    pixels_result = img_result.load()

    for y in range(1,height - 1):
        for x in range(1,width - 1):  
            r,g,b = pixels[x,y]

            r = max(r,g,b)

            gb_color = max(max(g,b) - 100, 0)

            pixels_result[x,y] = (r,gb_color,gb_color)

    return img_result

def sepia(img):
    # Obtém os dados dos pixels da original
    pixels = img.load()

    # Obtém as dimensões da imagem
    width, height = img.size

    #Cópia da original
    img_result = Image.new('RGB', (width, height))
    pixels_result = img_result.load()

    for y in range(1,height - 1):
        for x in range(1,width - 1):  
            r, g, b = pixels[x, y]
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            pixels_result[x, y] = (min(tr, 255), min(tg, 255), min(tb, 255))

    return img_result


Main()