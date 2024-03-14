# from abc import ABC, abstractclassmethod

# class Persona(ABC):
#     @abstractclassmethod
#     def __init__(self,nombre,edad,sexo,actividad):
#         self.nombre = nombre
#         self.edad = edad
#         self.sexo = sexo
#         self.actividad = actividad
        
#     @abstractclassmethod
#     def hacer_actividad(self):
#         pass
    
#     def presentarse(self):
#         print(F"Hola me llamo: {self.nombre} y tengo: {self.edad}")
        
# class Estudiante(Persona):
#     def __init__(self,nombre,edad,sexo,actividad):
#         super().__init__(nombre,edad,sexo,actividad)
        
#     def hacer_actividad(self):
#         print(f"Estoy estudiando: {self.actividad}")
        
# class Trabajador(Persona):
#     def __init__(self,nombre,edad,sexo,actividad):
#         super().__init__(nombre,edad,sexo,actividad)
        
#     def hacer_actividad(self):
#         print(f"Actualmente estoy trabajando en el area de: {self.actividad}")
        
# huxx = Estudiante("Chris",35,"Masculino","Programacion")
# pinchicha = Trabajador("Makima",25,"Demonio","Jujutsu Kaisen")

# huxx.presentarse()
# huxx.hacer_actividad()
# pinchicha.presentarse()
# pinchicha.hacer_actividad()        