# class Vehiculo:
    
#     def __init__(self, marca, motor):
#         self.marca = marca
#         self.motor = motor
    
#     def soy(self):
#         # print(f'Soy un', type(self).__name__)
#         return f'Soy un {type(self).__name__}'

# class Movimientos:
    
#     def avanzar(self, metros):
#         return f'{type(self).__name__} avanzo {metros} metros.'
    
# class VehiculoTerrestre(Vehiculo, Movimientos):
    
#     def __init__(self, cant_ruedas, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.cant_ruedas = cant_ruedas

# class Auto(VehiculoTerrestre):
    
#     # # v1
#     # def __init__(self, cant_ruedas, marca, motor):
#     #     self.cant_ruedas = cant_ruedas
#     #     self.marca = marca
#     #     self.motor = motor
    
#     # # v2
#     # def __init__(self, cant_ruedas, marca, motor):
#     #     super().__init__(marca, motor)
#     #     self.cant_ruedas = cant_ruedas
        
#     # # v3
#     # def __init__(self, cant_ruedas, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     self.cant_ruedas = cant_ruedas
#     ...
        

# class Moto(VehiculoTerrestre):
#     ...

# class Camion(VehiculoTerrestre):
#     ...
    
# class Lancha(Vehiculo):
    
#     def soy(self):
#         mensaje_del_padre = super().soy()
#         return mensaje_del_padre.replace('un', 'una')

#     def avanzar(self, nudos):
#         return f'{type(self).__name__} avanzo {nudos} nudos.'


# class Perro:
    
#     def avanzar(self, pasos):
#         return f'El perro avanza siempre {pasos} pasos.'



# motor_v8 = 'v8'
# motor_v12 = 'v12'
# ford = 'Ford'
# fiat = 'Fiat'

# auto = Auto(4, fiat, motor_v12)
# moto = Moto(2, fiat, motor_v12)
# camion = Camion(6, fiat, motor_v12)
# lancha = Lancha(ford,motor_v8)

# # print(auto.avanzar(30))
# # print(moto.avanzar(15))
# # print(lancha.avanzar(20))


# # print(Lancha.__mro__)
# # print(Auto.__mro__)
# # print(Vehiculo.__mro__)

# listado_cosas = [auto, moto, camion, lancha, Perro()]


# def ejecutar_avanzar(objeto, espacio):
#     print(objeto.avanzar(espacio))

# for indice, cosa in enumerate(listado_cosas):
#     ejecutar_avanzar(cosa, indice)



# Figuras
# Define una clase Figura con un método de instancia 
# area que devuelve el área de la figura. Luego, crea 
# clases hijas como Circulo y Rectangulo que hereden de 
# Figura y proporcionen implementaciones diferentes del método area.

import math

class Figura:
    
    def area(self):
        ...
    
    # v2
    def mostrar_area(self):
        print(self.area())

class Circulo(Figura):
    
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2


class Rectangulo(Figura):
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura


circulo = Circulo(3)
rectangulo = Rectangulo(3,5)

# # v1
# def mostrar_area(figura):
#     print(figura.area())

# for figura in [circulo, rectangulo]:
#     mostrar_area(figura)

# v2
for figura in [circulo, rectangulo]:
    figura.mostrar_area()






















# class Animal:
#     def tipo_animal(self):
#         print(f'Yo soy un', type(self).__name__)

# class Perro(Animal):
#     def hablar(self):
#         print('Guau guau!!')
        
# class Gato(Animal):
#     def hablar(self):
#         print('Miau miau!!')
    
# class Abeja(Animal):
#     ... # pass

# gato = Gato()
# perro = Perro()
# abeja = Abeja()

# gato.tipo_animal()
# gato.hablar()

# perro.tipo_animal()
# perro.hablar()

# abeja.tipo_animal()


##################################################################
##################################################################

# class Vehiculo:
#     def __init__(self, marca):
#         self.marca = marca
        
#     def descripcion(self):
#         return f'{type(self).__name__} marca: {self.marca}'

# class Auto(Vehiculo):
#     ...
        
