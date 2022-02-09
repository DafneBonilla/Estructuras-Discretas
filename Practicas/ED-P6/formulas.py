import pathlib
from typing import List
from itertools import product

Asignacion = List[bool]

class Formula:
    """
    Clase para representar fórmulas booleanas.
    """
    def __init__(self, izquierda, conectivo = None, derecha = None):
        """
        Constructor para la clase. En el caso de las variables,
        izquierda es el identificador de la variable, debe ser
        un entero, y conectivo y derecha deben ser None. El atributo
        conectivo debe ser un string, 'C'(onjunción), 'D'(isyunción),
        'I'(mplicación), 'N'(egación) o 'B'(icondicional). Para
        cualquier fórmula que no sea una variable, el atributo
        izquierda debe ser una fórmula, y para las fórmulas con
        conectivo distinto a 'N', el atributo derecho también tiene
        que ser una fórmula.
        """
        conectivos=['C','D','I','B','N']
        if (conectivo == None
                and not (isinstance(izquierda, int) and izquierda > -1)):
            raise TypeError("Las variables deben ser naturales")
        elif conectivo != None:
            if not isinstance(izquierda, Formula):
                raise TypeError("Los conectivos deben aplicarse a fórmulas")
            elif (conectivo == 'N' and derecha != None):
                raise TypeError("En la negación no debe existir fórmula derecha")
            elif (conectivo not in conectivos):
                raise ValueError("El conectivo es incorrecto")
            elif (conectivo != 'N' and not isinstance(derecha, Formula)):
                raise TypeError("Los conectivos deben aplicarse a fórmulas")
        self.izquierda = izquierda
        self.conectivo = conectivo
        self.derecha   = derecha

    def __repr__(self):
        """
        Representación en cadena, legible para humanos, de
        las fórmulas.
        """
        if self.conectivo == None:
            var = 'x{}'.format(repr(self.izquierda))
            return var
        elif self.conectivo == "N":
            negacion = "(¬{0})".format(repr(self.izquierda))
            return negacion
        else:
            binaria = "({0} {1} {2})".format(repr(self.izquierda), '{0}', repr(self.derecha))
            if self.conectivo == "C":
                binaria = binaria.format('∧')
            elif self.conectivo == "D":
                binaria = binaria.format('∨')
            elif self.conectivo == "I":
                binaria = binaria.format('→')
            else:
                binaria = binaria.format('↔')
            return binaria 

    def lista_variables(self):
        """
        Devuelve la lista de todas las variables que ocurren
        en una fórmula, en orden.
        """
        if self.conectivo == None:
            listita = []
            listita.append(self.izquierda)
            return listita
        if self.conectivo == "N":
            listita = self.izquierda.lista_variables()
        else: 
            listita = self.izquierda.lista_variables() + self.derecha.lista_variables()
            
        #Se usó sorted para ordenar los elementos de la lista y set para eliminar repetidos
        return sorted(list(set(listita)))

    def ultima_variable(self):
        """
        Devuelve la última variable que ocurre en una fórmula.
        """
        listita = self.lista_variables()
        return listita[len(listita)-1]

    def numero_conectivos(self):
        """
        Devuelve el número de conectivos que ocurren en la fórmula.
        """
        if self.conectivo == None:
            return 0
        if self.conectivo == 'N':
            return 1 + self.izquierda.numero_conectivos()
        else:
            return 1 + self.izquierda.numero_conectivos() + self.derecha.numero_conectivos() 
       
    def _evalua_aux(self, asignacion: Asignacion, posiciones: List[int]):
        """
        Función auxiliar para evaluar una fórmula. Recibe una lista de
        booleanos (una asignación de verdad), y una lista con las posiciones
        en las que ocurren las variables de la fórmula.
        """
        if len(asignacion) < len(posiciones):
            raise ValueError("La asignacion no cubre todas las variables")
        if self.conectivo == None:
            valor = asignacion[posiciones.index(self.izquierda)]
        else:
            if self.conectivo == 'N':
                valor = 1 - self.izquierda._evalua_aux(asignacion, posiciones)
            elif self.conectivo == 'C':
                valor = min(self.izquierda._evalua_aux(asignacion, posiciones), self.derecha._evalua_aux(asignacion, posiciones))
            elif self.conectivo == 'D':
                valor = max(self.izquierda._evalua_aux(asignacion, posiciones), self.derecha._evalua_aux(asignacion, posiciones))
            elif self.conectivo == 'I':
                if (self.izquierda._evalua_aux(asignacion, posiciones)) and not self.derecha._evalua_aux(asignacion, posiciones):
                    valor = 0
                else:
                    valor = 1
            else:
                valor = min(max(1-self.izquierda._evalua_aux(asignacion, posiciones), self.derecha._evalua_aux(asignacion, posiciones)), max(self.izquierda._evalua_aux(asignacion, posiciones), 1-self.derecha._evalua_aux(asignacion, posiciones)))
        return valor   

    def evalua(self, asignacion: Asignacion):
        """
        Devuelve el valor de verdad de la fórmula bajo una
        asignación dada, que recibe como entrada en la forma
        de una lista de booleanos.
        """
        posiciones = self.lista_variables()
        return self._evalua_aux(asignacion, posiciones)

    def aplana(self):
        """
        Devuelve una lista con la versión aplanada del árbol
        de sintáxis de la fórmula.
        """
        if self.conectivo == None:
            return [self]
        if self.conectivo == "N":    
            listita = []
            listita += self.izquierda.aplana() + [self] 
            return listita
        listita = []
        listita += self.izquierda.aplana() + [self] + self.derecha.aplana()
        return listita

    def aplana_sin_variables(self):
        """
        Devuelve una lista con la versión aplananada del
        árbol de sintaxis de la fórmula, sin las hojas.
        """
        if self.conectivo == None:
            return []
        if self.conectivo == "N":    
            listita = []
            listita += self.izquierda.aplana_sin_variables() + [repr(self)] 
            return listita
        listita = []
        listita += self.izquierda.aplana_sin_variables() + [repr(self)] + self.derecha.aplana_sin_variables()
        return listita