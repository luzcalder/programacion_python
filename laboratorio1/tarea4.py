#!/usrbin/env python
# _*_ coding: utf-8 _*_
#TAREA4
#luz maria calderon aguilera
dias=input("dias:")
hrs=input("horas")
minutos=input("minutos")
s=input("segundos")
def convierte(a,b,c,d):
  a=dias
  b=hrs
  c=minutos
  d=s
  stotal=a*86400+b*3600+c*60+d
  print stotal
salida=convierte(dias,hrs,minutos,s)
