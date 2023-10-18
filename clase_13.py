# https://www.seas.es/blog/informatica/agregacion-vs-composicion-en-diagramas-de-clases-uml/
# Slides

# Definiendo e instanciar una clase
'''
class Auto:
    ... # pass
    
auto1 = Auto()
auto2 = Auto()
'''


# def nombre_funcion(par):
#     ...
#     print('asd')
#     return 'pepito'

# nombre_funcion()

# print('hola como va?')
# print(type('hola como va?'))
# print('hola como va?'.capitalize())

class Auto: # -> color, marca, modelo
    
    def __init__(self, marca='Peugeot', modelo='206', color='blanco'):
        self.color = color
        self.marca = marca
        self.modelo = modelo
    
    def descripcion_con_ubicacion(self):
        print('Este es un auto.', self) # -> print('Este es un auto.', auto)
    
    def tocar_bocina(self):
        print('PIIIIIIIIIIIIII!!!!')
        # return 'PIIIIIIIIIIIIII!!!!'
        
    # def asignar_color(self, color):
    #     self.color = color
    
    def modificar_color(self, color):
        self.color = color
    
    def mostrar_color(self):
        print(self.color)


auto1 = Auto('Ford', 'K', 'rojo')
auto3 = Auto(color='negro')
auto2 = Auto('Fiat', 'Uno', 'verde')

print(auto1)
print(auto2)
# auto1.tocar_bocina()
# # print(auto1.tocar_bocina)
# # print(auto1.tocar_bocina())
# auto2.tocar_bocina()
auto1.descripcion_con_ubicacion()
auto2.descripcion_con_ubicacion()
auto3.descripcion_con_ubicacion()

auto1.mostrar_color()
auto2.mostrar_color()
auto3.mostrar_color()

# ================================================================================
# ================================================================================

# def funcion():
#     return 'valor'

# valor = funcion()
# print(valor)

# print(type(2))

# class ClaseAuto: # PascalCase
#     ... # pass

# auto1 = ClaseAuto()
# auto2 = ClaseAuto()

# print(type(2))
# print(type(auto1))
# print(type(auto2))


# print(funcion)
# print(ClaseAuto)
# print(auto1)
# print(auto2)


# Base sobre metodos

# class NombreClase:
    
#     def nombre_funcion(self): # self siempre va como primer parametro
#         ... # codigo


# class ClaseAuto: # PascalCase
            
#     def tocar_bocina(self):
#         print('Pi pi!!')  

#     def describir_auto(self):
#         # return f'Este es un auto.'
#         return f'Este es un auto. {self}'


# auto1 = ClaseAuto()
# auto2 = ClaseAuto()
# print(auto1)
# print(auto2)
# auto1.tocar_bocina()
# auto2.tocar_bocina()

# self va a valer auto1
# print(auto1.describir_auto()) # describir_auto(auto1)

# self va a valer auto2
# print(auto2.describir_auto()) # describir_auto(auto2)



# Atributos

# De clase

# class ClaseAuto: # PascalCase
    
#     tiene_velocimetro = True
            
#     def tocar_bocina(self):
#         print('Pi pi!!')  

#     def describir_auto(self):
#         # return f'Este es un auto.'
#         return f'Este es un auto. {self}' 

    
# auto1 = ClaseAuto()
# auto2 = ClaseAuto()
# auto1.tocar_bocina()
# auto2.tocar_bocina()
# print(auto1.describir_auto())
# print(auto2.describir_auto())

# print(ClaseAuto.tiene_velocimetro)
# print(auto1.tiene_velocimetro)
# print(auto2.tiene_velocimetro)


# class ClaseAuto: # PascalCase
    
#     tiene_velocimetro = True
    
#     def generar_color(self, color):
#         self.color = color
            
#     def tocar_bocina(self):
#         print('Pi pi!!')  

#     def describir_auto(self):
#         # return f'Este es un auto.'
#         return f'Este es un auto de color {self.color}. {self}' 

    
# auto1 = ClaseAuto()
# auto2 = ClaseAuto()
# auto1.generar_color('negro')
# print(auto1.describir_auto())
# print(auto2.describir_auto())
# print(auto1.color) 
# print(auto2.color)




# De instancia
'''
class Auto:
    
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca
'''

# class FordK:
    
#     def __init__(self, color='blanco', puertas=2):
#         self.color = color
#         self.puertas = puertas

