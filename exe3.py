# Implemente uma classe base chamada Animal, 
#     que tenha um método falar(). 
    
# Crie três subclasses: Gato, Cachorro e Vaca, 
#     cada uma com sua própria implementação do método falar() 
    
# (ex: o cachorro deve latir, o gato deve miar e a vaca deve mugir).

# Crie uma função chamada ouvir_animal(animal: Animal) 
#     que chame o método falar para o objeto recebido como parâmetro.



class Animal:
    def falar(self):
        return 'GGG'
    
class Gato(Animal):
    def falar(self):
        return 'o gato deve miar'

class Cachorro(Animal):
    def falar(self):
        return 'o cachorro deve latir'

class Vaca(Animal):
    def falar(self):
        return 'a vaca deve mugir'
    
def ouvir_animal(animal):
    return animal.falar()


animal = Animal()
cachorro = Cachorro()
gato = Gato()
vaca = Vaca()

print(ouvir_animal(animal))
print(ouvir_animal(cachorro))
print(ouvir_animal(gato))
print(ouvir_animal(vaca))