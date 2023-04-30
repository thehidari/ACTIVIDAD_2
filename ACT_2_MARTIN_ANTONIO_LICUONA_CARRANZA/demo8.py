#Diagrama de dispersion
import matplotlib.pyplot as plt
x1=[1,2,3,4,5,6,7,8,9,10]
y1=[4,5,4,3,2.5,3,3,2.7,2,1]

plt.scatter(x1,y1,label='estrellas',color='g',s=300,marker="*")

plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Grafica de dispersion')
plt.legend()

plt.show()