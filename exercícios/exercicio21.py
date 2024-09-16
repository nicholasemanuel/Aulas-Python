#Faça um programa que peça a idade de 
# duas pessoas e determine quem é mais velho ou se têm a mesma idade.

idade1 = int(input("Idade da primeira pessoa: "))
idade2 = int(input("Idade da segunda pessoa: "))

if idade1 == idade2:
    print("As duas pessoas tem a mesma idade")
elif idade1 > idade2:
    print("A primeira pessoa é mais velha")
else:
    print("A segunda pessoa é mais velha")