import argparse
import os

MODULOS_DISPONIVEIS = {
    "layout": ["layout", "id:1"],
    "painel": ["painel", "id:2"],
    "progresso": ["progresso", "id:3"],
    "estilo": ["estilo", "id:4"]
}

parser = argparse.ArgumentParser(description = "Imprime o texto passado como parâmetro usando os módulos do pacote personalizador.")

parser.add_argument("texto", help = "Texto ou caminho para o arquivo de texto")
parser.add_argument("-a", "--arquivo", action = "store_tue", help = "O texto será tratado como caminho para arquivo.")

modulos_str = ", ".join([f"{k} (id: {MODULOS_DISPONIVEIS[k][1].split(':')[1]})" for k in MODULOS_DISPONIVEIS])
parser.add_argument("-m", "--modulo", help = f"Escolhe o módulo a ser usado. Opções: {modulos_str}")

funcoes_str = ", ".join([f"{MODULOS_DISPONIVEIS[k][0]} (mod: {k})" for k in MODULOS_DISPONIVEIS])
parser.add_argument("-f", "--funcao", help = f"Escolhe a função a ser usada. Opções: {funcoes_str}")

args = parser.parse_args()


print(args.argumento1, args.argumento2, args.flag)