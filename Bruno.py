#Crie uma classe pai chamada Veiculo 
#     que tenha um método chamado descrever, o qual imprime "Este é um veículo". 
    
# Depois, crie duas subclasses: Carro e Moto. 

# Cada uma deve sobrescrever o método descrever para imprimir uma mensagem específica, 
#     como "Este é um carro" ou "Esta é uma moto".

class Veiculo:
    def Descrever(self):
        return 'Este é um veículo'
    
class Carro(Veiculo):
    def Descrever2(self):
        return 'Este é um carro'

class Moto(Veiculo):
    def Descrever2(self):
        return 'Esta é uma moto'
    
def trazer(descrito):
    return descrito.Descrever()


veiculo = Veiculo()
carro = Carro()
moto = Moto()

print(veiculo.Descrever())
print(carro.Descrever())
print(moto.Descrever())

print(trazer(veiculo),trazer(moto))