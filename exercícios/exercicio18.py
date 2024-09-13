#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';


#Validação do nome
while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    else:
        print("Erro. Seu nome deve conter mais de 3 caracteres")
        
#Validação da idade
while True:
    idade = int(input("Digite sua idade: "))
    if idade > 0 and idade <= 150:
        break
    else:
        print("Idade inválida. Por favor digite novamente")
        
#Validação do salário
while True:
    salario = float(input("Digite seu salário: "))
    if salario > 0:
        break
    else:
        print("Salário inválido. Por favor digite um número maior que zero")
    
#Validação do sexo
while True:
    sexo = input("Digite seu sexo (f ou m): ")
    if sexo in ("f", "m"):
        break
    else:
        print("Sexo inválido. Digite novamente")
        
#Validação estado civíl
while True:
    estado_civil = input("Digite seu estado civíl (s, c, v, d): ")
    if estado_civil in ('s', 'c', 'v', 'd'):
        break
    else:
        print("Estado civil inválido. Insira 's' para solteiro, 'c' para casado, 'v' para viúvo ou 'd' para divorciado.")
        
#Exibir informações
print("\nInformações válidas:")
print("Nome:", nome)
print("Idade:", idade)
print("Salário:", salario)
print("Sexo:", sexo)
print("Estado Civil:", estado_civil)