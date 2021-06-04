

import pickle

class Archivo:

 
    def CrearArchivo(self,texto):

        archivob = open("ficherob","wb")

        pickle.dump(texto,archivob)

        print("La informacion fue agregada: \n",texto)

        archivob.close()

        del (archivob)
    
    def LeerArchivo(self):
        archivob = open("ficherob","rb")

        info = pickle.load(archivob)

        print("La informacion del archivo binario es: \n", info)

        archivob.close()

        del (archivob)
    

doc = Archivo()






