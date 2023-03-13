#Escriba un programa que lea una lista de palabras y encuentre los anagramas existentes

#Importamos un diccionario para almacenar
#key y value
from collections import defaultdict

#Pedimos una lista de palabras y estas a su vez
#con .split van siendo separadas una de otra con un espacio

palabras = input("Ingrese una lista de palabras separadas por espacios: ").split()

#Asignamos que el diccionario
#pase a nuestra nueva variable llamada anagramas

#El append nos indica que se estara agragando una
#nueva key por cada palabara

anagramas = defaultdict(list)
for i in palabras:
    key = "".join(sorted(i))
    anagramas[key].append(i)

#Finalmente una vez se terminen de agregar todas las palabras
#se realiza una comparacion entre la key y el valor en
#cada item expuesto en anagramas
print("Los anagramas en la lista son:")
for key, value in anagramas.items():
    if len(value) > 1:
        print(value)