# class Lancha(Vehiculo):
#     # v1
#     # def __init__(self, tipo_ancla, marca):
#     #     self.tipo_ancla = tipo_ancla
#     #     self.marca = marca
    
#     # v2
#     def __init__(self, tipo_ancla, marca):
#         super().__init__(marca)
#         self.tipo_ancla = tipo_ancla
        
#     # v3
#     # def __init__(self, tipo_ancla, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     self.tipo_ancla = tipo_ancla
    
    
#     def descripcion(self):
#         return super().descripcion() + f'. Ancla {self.tipo_ancla}'
        
# class Moto(Vehiculo):
#     ...

        
# auto = Auto('Ford')
# print(auto.descripcion())

# lancha = Lancha('sin cepo', 'Bermuda')
# print(lancha.descripcion())

# moto = Moto('Yamaha')
# print(moto.descripcion())

# vehiculo = Vehiculo('Fiat')
# print(vehiculo.descripcion())








# class Animal:
#     def __tipo_animal(self):
#         print(f'Yo soy un', type(self).__name__)
    
#     def hablar(self):
#         print('Animal hablando')
        
# class AnimalTerrestre(Animal):
#     def caminar(self):
#         print(f'{type(self).__name__} esta caminando.')
        
#     def tiene_cola(self):
#         print('Soy terrestre y no tengo cola')
        
# class AnimalAcuatico(Animal):
#     def nadar(self):
#         print(f'{type(self).__name__} esta nadando.')
        
#     def tiene_cola(self):
#         print('Soy acuatico y no tengo cola')

# class Perro(AnimalTerrestre):
#     def hablar(self):
#         print('Guau guau!!')
        
# class Delfin(AnimalAcuatico):
#     # def nadar(self):
#     #     print('Hola soy un delfin nadando')
#     ...

# class Pato(AnimalAcuatico, AnimalTerrestre):
#     def hablar(self):
#         print('Cuak cuak!!')


# perro = Perro()
# perro.caminar()
# perro.hablar()
# perro.tipo_animal()
# print('####################')
# delfin = Delfin()
# delfin.nadar()
# delfin.tipo_animal()
# print('####################')
# pato = Pato()
# pato.caminar()
# pato.hablar()
# pato.nadar()
# pato.tipo_animal()
# pato.tiene_cola()
# print(Pato.__mro__)

# lista_de_animales1 = [Pato(), Perro(), Delfin(), Pato(), Perro(), Perro(), Delfin()]

# for animal in lista_de_animales1:
#     animal.tipo_animal()


# lista_de_animales2 = [Pato(), Perro(), Pato(), Perro(), Perro()]

# for animal in lista_de_animales2:
#     animal.hablar()















# # Definimos una clase padre
# class Animal:
#     def __init__(self, especie, edad):
#         self.especie = especie
#         self.edad = edad
        
#     # Metodo generico pero con implementacion particular
#     def hablar(self):
#         # Metodo vacio
#         pass
    
#     # Metodo generico pero con implementacion particular
#     def moverse(self):
#         # Metodo vacio
#         pass
    
#     # Metodo generico con la misma implementacion
#     def describeme(self):
#         print('Soy un Animal del tipo', type(self).__name__)

# # Perro hereda de Animal
# class Perro(Animal):     
#     def __init__(self, especie, edad, duenio):
#         # Alternativa 1
#         # self.especie = especie
#         # self.edad = edad
#         # self.duenio = duenio
        
#         # Alternativa 2
#         super().__init__(especie, edad)
#         self.duenio = duenio
        
# mi_perro = Perro('mamifero', 10, 'Luis')
# print(mi_perro.especie)
# print(mi_perro.edad)
# print(mi_perro.duenio)
           
#     def hablar(self):
#         print("Guau!")
#     def moverse(self):
#         print("Caminando con 4 patas")
# class Vaca(Animal):        
#     def hablar(self):
#         print("Muuu!")
#     def moverse(self):
#         print("Caminando con 4 patas")
# class Abeja(Animal):        
#     def hablar(self):
#         print("Bzzz!")
#     def moverse(self):
#         print("Volando")
        
