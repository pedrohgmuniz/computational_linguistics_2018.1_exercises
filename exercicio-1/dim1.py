# dim1.py
# Programa simples que transforma diminutivos em linguagem formal (como "garotinho")
# em diminutivos na linguagem coloquial do falar nordestino (como "garotim")
# O programa toma como input apenas palavras no diminutivo formal,
# o output deve ser o equivalente no diminutivo informal do falar nordestino
# Equipe: Pedro Muniz, Hélio Leonam, Adonis Sousa
# coding: utf-8

def main():
        print("Este programa transforma um diminutivo masculino formal (por exemplo: 'cachorrinho') em sua forma "
              "coloquial do falar nordestino ('cachorrim').")
        word: str = input("Escreva uma palavra no diminutivo masculino formal (tipo 'cachorrinho'): ")
        _: str
        for _ in word:
            if word[-4::] == "inho":
                word2 = word[0:-4]
                word2 = ''.join((word2, 'im'))
                print("O diminutivo informal de", word, "é", word2, '.')
                break;
            else:
                print("Parece que você não digitou um diminutivo masculino na linguagem formal! Mas não entre em "
                      "pânico! Você pode tentar novamente.")
                break;

main()


def sequence():
        question = input("Quer tentar de novo? [sim/não]: ")
        while question in "sim":
            main()
            sequence()
        if question not in "sim":
            exit()

sequence()