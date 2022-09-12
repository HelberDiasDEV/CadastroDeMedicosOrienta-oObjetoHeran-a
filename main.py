from Medico import Medico
from MedicoCirurgiao import MedicoCirurgiao
from MedicoAuxiliar import MedicoAuxiliar

medico = Medico("123","House", 54, 24000)
medico_cirurgiao = MedicoCirurgiao("321","Building", 51, 34000)
medico_aux = MedicoAuxiliar("456","Treta", 60, 7000)


medico_aux2 = MedicoAuxiliar("456","Treta", 60, 7000)
print("Medico:",medico.CalcularSalarioAposentadoria())

print("Medico:",medico.CalcularSalarioAposentadoria())

print("Cirurgiao:",medico_cirurgiao.VerificarAposentadoria())
print("Cirurgiao:",medico_cirurgiao.CalcularSalarioAposentadoria())

print("Aux:",medico_aux.VerificarAposentadoria())
print("Aux:",medico_aux.CalcularSalarioAposentadoria())