#Diagrama de dispersion
import matplotlib.pyplot as plt
x1=[1,2,3,4,5,6,7,8,9,10] #Se debe tener la misma cantidad de datos x & y
y1=[3,5,1,7,4,3,3,4,2,1]

plt.scatter(x1,y1,label='puntos',color='r',s=200)

plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Grafica de dispersión')
plt.legend()

plt.show()