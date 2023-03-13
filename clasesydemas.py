#Escriba un programa que use clases, atributos, métodos y herencia, documéntelo

#Definimos una clase que en este caso se llamara Animal
class Animal:
#Usamos un constructor que acepte los siguientes parametros
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
#Esta clase a su vez tendra dos metodos
    def comer(self):
        print(f"{self.nombre} esta comiendo.")

    def dormir(self):
        print(f"{self.nombre} esta durmiendo.")

#Creamos una subclase que se hereda de la clase Animal
#Esta linea de abajo es la sintaxis de herencia en python
#En donde Perro tendra todos los atributos y metodos
#ademas de esto un metodo adicional
class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} esta ladrando.")


class Gato(Animal):
    def maullar(self):
        print(f"{self.nombre} esta maullando.")

#Se crea una instancia de las subclases en donde se almacen metodos y atributos
perro = Perro("Tobby", 7)
gato = Gato("Zury", 1)

#En esta parte por ultimo llamamos los metodos y atributos de las instacias
print(perro.nombre)
perro.comer()
perro.ladrar()

print(gato.nombre)
gato.dormir()
gato.maullar()

 #Por ultimo llamamos a los metodos y atributos que definimos anteriormente