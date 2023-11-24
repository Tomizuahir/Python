from pathlib import Path, PureWindowsPath #PureWindowsPath transforma cualquier ruta en una ruta de windows

carpeta = Path("C:/Users/tomaszh/Desktop/Visitar/Python/Dia 6/pruebas.txt")

ruta_windows = PureWindowsPath(carpeta)

#print(carpeta.read_text())# lee el texto del archivo
#print(carpeta.name)#trae el nombre del archivo
#print(carpeta.suffix)#devuelve el sufijo o formato del archivo
#print(carpeta.stem)#nos devuelve el nombre sin la terminacion o sufijo

'''if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")'''
print(ruta_windows)

