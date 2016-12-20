#!/usrbin/env python
# _*_ coding: utf-8 _*_
#tarea6
#LUZ Maria calderon aguilera
peso=input("peso:")
altura=input("altura")
def funcion(x,y):
    x=peso
    y=altura
    relaci=x/float(y)**2
    if relaci<16:
        print "Delgadez severa"
    elif relaci>16 and relaci<19.99:
        print "Delgadez moderada"
    elif relaci>17 and relaci<18.49:
        print "Delgadez leve"
    elif relaci>18.5 and relaci<24.99:
        print "Normal"
    elif relaci>25 and relaci<30:
        print "Sobrepeso"
    elif relaci>30 and relaci<40:
        print "Obesidad"
    elif relaci>40:
        print "Obesidad morbida"
salida=funcion(peso,altura)
