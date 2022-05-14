
def recursivo(numero, contador): # 1
    if(contador == numero): # Condicion de parada 
        return numero
    else:
        return contador + recursivo(9, contador+1)
    
def Fibonacci(numero):
    if(numero == 0):
        return 0
    if(numero == 1):
        return 1
        
    return Fibonacci(numero-1) + Fibonacci(numero-2)
    

if __name__ == '__main__':
    print(recursivo(9,0))
    print(Fibonacci(9))


