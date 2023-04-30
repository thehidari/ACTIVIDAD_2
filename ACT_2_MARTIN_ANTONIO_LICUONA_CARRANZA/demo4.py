#Diagrama de barras
import matplotlib.pyplot as plt
x1 = [2, 4, 6, 8, 10]
y1 = [3, 5, 1, 7, 4]

x2 = [1, 3, 5, 7, 9]
y2 = [1, 3, 2, 4, 9]

plt.bar(x1, y1,label='Barra 1',color='r')
plt.bar(x2, y2,label='Barra 1',color='g')

plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Grafica de barras')
plt.legend()

plt.show()