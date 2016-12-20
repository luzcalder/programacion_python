#!/usrbin/env python
# _*_ coding: utf-8 _*_
#tarea3B
#LUZ MARIA CALDERON AGUILERA
import matplotlib.pyplot as plt
import numpy as np
import math
t=np.linspace(0,2*np.pi,100)
x=np.cos(t)*np.cos(t)*np.cos(t)
y=np.sin(t)*np.sin(t)*np.sin(t)
plt.plot(t,x,linewidth=3,color='black',label='t(x)')
plt.plot(t,y,linewidth=2,color='y',label='t(y)')
plt.legend('xy')
plt.title('')
plt.xlabel('t')
plt.ylabel('X(t)&Y(t)')
plt.grid(True)
plt.show()
plt.savefig('3a.png')
