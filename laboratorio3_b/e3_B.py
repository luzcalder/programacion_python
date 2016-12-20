#tarea3B
#LUZ MARIA CALDERON AGUILERA
import matplotlib.pyplot as plt
import numpy as np
import math
t=np.linspace(-2*np.pi,2*np.pi,100)
x=t+2*np.sin(2*t)
y=t+2*np.cos(5*t)
plt.plot(t,x,linewidth=4,color='r',label='t(x)')
plt.plot(t,y,linewidth=4,color='y',label='t(y)')
plt.legend('xy')
plt.title('')
plt.xlabel('t')
plt.ylabel('t(x)&t(y)')
plt.grid(True)
plt.show()
plt.savefig('3b.png')
