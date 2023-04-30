#Diagrama de apilamiento
import matplotlib.pyplot as plt
dias=['dom','lun','mar','mie','jue','vie','sab']

#tiempo empleado en horas:
dormir=[9,6,7,6,7,6,8]
comer=[3,1,1.30,1,1.30,2,3]
trabajar=[2,10,9,8,9,8,0]
jugar=[8,2,3,2,3,2,9]

plt.plot([],[], color='blue', label='dormir')
plt.plot([],[], color='orange', label='comer')
plt.plot([],[], color='brown', label='trabajar')
plt.plot([],[], color='red', label='jugar')

plt.stackplot(dias, dormir, comer, trabajar, jugar)
plt.legend()

plt.title('Apilamiento de actividades en la semana')
plt.xlabel('dias')
plt.ylabel('tiempo en horas')
plt.show()