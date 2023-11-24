def ordenar_letras(palabra):

    letras_ordenadas=set(palabra)
    letras_ordenadas = sorted(letras_ordenadas)    

    return ''.join(letras_ordenadas)


resultado = ordenar_letras("entretenido")
print(resultado)
