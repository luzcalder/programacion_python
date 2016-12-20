#!/usrbin/env python
# _*_ coding: utf-8 _*_
#tarea5
#luz maria calderon aguilera
s=input("segundos")
def convierte(x):
  x=s
  dias=x/float(86400)
  horas=dias/float(3600)
  minutos=horas/float(60)
  print dias
  print horas
  print minutos
salida=convierte(s)
