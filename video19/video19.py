# -*- coding: utf-8

Created on Wed May 4 18:07:18 2022

@author: nicosio

# Tiempo de vida del objeto

# El tiempo que pasa desde la instanciacion del objeto hasta que es # destruido se conoce como el tiempo de vida del objeto

# Conteo de referencia

#En Python los programadores no se deben de preocupar por el manejo de memoria # pero es bueno comprender que es lo que sucede en el lenguaje.

# Cuando un programa instancia un objeto, se reserva parte de la memoria para # guardar las variables de instancia de esa clase

# Cada objeto tiene un campo interno que se conoce como conteo de referencia # este nos indica cuantas variables diferentes se refieren al mismo objeto

# Incremento de reference count

# 1. Cuando una variable adicional es asignada al mismo objeto

# objeto2-objeto1

# 2. Cuando un objeto se pasa a una funcion y la variable del parametro # local es referenciada al objeto

# mifuncion (objeto1)

# 3. Cuando un objeto es colocado en un contenedor como una lista o diccionario

# milista=[objeto1, objeto2, objeto3]

import sys

# creamos una clases

class clase1():

def _init_(self,x,y):

self.x=x

self.y=y

# Creamos una instancia

objetol=clase1(2,3)

#Imprimimos su conteo de referencia

# El valor quiza nos confunda pero en la documentacion leemos que # El valor regresado es generalmente mayor en 1 por que incluye la # referencia temporal como argumento al invocar getrefcount

print(sys.getref count (objeto1))

# Asignamos una variable

objeto2=objeto1

print(sys.getrefcount(objeto1))

milista=[objeto1] print(sys.getrefcount(objeto1))

# Si creamos una nueva instancia cada quien tiene su reference count

objeto3-clase1(5,7)

print(sys.getrefcount(objeto1))
print(sys.getrefcount(objeto3))

#######################
