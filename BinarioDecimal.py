def Decimal2Binario(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

#Esta función sirve para convertir un número binario a decimal:
def Binario2Decimal(binario):
    n=len(binario)
    valor=0
    for bit in binario:
         if bit == '1':
              valor=valor+2**(n-1)
         n -=1
    return valor

 
