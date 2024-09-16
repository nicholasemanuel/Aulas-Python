#Formatação de Strings I: Função f-string | Aula 07

nome = "Nicholas Emanuel"
altura = 1.70
peso = 67
imc = peso / altura ** 2

#Sempre que tiver um f antes de Strings, ele é chamado de f-strings ou format string
linha_1 = f"{nome} tem {altura:.2f} de altura, "
linha_2 = f"pesa {peso} kgs e seu imc é"
linha_3 = f"{imc:.2f}"

print(linha_1)
print(linha_2)
print(linha_3)

