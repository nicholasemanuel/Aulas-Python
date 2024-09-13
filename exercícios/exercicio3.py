#Faça um programa que peça 4 notas bimestrais e mostre a média

nota1 = float(input("Digite a nota do seu primeiro bimestre: "))
nota2 = float(input("Digite a nota do seu segundo bimestre: "))
nota3 = float(input("Digite a nota do seu terceiro bimestre: "))
nota4 = float(input("Digite a nota do seu quarto bimestre: "))

calculo_media = (nota1 + nota2 + nota3 + nota4) // 4

print("Sua média final foi", calculo_media)
