#!/usrbin/env python
# _*_ coding: utf-8 _*_
#tarea3B
#LUZ MARIA CALDERON AGUILERA
import matplotlib.pyplot as plt
import numpy as np
import math
t=np.linspace(0,2*np.pi,100)
x=np.sin(3*t)
y=np.sin(4*t)
plt.plot(t,x,linewidth=6,color='r',label='t(x)')
plt.plot(t,y,linewidth=3,color='b',label='t(y)')
plt.legend('xy')
plt.title('')
plt.xlabel('t')
plt.ylabel('t(x)&t(y)')
plt.grid(True)
plt.show()
plt.savefig('3c.png')
