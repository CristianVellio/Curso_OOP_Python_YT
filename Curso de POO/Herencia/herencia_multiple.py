#class Persona:
    #def __init__(self,nombre,edad,nacionalidad):
        #self.nombre = nombre
        #self.edad = edad
        #self.nacionalidad = nacionalidad
        
    #def hablar(self):
        #print("Hola estoy hablando un poco")
        
#class Empleado(Persona):
    #def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
    #    super().__init__(nombre, edad, nacionalidad)
     #   self.trabajo = trabajo
      #  self.salario = salario
        
#class Artista:
 #   def __init__(self,habilidad):
  #      self.habilidad = habilidad

   # def mostrar_habilidad(self):
    #    return f"Mi habilidad es: {self.habilidad}"
    
#class EmpleadoArtista(Persona,Artista):
 #   def __init__(self, nombre, edad, nacionalidad,habilidad,empresa,salario):
  #      Persona.__init__(self,nombre,edad,nacionalidad)
   #     Artista.__init__(self,habilidad)
    #    self.salario = salario
     #   self.empresa = empresa
        
   # def presentarse(self):
    #     print(f"Hola soy: {self.nombre}, {self.mostrar_habilidad()}, y trabajo en {self.empresa}")
    
#Roberto = EmpleadoArtista("Roberto",43,"argentino","Cantar","Google",100000)

#herencia = issubclass(EmpleadoArtista,Artista)
#instancia = isinstance(Roberto,EmpleadoArtista)
#print(instancia)