# auto1 = FordK(color='rojo',puertas=5) # <<=== es como si tambien se ejecutase una linea asi auto1.__init__('rojo',5)
# print(auto1.color)
# auto2 = FordK()
# auto1 = FordK('Negro', 4)
# auto2 = FordK('Rojo', 2)
# auto3 = FordK('Rojo', 3)

# print(auto1)
# print(f'Color de auto1 {auto1.color}')
# print(f'Cant puertas {auto1.puertas}')
# print(auto2)
# print(f'Color de auto2 {auto2.color}')
# print(f'Cant puertas {auto2.puertas}')


# class FordK:
    
#     ruedas = 4
    
#     def __init__(self, color, puertas):
#         self.color = color
#         self.puertas = puertas
#         self.blindado = True
#         # if self.color == 'Negro':
#         #     self.ruedas = 1
#         self.aviso_de_fabricacion()
        
#     def aviso_de_fabricacion(self):
#         print('Se fabrico un auto Ford K')
    
#     def tocar_bocina(self):
#         print('Pi pi!!')
    
#     def describir_auto(self):
#         self.tocar_bocina()
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'
    

# auto1 = FordK('Negro', 4)
# auto2 = FordK('Rojo', 2)

# print(auto1)
# print(auto2)
# print(f'Color {auto1.color}')
# print(f'Color {auto2.color}')
# print(auto1.describir_auto())
# print(auto2.describir_auto())



# print(auto1)
# print(f'Color {auto1.color}')
# # print(f'Cant puertas {auto1.puertas}')
# print(auto1.blindado)
# auto1.tocar_bocina()
# print(auto1.blindado)
# print(auto1.describir_auto())
# print(f'Color {auto1.color}')
# print(auto1.ruedas)
# print(FordK.ruedas)

# # print(auto2)
# # print(f'Color {auto2.color}')
# # print(f'Cant puertas {auto2.puertas}')
# # auto2.tocar_bocina()
# print(auto2.describir_auto())

# ======================================================
# ======================================================

# Valores por defecto

# class FordK:
    
#     def __init__(self, color='Verde', puertas=5):
#         self.color = color
#         self.puertas = puertas
        
#     def tocar_bocina(self):
#         print('Pi pi!!')
    
#     def describir_auto(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'
    

# auto1 = FordK('Negro', 4)
# auto2 = FordK('Rojo', 2)
# auto3 = FordK(puertas=2)
# auto4 = FordK('Rojo')
# auto5 = FordK()

# print(auto1.color, auto1.puertas)
# print(auto2.color, auto2.puertas)
# print(auto3.color, auto3.puertas)
# print(auto4.color, auto4.puertas)
# print(auto5.color, auto5.puertas)

# *args, **kwargs en constructor


# print(type(auto1))
# print(type(auto2))

# ======================================================
# ======================================================

# Atributo de clase

# class FordK:
  
#     cant_ruedas = 4
    
#     def __init__(self, color='Verde', puertas=5):
#         self.color = color
#         self.puertas = puertas
#         self.radio = True
        
#     def tocar_bocina(self):
#         print('Pi pi!!')
    
#     def describir_auto(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'


# auto1 = FordK('Negro', 4)
# auto2 = FordK('Rojo', 2)
# auto3 = FordK(puertas=2)
# auto4 = FordK('Rojo')
# auto5 = FordK()

# print(auto1.color, auto1.puertas, auto1.cant_ruedas)
# print(auto2.color, auto2.puertas, auto2.cant_ruedas)
# print(auto3.color, auto3.puertas, auto3.cant_ruedas)
# print(auto4.color, auto4.puertas, auto4.cant_ruedas)
# print(auto5.color, auto5.puertas, auto5.cant_ruedas)

# print(type(auto1))
# print(type(auto2))

# print(FordK.cant_ruedas)
# print(FordK.color)

# ======================================================
# ======================================================

# Metodos

# class FordK:
  
#     cant_ruedas = 4
    
#     def __init__(self, color='Verde', puertas=5):
#         self.color = color
#         self.puertas = puertas
#         self.metros_recorridos = 0
#         self.fabricar()
    
#     def tocar_bocina():
#         print('Pi pi!!')
#         # self.toco_bocina = True
    
#     # def __str__(self):
#     #     return self.describir_auto()
    
#     def describir_auto(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'

