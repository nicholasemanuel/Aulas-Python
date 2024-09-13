#Estrutura de decisões I: If e Else | Aula 05

idade = int(input("Digite sua idade: "))
resp = idade >= 18

if idade >= 18:
    print("Você pode beber o quanto quiser")
    if idade >= 20:
        print("Você é V.I.P.")

else:
    print("Você só pode beber refrigerante")