"""
layout.py

Módulo com funções básicas de layout usando a biblioteca Rich.
Usa o componente `Layout` para dividir o terminal em seções simples.

"""


from rich import print
from rich.layout import Layout
from rich.panel import Panel
import os

layout = Layout()

layout.split_column(
    Layout(name="bloco")
)

def imprimeTexto (texto):
    if os.path.isfile(texto):
        with open(texto, "r", encoding = "utf-8") as arquivo:
            conteudo = arquivo.read()
            layout["bloco"].update(conteudo)
            
    else:
        layout["bloco"].update(texto)

print(layout)



imprimeTexto("ArquivoTeste.txt")