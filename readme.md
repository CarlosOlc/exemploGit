
# Classes Abstratas e Interfaces em Python

Em Python, as **classes abstratas** e **interfaces** são conceitos utilizados para definir contratos que classes concretas precisam seguir. Eles promovem uma estrutura de código mais organizada, permitindo que você crie classes com funcionalidades comuns, enquanto força as classes filhas a implementarem os métodos.

## Classes Abstratas

Uma **classe abstrata** é uma classe que não pode ser instanciada diretamente e que geralmente contém um ou mais **métodos abstratos**. Um método abstrato é um método que não tem implementação na classe abstrata. As classes filhas são obrigadas a implementar esses métodos abstratos.

Para criar classes abstratas e métodos abstratos em Python, utilizamos o módulo `abc` (Abstract Base Classes).

### Exemplo:

```python
from abc import ABC, abstractmethod

# Definindo uma classe abstrata
class Animal(ABC):

    # Método abstrato
    @abstractmethod
    def fazer_som(self):
        pass

# Tentando instanciar a classe abstrata causara um erro
# animal = Animal() # Isso resultara em um erro

# Definindo uma classe concreta que herda da classe abstrata
class Cachorro(Animal):

    # Implementando o método abstrato
    def fazer_som(self):
        return "Au Au!"

dog = Cachorro()
print(dog.fazer_som())  # Saída: Au Au!
```

### Explicação:
- A classe `Animal` é abstrata, pois herda de `ABC` e tem um método abstrato `fazer_som()`.
- A classe `Cachorro` herda de `Animal` e é obrigada a implementar o método `fazer_som()`.
- Se uma classe filha não implementar todos os métodos abstratos, ela também será considerada abstrata e não poderá ser instanciada.

## Interfaces em Python

Em Python, **interfaces** podem ser implementadas de maneira semelhante às classes abstratas, utilizando métodos abstratos. Embora Python não tenha o conceito de interfaces da mesma forma que outras linguagens como Java, podemos utilizar classes abstratas para definir contratos para as classes que as implementarem.

### Exemplo de Interface:

```python
from abc import ABC, abstractmethod

# Definindo uma interface
class Forma(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

# Implementando a interface em uma classe concreta
class Retangulo(Forma):

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    # Implementacao do metodo area
    def area(self):
        return self.largura * self.altura

    # Implementaçcao do metodo perimetro
    def perimetro(self):
        return 2 * (self.largura + self.altura)

# Criando uma instancia da classe concreta
retangulo = Retangulo(5, 3)
print(f"Area: {retangulo.area()}")        # Saida: Area: 15
print(f"Perimetro: {retangulo.perimetro()}")  # Saida: Perimetro: 16
```

### Explicação:
- A classe `Forma` é uma interface que define dois métodos abstratos: `area()` e `perimetro()`.
- A classe `Retangulo` implementa a interface `Forma` e fornece implementações para os métodos `area()` e `perimetro()`.
- Isso garante que qualquer classe que implemente a interface `Forma` terá que fornecer as funcionalidades exigidas.

## Diferença entre Classes Abstratas e Interfaces

- Uma classe abstrata pode ter tanto métodos abstratos quanto métodos concretos (com implementação). Já uma interface (como em outras linguagens, ou simulada com classes abstratas em Python) geralmente define apenas métodos abstratos.
- Interfaces são usadas para definir o que uma classe deve fazer, enquanto classes abstratas podem definir como algumas coisas devem ser feitas.
- Em Python, interfaces são implementadas usando classes abstratas com apenas métodos abstratos, e a distinção entre classes abstratas e interfaces não é tão rígida como em outras linguagens.

## Conclusão

Classes abstratas e interfaces ajudam a organizar e estruturar melhor o código, forçando as classes concretas a implementar determinados comportamentos. Isso facilita o desenvolvimento de sistemas grandes e complexos, promovendo a reutilização de código e a padronização de interfaces entre objetos.