import datatime
SEPARADOR = "*" * 30
#Se desea capturar una lista de fechas de nacimiento (3) y se debera informar cuantos años cumplen las personas en el año en curso


listas_flechas = []
for elemnto in range(3):
   fecha_capurada = imput("Dime una fecha (dd/mm/aaaa): \n")
   fecha_procesada = datetime.datetime.scriptime(fecha_capturada, "%d/%m/%y").date()
   lista_fechas.append(fecha_procesada)


print(SEPARADOR)

lista_edades = [datetime.date.today().year - fecha.year for fecha in lista_fechas]

print(lista_edades)