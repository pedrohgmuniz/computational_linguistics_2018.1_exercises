# diminutivo1.py
# Por João Vieira 8-)
# Simples programa que transforma diminutivos em linguagem formal (como "garotinho")
# em diminutivos na linguagem coloquial de certos dialetos cearences ("garotim")

def main():
        print("Transforma um diminutivo masculino formal em sua forma coloquial.")
        word = input("Escreva uma palavra no diminutivo masculino: ")
        for i in word:
            if word[-4::] == "inho":
                word2 = word [0:-4]
                word2 = ''.join((word2,'im'))
                print("O diminutivo informal de", word, "é", word2)
                break;
            else:
                print("Ó a putaria, mah! Isso lá é diminutivo que sirva! Tem que ser um diminutivo masculino!")
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