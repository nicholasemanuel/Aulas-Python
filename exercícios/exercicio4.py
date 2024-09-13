#Faça um programa que pergunte quanto você ganha por hora e o numero de horas trabalhados
#Calcule e mostre o total do seu salário no referido mês

valor_hora_trab = int(input("Digite o valor da hora trabalhada :"))
valor_hora_mes = int(input("Digite o número de horas trabalhadas no mês :"))

salario_mensal = valor_hora_trab * valor_hora_mes

print("Você ganha", salario_mensal, "por mês: ")

