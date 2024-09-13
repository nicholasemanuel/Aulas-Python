nome = str(input("Qual seu nome? "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc_calculo = peso // altura ** 2

print("Seu peso é:", imc_calculo)

