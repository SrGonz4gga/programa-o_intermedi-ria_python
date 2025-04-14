"""
painel.py

Módulo com uso básico de painéis (`Panel`) da biblioteca Rich.
Permite exibir textos dentro de caixas com bordas para destaque.

"""


from rich import print
from rich.panel import Panel
import os

def imprimeTexto(texto):
    """
    Exibe o texto do arquivo caso o parâmetro seja caminho de um. Exibe o texto do parâmetro caso contrário

    Parâmetros:
        texto(str): caminho para um arquivo ou um texto qualquer
    
    Retorna:
        None
    """
    if os.path.isfile(texto):
        with open (texto, "r" ,encoding = "utf=8") as arquivo:
            conteudo = arquivo.read()
            print(Panel(f"Hello, [bold red]{conteudo}[/bold red]!", title="Welcome", subtitle="Thank you"))
    else:
        print(Panel.fit(f"[red]'{texto}[/red]"))


def isArquivo(caminho):
    """
    Imprime na tela se a string passada como parâmetro é caminho para um arquivo ou não

    Parâmetros:
        caminho(str): caminho para um arquivo
    
    Retorna:
        None
    """
    if os.path.isfile(caminho):
        print(Panel.fit(f"[green]'{caminho}' é arquivo[/green]"))
    else:
        print(Panel.fit(f"[red]'{caminho}' não é arquivo[/red]"))

imprimeTexto("meuNome.txt")
isArquivo("meuNoe.txt")