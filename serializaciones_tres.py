
#SERIALIZACION DE UN OBJETO
import pickle

class Coche():#declaracion de la clase, se nombre con la primera letra en mayusculas
    #propiedades

    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.largochasis = 250
        self.anchoChasis = 120
        self.ruedas = 4
        self.enmarcha = False #para comprobar el estado del coche
    
    def infocoche(self):
        print("La marca del coche es: ",self.marca," el modelo es: ",self.modelo)

    def arrancar (self):
        self.enmarcha = True #cambia el estado a verdadero
               
    
    def estado(self):
        if(self.enmarcha):
            return "el coche esta en marcha"
        else:
            return "el coche esta parado"



coche1 = Coche("ford","ecosport")
coche2 = Coche("toyota","corolla")
coche3 = Coche("renaul","Megane")

coches =[coche1,coche2,coche3]#coleccion de objetos

fichero = open("loscoches","wb")
pickle.dump(coches,fichero)
fichero.close()
del (fichero)

#-----RECUPERAMOS INFORMACION DEL FICHERO

ficheroapertura =open("loscoches","rb")#a la variable le asiganmos lo que retorna el metodo open a traves del fichero binario, y le damos los permisos lectura binario rb

misCoches = pickle.load(ficheroapertura)#a la variable le asiganmos lo que devuelve la biblioteca pickle a traves de su metodo load que en este caso es el fichero binario

ficheroapertura.close()#cerramos el fichero

for c in misCoches:#recorremos los objetos almacenados en la coleccion de objetos devueltos del fichero binario
    c.infocoche()#aca mostramos por pantalla el metodo infocoche correspondiente a cada objeto




 
