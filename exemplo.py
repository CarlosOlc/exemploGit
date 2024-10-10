class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return 'aaaa'

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca


def fazer_falar(bixo):
    return bixo.falar()


animal = Animal("bb", 11)   
cachorro = Cachorro("Rex", 11, "aaaa")
gato = Gato("Rex", 11, "aaaa")

print(fazer_falar(animal))
print(fazer_falar(cachorro))
print(fazer_falar(gato))