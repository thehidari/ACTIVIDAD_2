#Grafica circular
import matplotlib.pyplot as plt
dias=['dom','lun','mar','mie','jue','vie','sab']

#tiempo empleado en horas:
dormir=[9,6,7,6,7,6,8]
comer=[3,1,1.30,1,1.30,2,3]
trabajar=[2,10,9,8,9,8,0]
jugar=[8,2,3,2,3,2,9]

partes=[7,2,8,5]
actividades=['dormir','comer','trabajar','jugar']
cols=['c','y','r','b']

plt.title('Diagrama circular \nactividades en la semana')
plt.xlabel=('x')
plt.ylabel=('y')
plt.pie(
        partes, 
        colors=cols, 
        labels=actividades, 
        startangle=90, 
        shadow=True, 
        explode=(0.2,0.2,0.2,-0.1),
        autopct=('%1.1f%%')
       )
plt.legend()
plt.show()