#     # Nuevo metodo
#     def picar(self):
#         print('Picar!')
    
    
# mi_perro = Perro('mamifero', 10)
# mi_vaca = Vaca('mamifero', 23)
# mi_abeja = Abeja('insecto', 1)

# mi_perro.hablar()
# mi_vaca.hablar()
# # Guau!
# # Muuu!

# mi_vaca.describeme()
# mi_abeja.describeme()
# # Soy un Animal del tipo Vaca
# # Soy un Animal del tipo Abeja

# mi_abeja.picar()
# # Picar!

# Soy un Animal del tipo Perro

# ======================================================
# ======================================================

# class Clase1:
#     ...
# class Clase2:
#     ...
# class Clase3(Clase1, Clase2):
#     ...

# print(Clase3.__mro__)
# # (<class '__main__.Clase3'>, <class '__main__.Clase1'>, <class '__main__.Clase2'>, <class 'object'>)

# class Clase1:
#     ...
# class Clase2:
#     ...
# class Clase3:
#     ...
# class Clase4(Clase1, Clase2, Clase3):
#     ...

# print(Clase4.__mro__)
# (<class '__main__.Clase4'>, <class '__main__.Clase1'>, <class '__main__.Clase2'>, <class '__main__.Clase3'>, <class 'object'>)


# class Perro():        
#     def hablar(self):
#         print("Guau!, Guau!")
        
# class Gato():        
#     def hablar(self):
#         print("Miau!, Miau!")
# class Animal():        
#     def hablar(self):
#         ...
        
# pato = Pato()
# pato.hablar()
# # Cua!, Cua!

# obrero1 = Obrero()
# obrero1.mensaje()

# def llama_hablar(x):
#     x.hablar()
    
# lista = [, Vaca()]
# for animal in Perro(), Gato():
#     animal.hablar()

# # Guau!, Guau!
# # Miau!, Miau!
# # Muuu!, Muuu!

# def sumar(n1, n2):
#     print(f'La suma me da: {n1+n2}')

# def restar(n1, n2):
#     print(f'La resta me da: {n1-n2}')
# mensaje desde la clase Obrero

# DRY

# class Auto:
#     def __init__(self, marca):
#         self.marca = marca
        
#     def descripcion(self):
#         print(f'Soy un {type(self).__name__} {self.marca}')
        
# class Lancha:
#     def __init__(self, marca):
#         self.marca = marca
        
#     def descripcion(self):
#         print(f'Soy un {type(self).__name__} {self.marca}')
    
        
# auto = Auto('Ford')
# auto.descripcion()

# lancha = Lancha('Bermuda')
# lancha.descripcion()


# ======================================================
# ======================================================


# class Vehiculo:
#     def __init__(self, marca):
#         self.marca = marca
        
#     def descripcion(self):
#         print(f'{type(self).__name__} marca: {self.marca}')

# class Auto(Vehiculo):
#         ...
        
# class Lancha(Vehiculo):
#         ...
        
# class Moto(Vehiculo):
#         ...

        
# auto = Auto('Ford')
# auto.descripcion()

# lancha = Lancha('Bermuda')
# lancha.descripcion()

# moto = Moto('Yamaha')
# moto.descripcion()


# ======================================================
# ======================================================

# class Vehiculo:
#     def __init__(self, marca):
#         self.marca = marca
        
#     def descripcion(self):
#         print(f'{type(self).__name__} marca: {self.marca}')

# class Auto(Vehiculo):
#     def __init__(self, marca, vidrios_blindados):
#         self.marca = marca
#         self.vidrios_blindados = vidrios_blindados
        
        
# class Lancha(Vehiculo):
        
#     def anclar(self):
#         print('Lancha anclada!')

        
# auto = Auto('Ford', True)
# auto.descripcion()

# lancha = Lancha('Bermuda')
# lancha.descripcion()
# lancha.anclar()


# ======================================================
# ======================================================


# class Vehiculo:
#     def __init__(self, marca, motor):
#         self.marca = marca
#         self.motor = motor
        
#     def descripcion(self):
#         print(f'{type(self).__name__} marca: {self.marca}')

