#CREACION DE UN ARCHIVO O FICHERO BINARIO
#import pickle

# lista_nombres = ["pedro","ana","maria","isabel"]

# fichero_binario=open("fb_lista_nombres","wb")#--> variable=metodo open  recibe dos argumentos el primero nombre del fichero, segundo argtumento tipo de permiso (wb=escritura binaria)

#despues de haber creado el fichero se hace un volcado de la lista al fichero externo mediante el uso de metodo dump()

#sintaxis:
#biblioteca pickle . metodo dump este recibe dos argumentos (nombredelalista, ficherobinario) se volca la lista al fichero binario

# pickle.dump(fb_lista_nombres,fichero_binario)

# fichero_binario.close()

# del (fichero_binario)#borra de la memoria el ficherobinario con la funcion del

#------------------------------------------------------

#PARA RESCATAR LA INFORMACION DEL ARCHIVO BINARIO CREADO
#SE DEBE IMPORTAR LA BIBLIOTECA

import pickle #importamos la biblioteca pickle

fichero = open("fb_lista_nombres","rb")#creamos una variable a la que le asignamos lo que devuelva el metodo open que recibe dos argumentos(nombredelfichero, permisos) en este caso se usa rb=leer archivos binarios (read binary)

lista = pickle.load(fichero)#en la variable lista asignamos lo que devuelva la biblioteca pickle a traves de su metodo load el cual recibe como parametro un fichero binario

print(lista)#mediante la funcion print mostramos por consola lo que tiene almacenado la variable lista