#     def fabricar(self):
#         print(f'Se fabrico un Ford K {self.color} de {self.puertas} puertas.')
        
#     def avanzar(self, metros):
#         print(f'el auto avanzo {metros} metros')
#         self.metros_recorridos += metros


# auto1 = FordK('Negro', 4)
# print(auto1)
# print(auto1.toco_bocina)
# auto1.tocar_bocina()
# print(auto1.describir_auto())
# print(auto1.toco_bocina)
# auto1.fabricar()
# auto1.avanzar(15)
# print(auto1.metros_recorridos)

# auto2 = FordK(puertas=2)
# auto2.fabricar()

# print(auto1)
# print(auto1.color, auto1.puertas, auto1.cant_ruedas)
# auto1.tocar_bocina()
# print(auto1.describir_auto())
# print(auto1.metros_recorridos)
# auto1.avanzar(150)
# print(auto1.metros_recorridos)

# print(auto2)
# print(auto2.color, auto2.puertas, auto1.cant_ruedas)
# auto2.tocar_bocina()
# print(auto2.describir_auto())
# print(auto2.metros_recorridos)
# auto2.avanzar(32)
# print(auto2.metros_recorridos)

# ======================================================
# ======================================================

# Ej 1: Mi primera clase (10min)
'''
Crear una clase para trabajar con una Persona. 
Agregarle 3 atributos de instancia, el constructor y dos métodos. 

Luego instanciar a dos personas.
'''

# ======================================================
# ======================================================


# Metodos especiales (Magic Methods, Dunder Methods)

# ======================================================
# ======================================================

# Nuestro ejemplo

# dicc = {
#     'llave1': 'valor1',
#     'llave2': 'valor2',
#     'llave3': 'valor3',
#     'llave4': 'valor4'
# }

# dicc = dict(
#     (('llave1','valor1'),
#     ('llave2','valor2'),
#     ('llave3','valor3'),
#     ('llave4','valor4'))
# )
# print(dicc)
# dicc.update({1: True})
# dicc.update(((1, True),))

# print(type(dicc)) # Checkeado
# print(dicc) # Checkeado mas o meno
# print(len(dicc)) # Checkeado
# print(dicc['llave2'])
# dicc['llave2'] = 'valor nuevo de la llave 2'
# print(dicc['llave2'])

# for llave in dicc:
#     print(f'La llave {llave} contiene el valor {dicc[llave]}')

# print('================================================================================================================')

# class MiDicc:
    
#     def __init__(self, datos):
#         self.datos = datos
    
#     def __str__(self):
#         mi_dic_en_str = ''
#         for dato in self.datos:
#             mi_dic_en_str += f'{dato[0]}: {dato[1]}, '
#         return '{' + mi_dic_en_str + '}'
    
#     def __len__(self):
#         return len(self.datos)
    
#     def __getitem__(self, clave):
#         for (primer_valor, segundo_valor) in self.datos:
#             if clave == primer_valor:
#                 return segundo_valor
#         return 'La llave no se encuentra'
    
#     def __setitem__(self, clave, nuevo_valor):
#         for (primer_valor, segundo_valor) in self.datos:
#             if clave == primer_valor:
#                 lista = list(self.datos)
#                 indice = lista.index((primer_valor, segundo_valor))
#                 lista[indice] = (primer_valor, nuevo_valor)
#                 self.datos = lista
#         return 'La llave no se encuentra'
    
#     def __iter__(self):
#         for dato in self.datos:
#             yield dato[0]



# mi_dic = MiDicc(
#     (
#         ('llave1','valor1'),
#         ('llave2','valor2'),
#         ('llave3','valor3'),
#         ('llave4','valor4')
#     )
# )

# print(type(mi_dic))
# print(mi_dic) # print(str(valor que le pasamos))
# print(len(mi_dic))
# print(mi_dic['llave2'])
# # print(mi_dic['llave7'])
# mi_dic['llave2'] = 'valor nuevo de la llave 2'
# print(mi_dic['llave2'])


# for llave in mi_dic:
#     print(f'La llave {llave} contiene el valor {mi_dic[llave]}')


'''
============================================================================================
============================================================================================
'''

# Magic/Dunder Methods

# class FordK:
  
#     cant_ruedas = 4
    
#     def __init__(self, color='Verde', puertas=5):
#         self.color = color
#         self.puertas = puertas
#         self.radio = True
        
