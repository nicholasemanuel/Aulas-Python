#Escreva um programa que peça duas palavras ao usuário e compare o tamanho (número de caracteres) 
# de cada uma delas

word_1 = input("Digite a primeira palavra: ")
word_2 = input("Digite a segunda palavra: ")

if len(word_1) == len(word_2):
    print("Elas são do mesmo tamanho")
elif len(word_1) > len(word_2):
    print("A primeira palavra é maior")
else:
    print("A segunda palavra é maior")