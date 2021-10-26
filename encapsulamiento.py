class alumno(object):  # Declaramos la clase principal Perros
    def __init__(self, nombre, edad):  # Definimos los parámetros
        self.__nombre = nombre  # Declaramos los atributos
        self.__edad = edad

    @property
    def nombre(self):  # Definimos el método para obtener el nombre
        "Documentación del método nombre bla bla"  # Doc del método
        return self.__nombre  # Aquí simplemente estamos retornando el atributo privado

    # Hasta aquí definimos los métodos para obtener los atributos ocultos o privados getter.
    # Ahora vamos a utilizar setter y deleter para modificarlos
    @nombre.setter  # Propiedad SETTER
    def nombre(self, nuevo):
        print("Modificando nombre..")
        self.__nombre = nuevo

        print("El nombre se ha modificado por")
        print(self.__nombre)
        print("Con una edad de ")
        print(self.__edad)# Aquí vuelvo a pedir que retorne el atributo para confirmar

    @nombre.deleter  # Propiedad DELETER
    def nombre(self):
        print("Borrando nombre..")
        del self.__nombre

    @property
    def edad(self):  # Definimos el método para obtener la edad #Automáticamente GETTER
        return self.__edad  # Aquí simplemente estamos retornando el atributo privado

    @edad.setter
    def edad(self, nuevaedad):

        self.__edad = nuevaedad
        print("La edad ahora es")
        print(self.__edad)

    @edad.deleter  # Propiedad DELETER
    def edad(self):
        print("Borrando edad..")
        del self.__edad


# Instanciamos
alumnorec = alumno('Manuel', 27)
print(alumnorec.nombre)  # Imprimimos el nombre de Tomas. Se hace a través de getter
# Que en este caso como esta luego de property lo toma como el primer método..
alumnorec.nombre = 'Pepe'  # Cambiamos el atributo nombre que se hace a través de setter
  # Volvemos a imprimir
alumnorec.edad = 28
del alumnorec.nombre  # Borramos el nombre utilizando deleter




