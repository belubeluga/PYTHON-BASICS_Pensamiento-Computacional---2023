#-------------------- SISTEMAS NUMERICOS -------------------- 20/10

'''SISTEMAS NUMERICOS POSICIONALES'''
# BINARIO (B=2)
    #1 bit = 2^bits combinaciones = 2
    #2 bits = 2^2 combo = 4
    #0 = 2^0 -1
# OCTAL (B=8)
# DECIMAL (B=10)
    #valor por base^pos
# HEXADECIMAL (B=16)
    #123456789ABCDEF
    #con 4 simbolo H puedo representar 4 bits

#1 byte = 8 bits
#con 4 bits --> 1 hexa

#MSB LSB

'''CONVERSION'''
# binario --> decimal
    # sumatoria de los digitos multiplicados por sus pesos

# decimal --> binario
def convertir_binario(numero:int)->str:
    if numero>0: #o 1
        return convertir_binario(numero//2)+str(numero%2) #ojo a estoy dando vuelta
    else: return '' #y aca str(numero)
convertir_binario(12)

# hexadecimal --> decimal
    #E*19**2 (analogo con binario)
    
# decimal --> hexadecimal
    #1. Se divide el número decimal por 16.
    #2. Se guarda el resto.
    #3. Se toma el cociente como nuevo dividendo y se repite desde paso 1 hasta que el cociente sea < 16.
    #4. Se guarda el último cociente
    #5. Se arma el número hexa tomando el último cociente como dígito más significativo y el primer resto como menos significativo,

# hexadecimal --> binario
    #juntando de a grupos de a 4 y convirtiendo a hexa
    # y si no es divisible x 4, lleno de 0 a la izq


'''SIGNO (POSITIVO/ NEGATIVO)'''
#NOTACION SIGNO MAGNITUD
#[bit signo][magnitus]
#el MSB da el signo
    # 1 --> (-)
    # 0 --> (+)

#COMPLEMENTO A 1
#  7 = 0111
# -7 = 1000

#COMPLEMENTO A 2
    #resuelve el tema del cero 
# PARTE POSITIVA (sin cambios)                  4 = 0100
# PARTE NEGATIVA (invertis bits y sumar 1)     -4 = 1100 (1011 + 1)
        #(no podes escribir 8, pero si el -8)

'''REPRESENTACION DE NUMEROS REALES'''
    #punto fijo     (parte entera , parte fraccionaria) (cuantizacion uniforme)
            #       (potencias positivas, potencias negativas)

    #punto flotante (notacion exponencial) (rango + amplio) (cuantizacion no uniforme)
            # [s][mantisa]2^[exponente]
            #signo, magnitud 
#IEE 754
# Precision simple (32 bits)
    # 1 bit signo, 8 exponente, 23 mantisa
# Presicion doble (64 bits)
    # 1 bit, 11 expo, 52 mantisa

#no puedo representar el 0 (underflow)
#PROCEDIMIENTO:
'''1. Se convierte el número a punto fijo binario (sin considerar el signo).
2. Mantisa: Se corre la coma (a derecha- o izquierda+) dejando siempre un bit en 1
como parte entera. La mantisa son todos los bits excepto el primero (ya que siempre está implícitamente). Se completa con ceros a derecha (mantisa de 23).
3. Exponente: se calcula como el número binario (8 bits p. simple, 11 bits p. doble) de bias-n (si es negativo) o bias+n (si es positivo), donde n es la cantidad de posiciones que se movió la coma y bias es 127 (p. simple) 0 1023 (p.idoble).
4. Se determina el bit de signo, 0 (+) o 1 (-).
5. Se arma el número en punto flotante como [Signo][Exponente][Mantisa)'''