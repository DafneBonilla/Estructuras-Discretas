#ejercicio1
def maximo_comun_divisor(x, y):
    if x < 0:
        return False
    if y < 0:
        return False
    i = 0
    while y != 0:
        i = y
        y = x % y
        x = i
    return x

#ejercicio2
def es_palindroma(cadena):  
    cadena = cadena.lower().replace(' ','') 
    """
    La función auxiliar -lower- se usó para cambiar todas las letras en la cadena a 
    minúsculas y facilitar la comparación de las cadenas
    La función auxiliar -replace- se usó para eliminar los espacios y dar un resultado correcto
    """
    cadena_reversa = ""
    for letra in cadena:
        cadena_reversa = letra + cadena_reversa
    if cadena_reversa == cadena:
        return True
    else:
        return False

#ejercicio3
def promedio_tuplas(tuplas):
    lista = [] 
    for i in range(len(tuplas)):
        promedio = 0
        promedio = sum(tuplas[i])/len(tuplas[i])
        lista.append(promedio)
    return lista        
        
#ejercicio4
def permutaciones(nums):   
    if len(nums) == 0: 
        return [] 
    if len(nums) == 1: 
        return [nums] 
    lista = [] 
    for i in range(len(nums)): 
       contenido = nums[i] 
       lista2 = nums[:i] + nums[i+1:]
       for a in permutaciones(lista2): 
           lista.append([contenido] + a) 
    return lista 

#ejercicio5
def filtrar_pares(lista):   
    return list(filter((lambda x: x % 2 == 0), lista))

#ejercicio6
def frecuencia(cadena):
    limpiar = "\n"
    for caracter in limpiar:
        cadena = cadena.replace(caracter," ")    
    palabras = cadena.split(" ")
    #La función -split- se usó para separar la cadena en partes
    diccionario_frecuencias = {}
    #Se usó la estructura de -diccionario- para guardar las frecuencias
    for palabra in palabras:
        if palabra in diccionario_frecuencias:
            diccionario_frecuencias[palabra] += 1
        else:
            diccionario_frecuencias[palabra] = 1
    lista = []
    for palabra in diccionario_frecuencias:
        frecuencia = diccionario_frecuencias[palabra]
        lista.append((f'{palabra}',frecuencia))
    return lista

#ejercicio7
def suma_digitos(num):
    suma = 0
    while (num > 0 or suma > 9):
        if num == 0:
            num = suma
            suma = 0
        suma = suma + num % 10
        num = num // 10
    return suma

#ejercicio8
def reemplaza_espacios(cadena): 
    cadena1 = ""
    cadena2 = ""
    cadena_suma = cadena.replace(' ','+')
    for i in range(len(cadena_suma)):
        if cadena_suma[i] == '+':
           cadena2 = cadena_suma[i] + cadena2
    cadena_suma = cadena_suma.replace('+',"")
    cadena1 = cadena2 + cadena_suma
    return cadena1

#ejercicio9
def dibuja_triangulo(n):
    cadena = ""
    a = 0
    while a < n:
        for i in range(1, a + 2):
            espacios = n - i 
            final = ' ' * espacios + '* ' * i 
            cadena += final + "\n"
        cadena += "\n"
        a += 1 
    return(cadena)
    
#ejercicio10
def pascal(n):
    lista = []
    cadena = ""
    a = 0
    for x in range(n):
        lista.append([])
    for x in range(n):
        for y in range(x + 1):
            if y == 0 or y == x:
                lista[x].append(1)
            else:
                a = (lista[x - 1][y]+lista[x - 1][y - 1])
                lista[x].append(a)
        cadena2 = str(lista[x])
        #Se usó -str- para convertir los valores de tipo int a string y poderlos concatenar
        cadena2 = cadena2.replace(",","")
        cadena = cadena + cadena2 + "\n"
    return cadena