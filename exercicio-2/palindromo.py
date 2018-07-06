# palindromo.py
# Programa que detecta se duas palavras sao palindromos:
# se a primeira palavra eh o contrario da segunda
# Por: João Vieira

def main ():
    print ("Cheque se a primeira palavra ao contrário é igual à segunda palavra!")
    palavra1 = input("Digite a primeira palavra: ")
    palavra2 = input("Digite a segunda palavra: ")
    palavra1 = list(palavra1)
    palavra1 = palavra1[::-1]
    palavra1 = ''.join(palavra1)
    if palavra1==palavra2:
        print("O inverso da primeira é igual à segunda!")
    else:
        print("Não, a primeira palavra não é o inverso da segunda!")
        
main()
