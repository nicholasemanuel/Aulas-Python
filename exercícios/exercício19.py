#Escreva um programa que peça ao usuário para digitar seu nome e sua idade
#e exiba uma mensagem formatada usando .format().

nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))

mensagem = "Olá, {}! você tem {} anos de idade".format(nome, idade)

print(mensagem)