#     def tocar_bocina(self):
#         print('Pi pi!!')
    
#     def __str__(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'


# auto1 = FordK('Negro', 4)
# auto2 = FordK('Rojo', 2)
# auto3 = FordK(puertas=2)
# auto4 = FordK('Rojo')
# # auto5 = FordK()


# class Concesionaria:
    
#     def __init__(self, nombre, autos_en_venta=[]):
#         self.nombre = nombre
#         self.autos_en_venta = autos_en_venta
    
#     def __str__(self):
#         return f'Esta es la consecionaria {self.nombre}.'
    
#     def __len__(self):
#         return len(self.autos_en_venta)
    
#     def __getitem__(self, ubicacion):
#         return self.autos_en_venta[ ubicacion - 1 ]
    
#     def __setitem__(self, ubicacion, nuevo_dato):
#         self.autos_en_venta[ ubicacion - 1 ] = nuevo_dato
        
#     def __iter__(self):
#         for auto in self.autos_en_venta:
#             yield auto
    
# concesionaria = Concesionaria('asd', ['auto1', 'auto2'])

# for dato in consecionaria:
    
# concesionaria1 = Concesionaria('Grillo', [auto1, auto2])
# print(concesionaria1)
# print(len(concesionaria1))
# print(concesionaria1[1])
# concesionaria1[1] = auto5
# print(concesionaria1[1])
# for elemento in concesionaria1:
#     print(elemento)



'''
============================================================================================
============================================================================================
'''





# print('================================================================================================================')

# Relaciones entre clases 

# class Motor:
#     def __init__(self, valvulas):
#         self.valvulas = valvulas
        
# class LevantaVidrios:
#     def __init__(self, velocidad):
#         self.velocidad = velocidad

# class Auto:
    
#     def __init__(self, puertas, color, motor, levanta_vidrios=[]):
#         self.puertas = puertas
#         self.color = color
#         self.motor = motor
#         self.levanta_vidrios = levanta_vidrios
        
# motor1 = Motor(12)
# auto1 = Auto(4, 'Negro', motor1)

# print(auto1.motor.valvulas)

# print('================================================================================================================')


# Encapsulamiento

# class Persona:
    
#     def __init__(self, dni, color_de_pelo, cant_cirugias):
#         self.__dni = dni
#         self.color_de_pelo = color_de_pelo
#         self.__cant_cirugias = cant_cirugias
        
#     def __mostrar_dni(self):
#         print(self.__dni)
        
#     # getters
#     def get_dni(self):
#         return self.__dni
    
#     # setters
#     def set_dni(self, valor_nuevo):
#         self.__dni = valor_nuevo
        

# persona1 = Persona(123123, 'castanio', 5)
# print(persona1.color_de_pelo)
# persona1.color_de_pelo = 'canoso'
# print(persona1.color_de_pelo)
# # print(persona1.__dni)
# # persona1.__dni = 222
# persona1.set_dni(222)
# persona1.mostrar_dni()
# # print(persona1.__cant_cirugias)
# print(persona1.get_dni())
# # persona1.dni = 43434343
# # persona1.__dni = 43434343
# print(persona1.get_dni())
# # # print(persona1.__dni)
    
# print('================================================================================================================')
# print('================================================================================================================')
# print('================================================================================================================')
# print('================================================================================================================')

# Ejemplos extras

# print('================================================================================================================')



# Utilizar para v2 del MiDIc.__str__
# def format_if_string(valor_a_corroborar):
#     if type(valor_a_corroborar) == str:
#         return f"'{valor_a_corroborar}'"
#     return valor_a_corroborar


# class MiDic:
    
#     def __init__(self, **kwargs):
#         self.llaves = []
#         self.valores = []
#         if len(kwargs) > 0:
#             for llave, valor in kwargs.items(): 
#                 self.llaves.append(llave)
#                 self.valores.append(valor)
    
#     def __str__(self):
#         midic_en_string = '{'
#         for indice, llave in enumerate(self.llaves):
#             if indice > 0:
#                 midic_en_string += ', '
                
#             # v1
#             midic_en_string += f"{llave}: {self.valores[indice]}"
#             if type(llave) == str:
#                 midic_en_string = midic_en_string.replace(llave, f"'{llave}'")
#             if type(self.valores[indice]) == str:
#                 midic_en_string = midic_en_string.replace(self.valores[indice], f"'{self.valores[indice]}'")
        
