'''
Implementacion de colas mediante deque()
Demuestra las diferencias en la forma de implementacion
'''
#Las colas (tuplas) son colecciones de elementos ordenados que unicamente permiten dos acciones:
#añadir un elemneto a la cola, sacar un elemento de la cola

SEPARADOR = ("*" * 20) + "\n"


cola = list() #cola utilizando lista

for cantidad in range (5):
   nuevo = imput("Nombre del recien llegado: ")
   cola.append(nuevo)

print(f"Se agregaron {len(cola)}, elementos: ")
for elemento in cola:
   print(elemento)
print(SEPARADOR)
pass #Hacer notar que los elementos permanecen en la cola

print("Procedemos a retirarlos de la cola")
while cola:
   print(cola.popleft())
pass #Verificar que la estructura vacia
