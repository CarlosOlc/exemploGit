# Herança e Polimorfismo

## Herança

Herança é um dos conceitos fundamentais da programação orientada a objetos. Ela permite que uma classe herde atributos e métodos de uma outra classe. A classe que herda é chamada de **subclasse** (ou classe derivada), e a classe da qual se herda é chamada de **superclasse** (ou classe base).

### Exemplo de Herança

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        return f'{self.nome} esta fazendo um som.'

class Cachorro(Animal):
    def emitir_som(self):
        return f'{self.nome} esta latindo.'


animal = Animal("Animal genérico")
cachorro = Cachorro("Rex")

print(animal.emitir_som())  # Saida: Animal generico esta fazendo um som.
print(cachorro.emitir_som())  # Saida: Rex esta latindo.
```

No exemplo acima, a classe `Cachorro` herda da classe `Animal`. Ela pode usar o método da classe pai, mas também pode sobrescrever o método `emitir_som` para fornecer um comportamento específico.

## Polimorfismo

Polimorfismo se refere à capacidade de um método agir de diferentes formas dependendo do contexto. Em Python, o polimorfismo pode ser implementado usando métodos sobrescritos e a capacidade de uma função trabalhar com objetos de diferentes tipos de uma forma genérica.

### Exemplo de Polimorfismo

```python
class Gato(Animal):
    def emitir_som(self):
        return f'{self.nome} esta miando.'

def fazer_barulho(animal):
    print(animal.emitir_som())

gato = Gato("Felix")
cachorro = Cachorro("Rex")

fazer_barulho(gato)  # Saida: Felix esta miando.
fazer_barulho(cachorro)  # Saida: Rex esta latindo.
```

Neste exemplo, a função `fazer_barulho` é capaz de lidar tanto com um objeto do tipo `Gato` quanto `Cachorro`, pois ambos têm o método `emitir_som`. O comportamento exato depende de qual classe foi instanciada.

## Resumo

- **Herança** permite que uma classe reutilize o código de outra, enquanto adiciona ou modifica comportamentos.
- **Polimorfismo** permite que um mesmo método funcione de forma diferente em classes relacionadas.