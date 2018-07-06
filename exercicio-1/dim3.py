# dim3.py
# Programa simples que toma como entrada um diminutivo masculino no falar nordestino
# (por exemplo: sorvetim) e retorna como saída a forma do diminutivo padrão
# (no exemplo: sorvetinho)
# Modificado a partir de diminutivo_sentence.py, por Katiusha de Moraes
# Equipe: Pedro Muniz, Hélio Leonam, Adonis Sousa
# coding: utf-8

def main():
    print("Transforma um diminutivo masculino no falar nordestino (como 'sorvetim') para a sua forma padrão ('sorvetinho').")
    reverse: str = input("Insira uma palavra no diminutivo masculino do falar nordestino: ")
    for _ in reverse:
        if reverse[-2::] == "im":
            palavra = reverse[0:-2]
            palavra = ''.join((palavra, 'inho'))
            dict = open("deadjectivals.mbr.dict.txt","r")
            check = dict.read()
            dict2 = open("denominals.mbr.dict.txt", "r")
            check2 = dict2.read()
            if palavra in check or check2:
                print("A forma padrão do diminutivo", reverse, "é", "'", palavra, "'")
                break;
            else:
                print("Você não inseriu um diminutivo.")
                break;
        else:
            print("Você não inseriu um diminutivo masculino do falar nordestino. Você pode tentar de novo, se quiser.")
            break;


main()


def sequence():
    question = input("Quer continuar? [sim/não]: ")
    while question in "sim":
        main()
        sequence()
    if question not in "sim":
        exit()

sequence()