#!/usrbin/env python
# _*_ coding: utf-8 _*_
#triangulo rectangulo
#luz maria calderon aguilera
import math as m
a=input("Ingresa a")
b=input("Ingresa b")
def hipotenusa(a,b):
    a=a
    b=b
    h=m.sqrt(a*a+b*b)
    print h

salida=hipotenusa(a,b)
print salida
