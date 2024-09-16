#Crie um programa que use um loop while para verificar se um número fornecido pelo usuário é primo.

numero = int(input("Digite um numero para verificar se é primo: "))
divisor = 2
is_primo = True

while divisor <= numero // 2:
    if numero % divisor == 0:
        is_primo = False
        break
    divisor += 1

if is_primo and numero > 1:
    print(f"{numero} é um número primo")
else:
    print(f"{numero} não é um número primo")