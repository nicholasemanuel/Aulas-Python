#Exercicio 13 | Classes e funções

#Marca, memoria ram, placa de video

class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def Ligar(self):
        print("estou ligado")
    
    def Desligar(self):
        print("estou desligado")

    def ExibirConfig(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = Computador("Asus", "16GB", "NVIDIA")
computador1.Ligar()
computador1.Desligar()
computador1.ExibirConfig() 

#ligar, desligar, exibir config