# class Auto(Vehiculo):
#     # v1
#     # def __init__(self, motor, marca, vidrios_blindados):
#     #     self.marca = marca
#     #     self.motor = motor
#     #     self.vidrios_blindados = vidrios_blindados
    
#     #v2 Uso de super()
#     def __init__(self, vidrios_blindados, motor, marca):
#         super().__init__(motor, marca)
#         # self.marca = 'Pepito'
#         self.vidrios_blindados = vidrios_blindados
        
#     #v3 Uso de super() y *args/**kwargs
#     # def __init__(self, vidrios_blindados, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     # self.marca = 'Pepito'
#     #     self.vidrios_blindados = vidrios_blindados
        
#     def descripcion(self):
#         super().descripcion()
#         if self.vidrios_blindados:
#             print('Tengo vidrios blindados')
#         else:
#             print('No tengo vidrios blindados')
        
# class Lancha(Vehiculo):
        
#     def anclar(self):
#         print('Lancha anclada!')

# # auto = Auto(marca='Ford', vidrios_blindados=True, motor='v12')
# auto = Auto(True, 'Ford', 'v8')
# auto.descripcion()

# lancha = Lancha('Bermuda', 'v12')
# lancha.descripcion()
# lancha.anclar()

# ======================================================
# ======================================================

# class Vehiculo:
#     def __init__(self, marca):
#         self.marca = marca
        
#     def descripcion(self):
#         print(f'{type(self).__name__} marca: {self.marca}')
        
# class VehiculoAcuatico(Vehiculo):
    
#     def anclar(self):
#         print(f'{type(self).__name__} se anclo!')

# class TransporteTerrestre:
    
#     cant_ruedas = 4
    
#     def tocar_bocina(self):
#         print('Piii Piiiii!!!')
        
#     def descripcion(self):
#         print('Soy un Transporte Terrestre')

# class Auto(Vehiculo, TransporteTerrestre):
#     def __init__(self, marca, vidrios_blindados):
#         super().__init__(marca)
#         self.vidrios_blindados = vidrios_blindados
        
# class Lancha(VehiculoAcuatico):
#     ...

# class Barco(VehiculoAcuatico):
#     ...

# print(Auto.__mro__)
# auto = Auto('Ford', True)
# auto.descripcion()
# auto.tocar_bocina()
# lancha = Lancha('Bermuda')
# lancha.descripcion()
# lancha = Barco('Pantalon Largo')
# lancha.descripcion()

# ======================================================
# ======================================================


# class Vehiculo:
#     def __init__(self, marca):
#         self.marca = marca
        
#     def descripcion(self):
#         print(f'{type(self).__name__} marca: {self.marca}')
        
#     def tocar_bocina(self, sonido):
#         print(sonido)

# class Auto(Vehiculo):
    
#     def tocar_bocina(self):
#         super().tocar_bocina("Piiii Piiiii!!")
        
# class Lancha(Vehiculo):
    
#     def tocar_bocina(self):
#         super().tocar_bocina("UUUuuuuuuu UUuuuuuu!!")
        
        
# def fabricar_vehiculo():
#     if input('Ingrese A para auto: ') == 'A':
#         return Auto(input('Ingrese marca de Auto: '))
#     else:
#         return Lancha(input('Ingrese marca de Lancha: '))
        

# vehiculo = fabricar_vehiculo()
# vehiculo.tocar_bocina()

# ======================================================
# ======================================================

# class Vehiculo:
#     def __init__(self, marca):
#         self.marca = marca
        
#     def descripcion(self):
#         print(f'{type(self).__name__} marca: {self.marca}')
        
#     def tocar_bocina(self):
#         ...

# class Auto(Vehiculo):
    
#     def tocar_bocina(self):
#         print("Piiii Piiiii!!")
        
# class Lancha(Vehiculo):
    
#     def tocar_bocina(self):
#         print("UUUuuuuuuu UUuuuuuu!!")
        
        
# def fabricar_vehiculo():
#     if input('Ingrese A para auto: ') == 'A':
#         return Auto(input('Ingrese marca de Auto: '))
#     else:
#         return Lancha(input('Ingrese marca de Lancha: '))
        

# vehiculo = fabricar_vehiculo()
# vehiculo.tocar_bocina()