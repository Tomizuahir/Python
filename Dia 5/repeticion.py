def repeticion(*args):
    contador = 0
    
    for num in args:
        
        
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False    
resultado = repeticion(0,6,1,0,9,3,5,0)
print(resultado)