# dim2.py
# Programa que toma uma expressao longa (como uma frase ou um pequeno texto) como input
# e transforma apenas os diminutivos masculinos do portugues formal (como 'cachorrinho')
# em diminutivos coloquiais do falar nordestino (como 'cachorrim'), dando como output
# dando a expressao longa com os diminutivos transformados.
# Equipe: Pedro Muniz, Hélio Leonam, Adonis Sousa
# coding: utf-8

def main():
    print("Insira uma oração e transforme qualquer diminutivo masculino formal em uma versão informal.")
    frase: str = input("Digite a sua oração com ao menos uma palavra no diminutivo masculino: ")
    if "inho" in frase:
        frase = frase.replace("inho", "im")
        print("A frase ficou assim: ", frase)
    else:
        print("Deixe de onda, que nem tem diminutivo masculino na frase.")

main()


def sequence():
    question = input("Quer continuar? [sim/não]: ")
    while question in "sim":
        main()
        sequence()
    if question not in "sim":
        exit()

sequence()
