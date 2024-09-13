#Faça um programa para uma loja de tintas 
#O prgrama deverá pedir o tamanho em m² da área a ser pintada
#Considere que a cobertura da tinta é 1 litro para cada 6m²
#A tinta é vendida em latas de 18L, que custam R$80,00 
#Ou em galões de 4 litros, que custam R$25,00


#Informe ao usuario as quantidades de latas de tinta a serem compradas e os respectivos preços em 3 situações
    #Comprar apenas latas de 18L;
    #Comprar apenas galões de 4L;
    #Misturar latas e galões, de forma que o preço seja menor

#______________________________________________________________

area = int(input("Qual o tamanho da área desejada?"))

#Adição de 10% à área em m²
area = area + area * 0.1
if area > int(area):
    area = int(area) + 1
else:
    area = int(area)
print("Caso seja acrescentado os 10% de folga teremos", area, "m²\n")

#Calculo litros
litros = area // 6
if area % 6 >= 1:
    litros + 1
print("Para pintar",area, "m² são necessários", litros, "litros de tinta\n")
print("="*30,"\n")

#Calculo latas
latas = litros // 18
if litros % 18 >= 1:
    latas = latas + 1
a = "1ª opção:", latas,"latas de tinta | Valor total R$" ,latas*80.0
print(a)

#Calculo galões
galoes = litros // 4
if litros % 4 >= 1:
    galoes = galoes + 1
b = "2ª opção:", galoes,"galoes de tinta | Valor total R$" ,latas*25.0
print(b)

#Excesso das latas
latas1 = litros // 18
galoes1 = 0
excesso = litros % 18

if excesso <= 3 * 4:
    galoes1 = excesso // 4
    if excesso % 4 > 0:
        galoes1 = galoes + 1
else:
    latas1 = latas1 + 1

c = "3ª opção:" , latas1, "latas e" , galoes1, "galões | Valor total R$" ,galoes1*25.0 + latas1*80.0
print(c)
print("\n", "=" * 30, "\n")
