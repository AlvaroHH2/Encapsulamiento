class alumno(object):
   def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

   @property
   def nombre(self):  # Definimos el método para obtener el nombre
        "Documentación del método nombre bla bla"  # Doc del método
        return self.__nombre

   @nombre.setter
   def nombre(self, nuevo):
        self.__nombre = nuevo
        print(self.__nombre)  # Aquí vuelvo a pedir que retorne el atributo para confirmar

        print("Modificando nombre..")


        print("El nombre se ha modificado por")

        print(self.__nombre)


   @nombre.deleter  # Propiedad DELETER
   def nombre(self):
     print("Borrando nombre..")
     del self.__nombre


   @property
   def edad(self):
        return self.__edad

   @edad.setter
   def edad(self, nuevo2):
         self.__edad = nuevo2
         print(self.__edad)
         print("Modificando edad..")

         print("La edad se ha modificado por")
         print(self.__edad)  # Aquí vuelvo a pedir que retorne el atributo para confirmar

alumnorec=alumno("Manuel",22)
alumnorec.nombre='Manolito'
alumnorec.edad=20
del alumnorec.nombre
#print(alumnorec.nombre)

