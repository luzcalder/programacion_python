
import math as math
h= input("pedir latitud")
g=input("pedir longitud")
j= input("pedir latitud")
k= input("pedir longitud")

def funcion(t1,t2,g1,g2):
    pi=3.1416
    t1= (h*pi/180)
    g1= (g*pi/180)
    t2=(j*pi/180)
    g2= (k*pi/180)
    distancia=6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
    return distancia
    print distancia

salida=funcion(h,g,j,k)
print salida
