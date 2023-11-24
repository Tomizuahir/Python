#import os 
from pathlib import Path

#ruta = os.getcwd()# devuelve la ruta en la que estamos
#ruta = os.chdir('C:\\Users\\tomaszh\\Desktop\\Alternativa') #cambiar ruta de carpeta
#ruta = os.makedirs('C:\\Users\\tomaszh\\Desktop\\Alternativa\\otra')# crea una nueva carpeta
#os.rmdir('C:\\Users\\tomaszh\\Desktop\\Alternativa\\otra')# elimina la carpeta
#elemento = os.path.basename(ruta)# nombre base del elemento
#elemento = os.path.dirname(ruta)# nombre del directorio, primera parte de la ruta
#elemento = os.path.split(ruta)# divide en una tupla el directorio y el elemento 

carpeta = Path('C:/Users/tomaszh/Desktop/Alternativa')# este metodo es para abrirlo desde windows como en mac
archivo = carpeta / 'documento.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())