def main():
    print("HUCHA")
    contraseña1 = input("¿Cuantos pesos quiere ahorrar?: ")
    contraseña2 = input("Escriba su nueva contraseña: ")
    
    while contraseña1 != contraseña2:
        print("Las contraseñas no coinciden, vuelva a ingresar")
        contraseña1 = input("Escriba su contraseña: ")
        contraseña2 = input("Escriba su nueva contraseña: ")
    print("Contraseña confirmada, hasta la vista!")
if __name__=="__main__":
    main()