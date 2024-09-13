#CALCULADORA DE IMC

class CalculadoraIMC:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        if self.peso > 0 and self.altura > 0:
            imc = self.peso / (self.altura ** 2)
            return imc
        else:
            return "Dados inválidos: O peso e a altura devem ser maiores que zero."

    def interpretar_imc(self):
        imc = self.calcular_imc()
        if isinstance(imc, str):
            return imc
        elif imc < 18.5:
            return "Abaixo do peso"
        elif imc < 24.9:
            return "Peso saudável"
        elif imc < 29.9:
            return "Sobrepeso"
        elif imc < 34.9:
            return "Obesidade classe 1"
        elif imc < 39.9:
            return "Obesidade classe 2"
        else:
            return "Obesidade classe 3"

    def mostrar_resultado(self):
        imc = self.calcular_imc()
        interpretacao = self.interpretar_imc()
        if isinstance(imc, str):
            print(imc)
        else:
            print(f"Seu IMC é: {imc:.2f}")
            print(f"Interpretação: {interpretacao}")

if __name__ == "__main__":
    peso = float(input("Informe o seu peso em quilogramas: "))
    altura = float(input("Informe a sua altura em metros: "))

    calculadora = CalculadoraIMC(peso, altura)
    calculadora.mostrar_resultado()