#Diagrama de apilamiento
import matplotlib.pyplot as plt

meses= [x for x in range(1,13)]

hipoteca= [700, 700, 700,
           800, 800, 800,
           850, 850, 850,
           850, 850, 850]

servicios= [500, 300, 380,
           200, 600, 550,
           310, 620, 290,
           320, 440, 400]

reparaciones= [100, 120, 100,
          150, 850, 80,
          120, 220, 240,
          50, 60, 150]

plt.plot([],[], color='blue', label='hipoteca')
plt.plot([],[], color='orange', label='servicios')
plt.plot([],[], color='brown', label='reparaciones')


plt.stackplot(meses, hipoteca, servicios, reparaciones, colors=['blue', 'orange', 'brown'])

plt.legend()

plt.title('Gastos de la casa')
plt.xlabel('Meses del año')
plt.ylabel('Costo')

plt.show()