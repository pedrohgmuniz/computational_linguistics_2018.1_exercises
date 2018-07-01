# palindromocomplexo.py
# Programa que testa uma palavra, frase ou expressao
# eh um palindromo: se a inversao de seus caracteres
# gera a mesma palavra, frase ou expressao
# Por: Pedro Muniz, Joao Vieira, Brenda Souza

def main ():
    print ("Cheque se uma palavra/termo/frase é a mesma coisa ao contrário!")
    palavra1 = input("Digite a palavra/termo/frase sem acento e sem pontuação: ")
    palavra1 = palavra1.lower().replace(" ", "")
    palavra2 = palavra1[::-1]
    if palavra1 == palavra2:
        print("Sim, é a mesma coisa, é um palíndromo!")
    else:
        print("Não, não é a mesma coisa, não é um palíndromo!")
            
main()


# teste que nao funcionou:
# print ("Cheque se a primeira palavra/termo/frase ao contrário é igual à segunda!")
#    palavra1 = input("Digite a primeira palavra/termo/frase sem acento e sem pontuação: ")
#    question = input("Quer comparar com uma segunda? [sim/não]: ")
#    if question in "sim":
#        palavra2 = input("Digite a segunda palavra/termo/frase sem acento e sem pontuação: ")
#        palavra1 = palavra1.lower().replace(" ", "")
#        palavra1 = palavra1[::-1]
#        palavra2 = palavra2.lower().replace(" ","")
#        if palavra1 == palavra2:
#            print("Sim, são palíndromos!")
#        else:
#            print("Não, não são palíndromos!")
#    if question not in "sim":
#        palavra3 = palavra1[::-1]
#        if palavra1 == palavra3:
#            print("Sim, são palíndromos!")
#        else:
#            print("Não, não são palíndromos!
