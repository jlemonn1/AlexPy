class Persona:
    #Declaramos constructor
    def __init__(self, nombre, edad, genero):
        self._nombre = nombre
        self._edad = edad
        self._genero = genero

    #Getters --> nos devolvia el valor del atributo
    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad
    
    def get_genero(self):
        return self._genero
    #Actualizar el valor del atributo
    def set_nombre(self, nombreNuevo):
        self._nombre = nombreNuevo

    def set_edad(self, edadNueva):
        self._edad = edadNueva

    def set_genero(self, generoNuevo):
        self._genero = generoNuevo

    def get_info(self):
        return f"nombre:  {self._nombre} , edad: {self._edad} , gen: {self._genero}"
        
    
    


persona = Persona("Pepe" , 12, "Hombre")
print(persona.get_info)

 



    
