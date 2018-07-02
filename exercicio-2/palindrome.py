# palindrome.py
# Simple program for detecting if a word is a palindrome, that is,
# if it can can be read the same way backward or forward.
# By Joao Vieira, Pedro Muniz, 
def main ():
    print ("This program checks whether any given word is a palindrome, that is, whether it can be read the same way backward or forward!")
    word1 = input("Type the word: ")
    word2 = word1[::-1]
    if word1 == word2:
        print("The word is a palindrome!")
    else:
        print("Nope, the word isn't a palindrome! :(")

main()
