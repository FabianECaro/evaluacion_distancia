#Escriba un programa que determine la suma de los n primeros números de la serie: 1, 1, 2, 3, 5, 8, 13, 21

#Definimos nuestra funcion, en este caso suma_dosanteriores
#La letra n nos indicara la cantidad de veces que queremos hacer la suma empezando desde el 1, 1
def suma_dosanteriores(n):

#Creamos la lista en la cual se llevara a acabo la suma, empezando por los dos primeros numeros
    serie = [1, 1]

#Empleamos un ciclo para determinar asi el numero de iteraciones de acuerdo a n
    for i in range (n):

#En la lista serie se agregara un resultado respecto a los dos ultimos terminos de serie, para esto se usa append
        serie.append(sum(serie[-2:]))

#Separamos los terminos con una , y asi mostramos la lista de numero que hay en serie
    return ','.join(str(e) for e in serie)

#Llamamos nuestra funcion indicando en este caso 6 iteraciones
print(suma_dosanteriores(100))



