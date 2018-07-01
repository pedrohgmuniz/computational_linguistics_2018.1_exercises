# diminutivo.py
# Programa que toma uma expressao longa (como uma frase ou um pequeno texto) como input
# e transforma apenas os diminutivos masculinos do portugues formal (tipo 'cachorrinho')
# em diminutivos coloquiais (tipo 'cachorrim'), dando a expressao longa com os diminutivos
# transformados como output
# Por: Joao Vieira, Pedro Muniz,
# thanks and good night

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
