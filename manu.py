# Crie uma classe Funcionario 
#     que tenha os atributos nome e salario. 
    
# Crie uma subclasse chamada Gerente 
#     que herda de Funcionario, mas que também tenha um atributo adicional bonus. 
    
# O construtor da classe Gerente deve receber nome, salario e bonus.



class Funcionario():
    def __init__(self, nome, salario):
        self.__nome = nome 
        self.__salario = salario 

    def info(self):
        # return f'{self.__nome} ganha {self.__salario}'
        return self.__nome + " ganha" + self.__salario


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.__bonus = bonus

    def info(self):
       return f'{super().info()}, bonus: {self.__bonus}'



f1 = Funcionario('ema', 100000000000)
gerente = Gerente('jeudje', 7483783, 'nhdhede')
print(f1.info())
print(gerente.info())

