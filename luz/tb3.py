
import csv

a=raw_input("introduce una caracteristica del elemento: ")
def tabla(x):
     x=a
     with open('periodo.csv') as tabla:
         fuente= csv.reader(tabla)
         elementos=[]
         for reg in fuente:
              elementos.append(reg)
         for i in range(118):
            if x in elementos[i]:
                print elementos[i]

salida = tabla(a)