#             # v2
#             # midic_en_string += f"{format_if_string(llave)}: {format_if_string(self.valores[indice])}"
            
#         midic_en_string += '}'
#         return midic_en_string
    
#     def __len__(self):
#         return len(self.llaves)
    
#     def __getitem__(self, llave):
#         index_valor = self.llaves.index(llave)
#         return self.valores[index_valor]
    
#     def __setitem__(self, llave, valor_nuevo):
#         index_valor = self.llaves.index(llave)
#         self.valores[index_valor] = valor_nuevo
    
#     def __iter__(self):
#         for llave in self.llaves:
#             yield llave
        
    
# midic1 = MiDic(
#     llave1='valor1',
#     llave2='valor2',
#     llave3='valor3',
#     llave4='valor4'
# )

# print(midic1)
# print(len(midic1))
# print(midic1['llave2'])
# midic1['llave2'] = 'valor nuevo de la llave 2'
# print(midic1['llave2'])

# for llave in dicc:
#     print(f'La llave {llave} contiene el valor {dicc[llave]}')

# ======================================================
# ======================================================


# class Motor:
#     def __init__(self, valvulas):
#         self.valvulas = valvulas
    
#     def __str__(self):
#         return f'Este motor es de {self.valvulas} valvulas.'
    
# motor = Motor(12)
# print(motor)

# class FordK:
  
#     cant_ruedas = 4
    
#     def __init__(self, color='Verde', puertas=5):
#         self.color = color
#         self.puertas = puertas
#         self.metros_recorridos = 0
#         self.fabricar()
    
#     def __str__(self):
#         return f'Ford K -> puertas: {self.puertas}, color: {self.color}'
        
#     def tocar_bocina(self):
#         print('Pi pi!!')
    
#     def describir_auto(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'

#     def fabricar(self):
#         print(f'Se fabrico un Ford K {self.color} de {self.puertas} puertas.')
        
#     def avanzar(self, metros):
#         print(f'el auto avanzo {metros} metros')
#         self.metros_recorridos += metros


# auto1 = FordK('Negro', 4)
# print(auto1)
# auto2 = FordK('Negro')

# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1.describir_auto())

# ======================================================
# ======================================================

# Magic/Dunder Methods

# class Concesionaria:
    
#     def __init__(self, concesionaria):
#         self.concesionaria = concesionaria
#         self.autos = []

#    # https://www.geeksforgeeks.org/str-vs-repr-in-python/
#    def __str__(self):
#        return f'Listado de autos en la consecionaria "{self.concesionaria}"'
        
#     def __len__(self):
#         return len(self.autos)
    
#     def agregar_auto(self, auto):
#         if auto:
#             self.autos.append(auto)
#         else:
#             print('Te falto el auto.')

# concesionaria = Concesionaria('Gimenez')
# print(concesionaria)
# print(len(concesionaria))
# concesionaria.agregar_auto(auto1)
# print(len(concesionaria))

# ======================================================
# ======================================================

# class Concesionaria:
    
#     def __init__(self, concesionaria):
#         self.concesionaria = concesionaria
#         self.autos = []
        
#     def __str__(self):
#         return f'Listado de autos en la consecionaria "{self.concesionaria}"'
        
#     def __len__(self):
#         return len(self.autos)
    
#     def agregar_auto(self, auto):
#         if auto:
#             self.autos.append(auto)
#         else:
#             print('Te falto el auto.')
        
#     def __getitem__(self, posicion):
#         try:
#             return self.autos[posicion]
#         except:
#             return 'No se encontro ese auto'

# concesionaria = Concesionaria('Gimenez')
# print(concesionaria)
# concesionaria.agregar_auto(auto1)
# print(concesionaria[0])


# ======================================================
# ======================================================

# class Concesionaria:
    
#     def __init__(self, concesionaria):
#         self.concesionaria = concesionaria
#         self.autos = []
        
#     def __str__(self):
#         return f'Listado de autos en la consecionaria "{self.concesionaria}"'
        
#     def __len__(self):
#         return len(self.autos)
    
#     def agregar_auto(self, auto):
#         if auto and auto.color == 'Negro':
#             self.autos.append(auto)
#         else:
#             print('Te falto el auto de color negro.')
        
#     def __getitem__(self, posicion):
#         try:
#             return self.autos[posicion]
#         except:
#             return 'No se encontro ese auto'
        
