"""
progresso.py

Módulo com uma implementação simples de barra de progresso usando Rich.
Mostra o andamento de tarefas de forma visual no terminal.

"""


import time
import os

from rich.progress import track

def imprimeTexto(texto):
    """
    Simula o carregamento e leitura de um arquivo caso o parâmetro seja caminho para um. Exibe o texto do parâmetro caso contrário.

    Parâmetros:
        texto(str): caminho para um arquivo ou um texto qualquer
    
    Retorna:
        None
    """

    if os.path.isfile(texto):
        with open(texto, "r", encoding="utf-8")as arquivo:
            conteudo = arquivo.read()
            for i in track(range(4), description="Opening..."):
                time.sleep(0.5)
            for i in track(range(2), description="Reading..."):
                time.sleep(0.5)
            print(conteudo)
    else:
        print(texto)

def isArquivo(caminho):
    """
    Imprime na tela se a string passada como parâmetro é caminho para um arquivo ou não

    Parâmetros:
        caminho(str): caminho para um arquivo
    
    Retorna:
        None
    """
    if os.path.isfile(caminho):
        for i in track(range(2), description="Reading..."):
            time.sleep(0.5)
        print(f"'{caminho}' é Arquivo")
    else:
        print(f"'{caminho}' não é Arquivo")

isArquivo("meuNome.txt")
imprimeTexto("meuNome.txt")
