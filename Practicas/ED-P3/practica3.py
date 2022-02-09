def encripta_cadena(s):
    """
        Devuelve la cadena de acuerdo a las reglas escritas.
    """
    if len(s) == 1 or s == "":
        return s
    index = len(s) // 2
    if len(s) % 2 == 0:
        index -= 1
    return s[index] + encripta_cadena(s[:index]) + encripta_cadena(s[index+1:])

def es_primo(n):
    """
        Regresa verdadero si el número n es primo
    """ 
    #Función auxiliar: Se realizó para tener un índice que divida al número y nos 
    #ayude a comprobar que el número solo es divisible entre si mismo o la unidad.
    def auxiliar(n, i):
        if n <= 1:
            return False
        if i * i > n :
            return True
        if n % i == 0:
            return False
        return auxiliar(n, i + 1)
    return auxiliar(n, 2)

def decimal_binario(n):
    """
    Regresa la conversión de un número decimal n a binario
    """   
    if n == 0:
        return 0    
    binario = decimal_binario(n // 2)
    return n % 2 + 10 * binario

def suma_triangulo(lista): #Primero hacer el suma consecutivos 
    """
    Regresa una lista de listas, donde la última es la lista original y representa
    el primer nivel. En los siguientes niveles se tiene una lista que tiene por
    elementos la suma de cada par de elementos consecutivos en el nivel anterior
    Hint: Utilizar suma_consecutivos
    """
    if len(lista) == 0 or len(lista) == 1:
        return [lista]
    return suma_triangulo(suma_consecutivos(lista)) + [lista]

def suma_consecutivos(lista):
    """
    Regresa una lista con la suma de dos elementos consecutivos de la lista
    original
    """
    if len(lista) == 0 or len(lista) == 1:
        return lista
    if len(lista) == 2:
        return [lista[0]+lista[1]]
    return [lista[0]+lista[1]] + suma_consecutivos(lista[1:])

def suma_potencias(numero, potencia):
    """
        Regresa la suma de los dígitos elevados a la potencia dada.
    """
    if potencia == 0:
        return 1
    if potencia == 1:
        return numero
    if numero < 9: 
        return numero ** potencia
    return ((numero % 10)**potencia + suma_potencias((numero//10), potencia))
    
def oculta_caracter(caracter, veces):
    """
        Regresa la cadena con tantos paréntesis como veces se pidió ocultar
        el caracter.
    """
    if veces == 0:
        return caracter
    return "(" * veces + caracter + ")" * veces

def numero_de_formas(n):
    """
        Regresa la cantidad de formas diferentes en la que una
        persona puede subir los escalones, tomando en cuenta que
        solo puede dar saltos de uno en uno, de dos en dos y de tres en tres.
    """   
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return numero_de_formas(n-1) + numero_de_formas(n-2) + numero_de_formas(n-3)
    
def consonante_a_f(cadena):
    """
    Regresa la cadena con todas las consonantes reemplazadas por f.
    """
    lista = list(cadena)
    if cadena == "": 
        return cadena
    if lista[0] not in "aeiouAEIOU" and lista[0] != " ": 
        return "f" + consonante_a_f("".join(lista[1:]))
    if lista[0] == "": 
        return  consonante_a_f("".join(lista[1:])) + " "
    return lista[0] + consonante_a_f("".join(lista[1:]))