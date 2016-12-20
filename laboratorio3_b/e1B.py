#tarea3B
#LUZ MARIA CALDERON AGUILERA
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-1,5,93)
y=-2*x**2-8*x-11
plt.plot(x,y,linewidth=6,color='purple',label='Inciso b)')
plt.legend()
plt.title('')
plt.xlabel('x')
plt.ylabel('f(x)=2x^2-8x-11')
plt.grid(True)
plt.show()
plt.savefig('b.png')
