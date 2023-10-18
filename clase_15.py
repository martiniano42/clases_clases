
# valor = 'Hola script'
# valor = input('Ingrese un texto a mostrar: ')

# import sys

# print(sys.argv)
# datos = sys.argv[1:]
# valor = datos[0]
# print(valor)
# print(dir(sys))


# import matematica

# print(matematica.suma(1, 2))
# print(matematica.resta(1, 2))

# rectangulo = matematica.Rectangulo(5,2)

# print(rectangulo.area())


# import pepe.ea

# from matematica import suma, Circulo
# print(suma(1,2))


# from matematica import *
# print(suma(1,2))



# import matematica as modulo_matematica
# matematica = 'Matematica'
# print(modulo_matematica.suma(1, 2))


# from matematica import suma as suma_de_matematica, Rectangulo as RectanguloMatematica

# Rectangulo = 'Rectangulo'
# suma = 'suma'
# rectangulo = RectanguloMatematica(5,2)

# print(rectangulo.area())

# print(suma_de_matematica(1,2))


# from mi_paquete.pepe.ea import funcion_a_compartir

# funcion_a_compartir()


# import mi_paquete
# mi_paquete.pepe.ea.funcion_a_compartir()



















#################################################
#################################################
















# import sys

# print(sys.argv)
# print(type(sys.argv))

# argumentos = sys.argv[:]

# print('Ahi te va de que grupo sos!')
# nombre = sys.argv[1]
# preferencia = sys.argv[2]

# if (preferencia == "marvel" and nombre < 'm' ) or (preferencia == "capcom" and nombre > 'n'):
#     print('Sos del grupo A!')
# else:
#     print('Sos del grupo B!')

#################################################
#################################################

# # siempre va a arriba de todo solo esta aca por ventajas a la hora de dar la clase
# import clase_14 
# import clase_14 as el_otro_modulo

# perro = clase_14.Perro()
# # perro.hablar()

# clase_14.llama_hablar(perro)

# perro = el_otro_modulo.Perro()
# # perro.hablar()

# el_otro_modulo.llama_hablar(perro)

#################################################
#################################################

# # siempre va a arriba de todo solo esta aca por ventajas a la hora de dar la clase
# from clase_14 import Perro, llama_hablar

# perro = Perro()
# perro.caminar()

# llama_hablar(perro)

#################################################
#################################################

# # siempre va a arriba de todo solo esta aca por ventajas a la hora de dar la clase
# from clase_14 import *

# perro = Perro()
# perro.caminar()

# llama_hablar(perro)

#################################################
#################################################

# # siempre va a arriba de todo solo esta aca por ventajas a la hora de dar la clase
# from clase_14 import Perro as PerritoLoco, llama_hablar as llama_hablar_14

# perro = PerritoLoco()
# perro.caminar()

# llama_hablar_14(perro)

# def llama_hablar():
#     print('Mira lo que hago!!')
    
# llama_hablar_14(perro)

#################################################
#################################################

# # siempre va a arriba de todo solo esta aca por ventajas a la hora de dar la clase
# from mi_paquete import funciones
# from mi_paquete.funciones import llama_hablar as llama_hablar_funciones
# from mi_paquete.clases import Perro as PerritoLoco

# perro = PerritoLoco()
# perro.caminar()

# llama_hablar_funciones(perro)

# def llama_hablar():
#     print('Mira lo que hago!!')
    
# llama_hablar_funciones(perro)

#################################################
#################################################


# collections

# from collections import namedtuple, Counter

# Pescado = namedtuple('Pescado', ['nombre', 'especie', 'peso'])

# pescado1 = Pescado('pecesin', 'payaso', 200)

# print(Pescado)
# print(pescado1)
# print(pescado1.nombre)
# print(pescado1[0])
# print(pescado1._asdict())
# print(list(pescado1._asdict().items())[0])

# print(Counter('abcabc123'))
# print(Counter((1,2,3,4,5,3,5,7,8,9,1,1,1,2,2)))

# datetime

# from datetime import datetime, timedelta

# dt = datetime.now()
# print(dt)

# dt_custom = datetime(2000, 1, 1)
# print(dt_custom)

# print(dt.strftime("%A %d %B %Y %I:%M"))
# print(dt.hour)

# dt1 = dt.replace(day=5)
# print(dt)
# print(dt1)

# td = timedelta(days=15)

# dato_de_fecha_modificado = dt + td
# # dato_de_fecha_modificado = dt - td
# print(dato_de_fecha_modificado)


# math

# import math

# print(math.pi)
# print(math.sqrt(64))
# print(round(3.3))
# print(round(3.5))
# print(round(3.8))
# print(math.floor(3.8))
# print(math.ceil(3.3))

# import random

# print(random.randrange(15))
# print(random.randrange(15, 22))
# print(random.randrange(15, 28, 2))

# lista = ['hoy', 'corri', '4', 'kilometros']
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choices(lista, k=3))
# print(random.choices(lista, k=2))
# print(random.choices(lista, k=5))
# print(random.choices(lista))

# class Persona():
    
#     def __str__(self):
#         return 'Yo soy tu padre'
    
# class Cliente(Persona):
    
#     def __str__(self):
#         return super().__str__() + 'y yo tu hijo'
    
# cliente = Cliente()

# print(cliente)