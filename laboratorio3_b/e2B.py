#tarea3B
#LUZ MARIA CALDERON AGUILERA
import matplotlib.pyplot as plt
import numpy as np
import math
x=np.linspace(0,2,100)
m=-3*x
f=x*np.e**m
g=(np.e**m)*(1-m)
plt.plot(x,f,linewidth=3,color='b',label='f(x)')
plt.plot(x,g,linewidth=2,color='y',label='g(x)')
plt.legend('fg')
plt.title('')
plt.xlabel('x')
plt.ylabel('f(x)&g(x)')
plt.grid(True)
plt.show()
plt.savefig('2b.png')
