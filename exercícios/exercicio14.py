#criar a classe carro e ter no minimo 3 propriedades e no minimo 3 metodos

class Carro:
    def __init__(self, marca, tipo, cor):
        self.marca = marca
        self.tipo = tipo
        self.cor = cor

    def Ligar(self):
        print("VRUM, estou ligado")

    def Status(self):
        print(self.marca, self.tipo, self.cor)

    def Desligar(self):
        print("Estou desligadno")

carro1 = Carro("Toyota", "Elétrico", "Azul")
carro1.Ligar()
carro1.Status()
carro1.Desligar()