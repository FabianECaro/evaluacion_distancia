#Escriba un programa que le solicite una palabra al usuario y determine si la palabra ingresada es un palíndromo

#Pedimos como entrada una frase o palabra
#Una vez tenemos una de estas dos le asignaremos a una
#nueva variable con el nombre de entradainvertida la cual
#tendra la entrada sin espacios, con todas sus palabras
#sin mayuscula y ademas de esto con la frase o palabra invertida
entrada=input("escribe una palabra o frase: ")
entradainvertida = entrada.replace(' ','').lower() [:: - 1]

#Se imprime sin mayuscula y sin espacios
#con la sentencia if diremos que si la entrada sin espacios ni
#mayusculas es igual a la variable entradainvertida nos de como
#resultado que la palabra es palindroma en dado caso de que no se cumpla
#nos dira que la palabra no es palindroma
print(entrada.replace(' ','').lower())
if entrada.replace(' ','').lower() == entradainvertida:
    print("La palabra es palindroma")
else:
    print("La Palabra no es palindroma")


