
class Persona:

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

        #print("Se agrego una persona con el nombre de: ",self.nombre)

    def __str__(self):

        return "{} {}".format(self.nombre,self.edad)

    def llamarmensaje(self):

        self.mensaje()
    
    def mensaje(self):
        print("mensaje de la funcion")

class listaPersonas:
    listadepersona = []
    def agregarPersonas(self,objpersona):
        
        self.listadepersona.append(objpersona)
    
    def mostrarLista(self):
        for i in self.listadepersona:
            print(i)



p = Persona("alex",23)
lista = listaPersonas()
lista.agregarPersonas(p)
p = Persona("gabriel",32)
lista.agregarPersonas(p)
p = Persona("keidy",34)
lista.agregarPersonas(p)
lista.mostrarLista()

p.llamarmensaje()




    
