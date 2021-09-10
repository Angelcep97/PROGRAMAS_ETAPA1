'''
Implementacion de pilas ulitizando listas y con deques
'''

import collections
SEPARADOR = ("*" *20 + "\n"

pila_con_lista = list()
for i in range(5):
   pila_con_lista.append(impunt("Dime el nombre a agregar: "))

#sacar elementos de la pila
while pila_con_lista:
   print(pila_con_lista.pop())
print(SEPARADOR)


#UNA COLA DOBLEMENTE TERMINADA, O DEQUE, ADMITE AGREGAR Y ELIMINAR ELEMENTOS DE CUALQUIER EXTREMO DE LA COLA
#LAS PILAS Y COLAS MAS COMUNES SON FORMAS DEFENERADAS DE DEQUES,DONDE LAS ENTRADAS Y SALIDAS ESTAN RESTRIGIDAS A UN SOLO EXTREMO


pila_deque = collections.deque()
for i in range(5):
   pila_deque.append(imput("Dime el nombre a agregar: "))

#Sacar elementos de la pila
while pila_deque:
   print(pila_deque.pop())
pass