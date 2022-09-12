from Medico import Medico
class MedicoAuxiliar(Medico):
    def __init__(self, CRM, nome, idade, salario):
        super().__init__(CRM, nome, idade, salario)
        self._IDADE_APOSENTADORIA = 60
        