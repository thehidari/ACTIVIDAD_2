#Colocando titulos y etiquetas
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]

plt.plot(x,y)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Grafica Lineal')

plt.show()