"""
estilo.py

Módulo com aplicações básicas de estilo usando a biblioteca Rich.
Aplica cores simples e estilos como negrito ou itálico a textos impressos no terminal.

"""


import os
from rich.console import Console

console = Console()

def imprimeTexto(texto):
    """
    Exibe o texto do arquivo caso o parâmetro seja caminho de um. Exibe o texto do parâmetro caso contrário

    Parâmetros:
        texto(str): caminho para um arquivo ou um texto qualquer
    
    Retorna:
        None
    """
    if os.path.isfile(texto):
        with open(texto, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            console.print(conteudo, style="green")
    else:
        console.print(texto, style="red")

def isArquivo(caminho):
    """
    Imprime na tela se a string passada como parâmetro é caminho para um arquivo ou não

    Parâmetros:
        caminho(str): caminho para um arquivo
    
    Retorna:
        None
    """

    if os.path.isfile(caminho):
        console.print(f"'{caminho}' é Arquivo", style="green")
    else:
        console.print(f"'{caminho}' não É Arquivo", style = "red")

print(imprimeTexto.__doc__)
imprimeTexto("Nome.txt")
isArquivo("meuNome.txt")