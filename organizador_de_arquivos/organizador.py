import os
import tkinter as tk
from tkinter.filedialog import askdirectory

opt = int(input("O que gostaria de fazer? [ 1 - organizar] [ 2 - deletar]: "))
if opt == 1:
    #resolver crashs
    a = tk.Tk()

    print("Selecione o caminho que deseja organizar: ")
    caminho_downloads = askdirectory(title='Selecione a pasta que deseja organizar')

    lista_de_arquivos = os.listdir(caminho_downloads)

    locais = {
        'imagens': ['.png', '.jpeg', '.jpg', '.gif', '.ico'],
        'executáveis': ['.exe'],
        'planilhas': ['.xlsx', '.xls'],
        'pdfs': ['.pdf'],
        'compactados': ['.zip', '.rar', '.7z'],
        'html': ['.html', '.htm'],
        'documentos': ['.doc', '.docx', '.txt', '.rtf'],
        'apresentacoes': ['.ppt', '.pptx', '.key'],
        'textos': ['.txt', '.rtf'],
        'codigo': ['.py', '.java', '.cpp', '.html', '.css', '.js'],
        'configuracoes': ['.ini', '.cfg', '.json', '.yaml'],
        'dados': ['.csv', '.xml', '.json'],
        'audio': ['.mp3', '.wav', '.ogg', '.flac'],
        'video': ['.mp4', '.avi', '.mkv', '.mov'],
        'modelo': ['.docx', '.xlsx', '.pptx'],
        'backup': ['.bak', '.backup'],
        'log': ['.log'],
        'fonte': ['.ttf', '.otf'],
        'programa': ['.dll', '.lib'],
        'projeto': ['.proj', '.sln'],
        'instaladores': ['.msi'],
        'jar':['.jar'],
        'torrents': ['.torrent']
    }

    for arquivo in lista_de_arquivos:
        try:
            nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
            for pasta, extensoes in locais.items():
                if extensao_arquivo.lower() in extensoes:
                    pasta_destino = f'{caminho_downloads}/{pasta}'
                    if not os.path.exists(pasta_destino):
                        os.mkdir(pasta_destino)
                    destino_arquivo = f'{pasta_destino}/{arquivo}'
                    os.rename(f'{caminho_downloads}/{arquivo}', destino_arquivo)
                    break
        except PermissionError:
            print(f"Não foi possível processar o arquivo '{arquivo}' devido a permissões insuficientes.")
    a.destroy()

    #mover imagens
    a = tk.Tk()
    if 'imagens' in os.listdir(caminho_downloads):
        if len(os.listdir(f'{caminho_downloads}/imagens')) > 0:

            resposta = input('Gostaria de enviar as imagens para o arquivo de imagens? S / N: ')
            if resposta.lower().strip() == 's':
                imagens = os.listdir(f'{caminho_downloads}/imagens')
                caminho_imagens = askdirectory(title='Selecione a pasta de imagens')
                for imagem in imagens:
                    os.rename(f'{caminho_downloads}/imagens/{imagem}', f'{caminho_imagens}/{imagem}')     
        a.destroy()

else:

    quantidade = 0
    while True:
        quantidade = int(input("Quantos diretórios deletará?: "))
        if quantidade > 0:
            break

    for i in range(quantidade):
        a = tk.Tk()
        diretorio = askdirectory(title='Qual diretório deseja deletar?')
        print(f"Diretório a ser deletado: {diretorio}")
        certeza = input("Tem certeza?[s/n]: ")
        if certeza.lower() == 's':
            arquivos = os.listdir(diretorio)
            for i in arquivos:
                os.remove(f'{diretorio}/{i}')
            os.rmdir(diretorio)
        a.destroy()

        parar = input("Quer parar?[s/n]: ")
        if parar.lower() == 's':
            break