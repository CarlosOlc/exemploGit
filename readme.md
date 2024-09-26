
# Tratamento de Exceções em Python

## Por que é usado?

Utilizado para lidar com erros que podem ocorrer durante a execução de um programa. Em vez de o programa terminar quando encontra um erro, é possível capturá-lo e tratá-lo adequadamente, permitindo que o fluxo de execução continue ou que uma ação corretiva seja tomada. Controlar falhas inesperadas.

### Vantagens:
- **Prevenir o término do programa**: Permite que o programa lide com erros, continuando a execução ou fechando de maneira controlada.
- **Melhor legibilidade e manutenção**: Separa o código de tratamento de erros do código da lógica principal.
- **Fornece flexibilidade**: Diferentes exceções podem ser tratadas de maneira diferente.

## Modos de Usar

### 1. Bloco `try-except`
A forma mais comum de tratar exceções em Python é utilizando o bloco `try-except`.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisao por zero nao eh permitida")
```

### 2. Capturando Múltiplas Exceções
Você pode capturar múltiplas exceções em um único bloco de `except` ou tratar cada uma separadamente.

```python
try:
    x = 10 / 0
except (ZeroDivisionError, TypeError):
    print("Erro: operacao invalida")
```

### 3. Usando `else`
O bloco `else` é executado se nenhuma exceção ocorrer no bloco `try`.

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Erro: divisao por zero")
else:
    print("Resultado:", resultado)
```

### 4. Bloco `finally`
O bloco `finally` é sempre executado, independentemente de uma exceção ter ocorrido ou não.

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Erro: divisao por zero")
finally:
    print("Fim")
```

## Importância em POO

Em programação orientada a objetos (POO), o tratamento de exceções é essencial para encapsular e isolar falhas que possam ocorrer nos métodos de uma classe, sem expor o estado interno da classe diretamente. Ele permite que as classes lidem com erros internamente e mantenham a integridade de seus objetos.

### Exemplo:
```python
class Calculadora:
    def dividir(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Erro: divisao por zero"

calc = Calculadora()
print(calc.dividir(10, 0))
```

### JavaScript
- **Flexibilidade**: JavaScript utiliza `try-catch-finally`.

Exemplo em JavaScript:
```javascript
try {
    let x = 10 / 0;
} catch (e) {
    console.log("Erro: divisao por zero");
} finally {
    console.log("Fim da operacao");
}
```
