#lista_numeros = [range(1,1000)]


def devolver_distintos(num1,num2,num3):
    suma = num1+num2+num3
    
    if suma > 15:
        return max(num1,num2,num3)
    elif suma < 10:
        return min(num1,num2,num3)
    else:
        numeros_ordenados = sorted([num1,num2,num3])
        return numeros_ordenados[1]

   
      
    
         
    
        
resultado = devolver_distintos(5,6,3)
print(resultado)