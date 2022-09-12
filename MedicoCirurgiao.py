from Medico import Medico
class MedicoCirurgiao(Medico):
    def __init__(self, CRM, nome, idade, salario):
        super().__init__(CRM, nome, idade, salario)
        self._IDADE_APOSENTADORIA = 50
        
    def CalcularSalarioAposentadoria(self):
        return (self.salario * .8) + 2000
    