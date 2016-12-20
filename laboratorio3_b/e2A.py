#tarea3B
#LUZ MARIA CALDERON AGUILERA
import matplotlib.pyplot as plt
import numpy as np
import math
x=np.linspace(0,4*math.pi,100)
y=np.cos(2*x)+np.sin(3*x)
z=-2*np.sin(2*x)+3*np.cos(3*x)
plt.plot(x,y,linewidth=3,color='r',label='s(x)')
plt.plot(x,z,linewidth=2,color='blue',label='v(x)')
plt.legend('sv')
plt.title('')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
plt.savefig('2a.png')
