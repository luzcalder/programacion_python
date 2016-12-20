#tarea3B
#LUZ MARIA CALDERON AGUILERA
import matplotlib.pyplot as plt
import numpy as np
import math
teta=np.linspace(0,2*np.pi,100)
r=105+100*np.sin(4.5*teta)
yt=teta-np.cos(10*teta)/10
x=320+r*np.cos(yt)
y=-240-r*np.sin(yt)
plt.plot(x,y,linewidth=3,color='brown',label='(x,y)')
plt.fill_between(x,y,color='b')
plt.legend()
plt.title('')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')
plt.axis('off')
plt.show()
plt.savefig('7.png')
