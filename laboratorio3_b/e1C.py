#tarea3B
#LUZ MARIA CALDERON AGUILERA
import matplotlib.pyplot as plt
import numpy as np
import math
x=np.linspace(-1,5,93)
t=x
y=t*math.e**(-2*t)
plt.plot(x,y,linewidth=7,color='b',label='Inciso c')
plt.legend()
plt.title('')
plt.xlabel('t')
plt.ylabel('f(t)=te**-2*t')
plt.grid(True)
plt.show()
plt.savefig('c.png')