#     def __setitem__(self, posicion, nuevo_auto):
#         try:
#             if nuevo_auto.color == 'Negro':
#                 self.autos[posicion] = nuevo_auto
#             else:
#                 print('El auto no es negro.')
#         except:
#             print('No se pudo modificar el auto de la posicion {posicion}.')


# concesionaria = Concesionaria('Gimenez')
# print(concesionaria)
# concesionaria.agregar_auto(auto1)
# print(concesionaria[0])
# concesionaria[0] = auto2
# print(concesionaria[0])

# ======================================================
# ======================================================

# class Concesionaria:
    
#     def __init__(self, concesionaria):
#         self.concesionaria = concesionaria
#         self.autos = []
        
#     def __str__(self):
#         return f'Listado de autos en la consecionaria "{self.concesionaria}"'
        
#     def __len__(self):
#         return len(self.autos)
    
#     def agregar_auto(self, auto):
#         if auto and auto.color == 'Negro':
#             self.autos.append(auto)
#         else:
#             print('Te falto el auto de color negro.')
        
#     def __getitem__(self, posicion):
#         try:
#             return self.autos[posicion]
#         except:
#             return 'No se encontro ese auto'
        
#     def __setitem__(self, posicion, nuevo_auto):
#         try:
#             if nuevo_auto.color == 'Negro':
#                 self.autos[posicion] = nuevo_auto
#             else:
#                 print('El auto no es negro.')
#         except:
#             print('No se pudo modificar el auto de la posicion {posicion}.')
        
#     def __iter__(self):
#         for auto in self.autos:
#             yield auto

# concesionaria = Concesionaria('Gimenez')
# print(concesionaria)
# concesionaria.agregar_auto(auto1)
# concesionaria.agregar_auto(auto2)

# for valor in [1,2,3,4]:
#     print(valor)
    
# for valor in concesionaria:
#     print(valor)

# ======================================================
# ======================================================

# Encapsulamiento

# class Auto:
#     def __init__(self, modelo, marca, patente, chasis):
#         self.modelo = modelo
#         # self.marca = marca
#         self.patente = patente
#         # self.chasis = chasis
#         self._marca = marca
#         self.__chasis = chasis
    
#     def __arrancar(self):
#         print('Prrmmm!')
        
#     def podemos_arrancar(self):
#         self.__arrancar()
        
    # def get_chasis(self):
    #     return self.__chasis
        # if self._marca == 'fiat':
        #     return self.__chasis
        # else:
        #     return 'no se puede mostrar, estas limitado'
        
#     def set_chasis(self, nuevo_valor):
#         self.__chasis = nuevo_valor
#         # if self._marca == 'fiat':
#         #     self.__chasis = nuevo_valor
#         # else:
#         #     print('no se puede mostrar, estas limitado')
            
#     # def set_chasis(self):
#     #     if self._marca == 'fiat':
#     #         self.__chasis = self.__chasis[1:]
#     #     else:
#     #         print('no se puede mostrar, estas limitado')
        

# auto1 = Auto('uno', 'fiat', 'asd 123', 'AUSHDKBuaqw231323')
# auto2 = Auto('K', 'Ford', 'asd 113', 'AUSHDKBuaqw131323')
# # print(auto1.modelo)
# # print(auto1.marca)
# # print(auto1.patente)
# # print(auto1.chasis)
# # print(auto1._marca)
# print(auto1.__chasis)
# # print(auto1._Auto__chasis)
# # print(auto1.get_chasis())
# print(auto1.get_chasis())
# auto1.__chasis = 123
# print(auto1.__chasis)
# auto1.set_chasis(123)
# print(auto1.get_chasis())
# # print(auto2.get_chasis())
# # # auto1.__chasis = 123
# # auto2.set_chasis(123)
# # print(auto2.get_chasis())

# # auto1.__arrancar()
# auto1.podemos_arrancar()

# ======================================================
# ======================================================

# class Cuenta:
#     def __no_es_cero(self, valor):
#         return valor == 0
        
#     def dividir(self, num1, num2):
#         if not self.__no_es_cero(num2):
#             return num1 / num2
#         else:
#             return 'El segundo valor no tiene que ser cero'
        
# cuenta1 = Cuenta()

# print(cuenta1.dividir(1,1))
# cuenta1.__no_es_cero(1)

