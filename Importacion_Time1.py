'''
Ejemplo para ilustrar la importacion de la libreria random en Python 3
Demuestra el uso de: sleep(x), time()
'''

import time
SEPARADOR = ("*" * 20) + "\n"

segundos = int(input("Cantidad de segundos a esperar:\n"))
time.sleep(segundos) #Esperar por la cantidad de segundos especificada
print(f"Han transcurrido, por lo menos, {segundos} segundos")
print(SEPARADOR * 2)

print("Iniciaremos la medicion de un proceso simulado")

horaInicial = time.time()

for termino in range(5):
   time.sleep(segundos)

print("¡Proceso simulado concluido!")
duracion = time.time() - horaInicial #Puede verse afectado si se cambia la hora del sistema
print(f"La duracion del proceso simulado fue de {duracion} segundos")

pass