# coding=utf-8
# lingua.py
# Por João Vieira

def main():
    print("Uma língua L1 é composta apenas pela vogal A e por todas as consoantes do Português.")
    print("Queremos saber se uma dada palavra pode fazer parte de L1.")
    print("L1 permite qualquer sequência de letras, de até 10 letras, contanto que façam parte do seu alfabeto.")
    palavra: str = input("Digite uma palavra para verificar se ela pode fazer parte de L1: ")
    letras = len(palavra)
    if letras <= 10:
        lingua = ["a", "b", "c", "ç", "d", "f", "g", "h", "j", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "z"]
        palavra = list(palavra)
        if all(elem in palavra for elem in lingua):
            print("Esse exemplo pode existir em L1!")
        else:
            print("O exemplo não pode existir em L1, pois apresenta elementos que não estão contidos em seu alfabeto!")
    else:
        print("O exemplo não pode existir em L1, pois possui mais de 10 caracteres.")


main()
