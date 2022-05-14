def Funcion(FString): # FUNCION FUNCIONA UNICAMENTE CON UNA ESTRUCTURA CORRECTA
    ListElemento = FString.split(" ")
    resultado = 0
    for i in range(len(ListElemento)):
        if (ListElemento[i] == "+"):
            if(resultado==0):
                resultado += int(ListElemento[i-1]) + int(ListElemento[i+1])
            else:
                resultado += int(ListElemento[i+1])

        if (ListElemento[i] == "-"):
            if(resultado==0):
                resultado += int(ListElemento[i-1]) - int(ListElemento[i+1])
            else:
                resultado -= int(ListElemento[i+1])

        if (ListElemento[i] == "*"):
            if(resultado==0):
                resultado += int(ListElemento[i-1]) * int(ListElemento[i+1])
            else:
                resultado *= int(ListElemento[i+1])
    return resultado
    
funcion = "10 * 10 - 100 " 
print(Funcion(funcion))

"resultado - 1 " 