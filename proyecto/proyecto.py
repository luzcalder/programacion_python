grafica fluidos
import matplotlib.pyplot as plt
import numpy as np


x= np.linspace(3,-3,100)
y=x**2
z=x
w=x**3
celdas=36000
tibio=10
caliente=3600/2
frio=3600/2
aceite=frio
range(2,100)
plt.plot(x,y, linewidth=6,color='r',label='parabola')
plt.plot(z,w, linewidth=6,color='g',label='una cubica')
plt.legend()
plt.title('fluidos')
plt.xlabel('')
plt.ylabel('una funcion')
plt.grid(True)
plt.show()
plt.savefig('grafica.prig')
