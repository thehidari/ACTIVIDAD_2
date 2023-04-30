#Histograma
import matplotlib.pyplot as plt
edad_hombres=[2,3,4,5,1,2,4,5,14,25,12,56,34,22,78,65,77,90,5,22,33,55,44,66,22,34,13,5,33,56,88,95,75]
edad_mujeres=[77,66,55,44,33,22,11,22,2,42,21,63,6,99,88,66,13,42,35,38,47,54,34,39,78,27,73,26,3,4,5,1]
edades=[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(edad_hombres,edades,histtype='bar',rwidth=0.8,color='b',label='hombres')
plt.hist(edad_mujeres,edades,histtype='bar',rwidth=0.4,color='r',label='mujeres')

plt.xlabel('Eje X: Edades')
plt.ylabel('Eje Y: Poblacion')
plt.title('Histograma')
plt.legend()

plt.show()