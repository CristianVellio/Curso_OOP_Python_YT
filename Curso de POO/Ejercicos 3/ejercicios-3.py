# class Personaje:
#     def __init__(self, nombre, fuerza, velocidad):
#         self.nombre = nombre
#         self.fuerza = fuerza
#         self. velocidad = velocidad
        
#     def __repr__(self):
#         return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
#     def __add__(self,otro_pj):
#         nuevo_nombre = self.nombre + "-" + otro_pj.nombre
#         nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.5)  #SACAMOS EL PROMEDIO SUMANDO LOS FACTORES DIVIDIENDO POR LA CANTIDAD
#         nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.5)  #DE FACTORES Y ELEVANDO A LA POTENCIA 2
#         return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    
# denji = Personaje("Denji",100,100)
# power = Personaje("Power",90,90)
# makima = Personaje("Control Demon",200,200)

# demon = denji + power
# chaos = demon + makima
# print(chaos)
# print(demon)
# print(denji)
# print(power)
# print(makima)