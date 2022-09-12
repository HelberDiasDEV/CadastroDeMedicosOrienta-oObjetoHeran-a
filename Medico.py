class Medico:
    def __init__(self, CRM, nome, idade, salario):
        self.CRM = CRM
        self.nome = nome
        self._idade = idade
        self.salario = salario
        self._IDADE_APOSENTADORIA = 56

    @property
    def Idade(self):
        return self._idade
    
    @Idade.setter
    def Idade(self, value):
        self._idade = value

    @property
    def IDADE_APOSENTADORIA(self):
        return self._IDADE_APOSENTADORIA

    def VerificarAposentadoria(self):
        if self._idade >= self.IDADE_APOSENTADORIA:
            return True
        else:
            return False
    
    def CalcularSalarioAposentadoria(self):
        return self.salario * .8