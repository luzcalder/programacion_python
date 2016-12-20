#!/usrbin/env python
# _*_ coding: utf-8 _*_
#tarea3B
#LUZ MARIA CALDERON AGUILERA
import matplotlib.pyplot as plt
import numpy as np
import math
t=np.linspace(0,4*np.pi,100)
m=0.5
n=2.5
f=np.sin(3*t)*np.cos(2*t)
g=m*np.cos(t)+n*np.cos(5*t)
plt.plot(t,f,linewidth=3,color='blue',label='f(x)')
plt.plot(t,g,linewidth=3,color='r',label='g(x)')
plt.legend('fg')
plt.title('')
plt.xlabel('t')
plt.ylabel('f(t)&g(t)')
plt.grid(True)
plt.show()
plt.savefig('2c.png')
