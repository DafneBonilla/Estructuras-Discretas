from ast import For
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

#-----------------------------FUNCIONES PRÁCTICA 1------------------------------
    def __repr__(self):
        """
        Representación en cadena, legible para humanos, de
        las fórmulas.
        """
        if self.conectivo == None:
            var = 'x{}'.format(repr(self.izquierda))
            return var
        elif self.conectivo == 'N':
            neg = "(¬{0})".format(repr(self.izquierda))
            return neg
        else:
            bin = "({0} {1} {2})".format(repr(self.izquierda),'{0}',repr(self.derecha))
            if self.conectivo == 'C':
                bin = bin.format('∧')
            elif self.conectivo == 'D':
                bin = bin.format('∨')
            elif self.conectivo == 'I':
                bin = bin.format('→')
            else:
                bin = bin.format('↔')
            return bin

    def lista_variables(self):
        """
        Devuelve la lista de todas las variables que ocurren
        en una fórmula, en orden.
        """
        if self.conectivo == None:
            listita = []
            listita.append(self.izquierda)
            return listita
        elif self.conectivo == 'N':
            listita = self.izquierda.lista_variables()
        else:
            listita = self.izquierda.lista_variables() + self.derecha.lista_variables()
        #Se usó sorted para ordenar los elementos de la lista y set para eliminar repetidos
        listita = list(set(listita))
        return sorted(listita)

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
        if self.conectivo == 'N':
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
        if self.conectivo == 'N':
            listita = []
            listita += self.izquierda.aplana_sin_variables() + [self]
            return listita
        listita = []
        listita += self.izquierda.aplana_sin_variables() + [self] + self.derecha.aplana_sin_variables()
        return listita

#-----------------------------FUNCIONES PRÁCTICA 2------------------------------
    def _evalua_sub_aux(self,
                        asignacion: Asignacion,
                        posiciones: List[int],
                        partes,
                        resultado):
        """
        Función auxiliar para evaluar a la fórmula y todas sus
        subfórmulas. Recibe como entrada una lista de booleanos
        (asignación de verdad), una lista con las posiciones en
        las que ocurren las variables, y una lista de las subfórmulas
        de la fórmula.   Este método devuelve un diccionario que asocia
        a cada subfórmula su valor de verdad bajo la asignación.
        """
        if len(asignacion) < len(posiciones):
            raise ValueError("La asignacion no cubre a todas las variables")
        if self.conectivo == None:
            resultado[self] = asignacion[posiciones.index(self.izquierda)]
        else:
            self.izquierda._evalua_sub_aux(asignacion, posiciones, 0, resultado)
            if self.conectivo == 'N':
                resultado[self] = 1 - resultado[self.izquierda]
            else:
                self.derecha._evalua_sub_aux(asignacion, posiciones, 0, resultado)
                if self.conectivo == 'C':
                    resultado[self] = min(resultado[self.izquierda], resultado[self.derecha])
                elif self.conectivo == 'D':
                    resultado[self] = max(resultado[self.izquierda], resultado[self.derecha])
                elif self.conectivo == 'I':
                    if (resultado[self.izquierda] and not resultado[self.derecha]):
                        resultado[self] = 0
                    else:
                        resultado[self] = 1
                else:
                    resultado[self] = min(max(1-resultado[self.izquierda], resultado[self.derecha]), max(resultado[self.izquierda], 1-resultado[self.derecha]))
        return resultado

    def evalua_sub(self, asignacion):
        """
        Recibe como entrada una lista de booleanos (asignación de verdad)
        y devuelve una lista de booleanos; las entradas de esta lista de
        booleanos corresponden con las posiciones de la lista de
        subfórmulas que genera la función aplana.   La finalidad de esta
        función es generar los renglones de la tabla de verdad de esta
        fórmula.   Sólo la primera ocurrencia está evaluada en la lista.
        """
        resultado = {}
        return self._evalua_sub_aux(asignacion, self.lista_variables(), 0, resultado)

    def renglones_verdad(self):
        """
        Devuelve una lista con los renglones de la tabla de verdad de
        la fórmula.   Por diseño, los valores de las variables sólo
        ocurren en las primeras columnas de la tabla de verdad.
        """
        renglones = []
        asignaciones = product([0,1], repeat= len(self.lista_variables()))
        for asignacion in asignaciones:
            renglones = list(asignacion)
            renglones.extend(self.evalua_sub(renglones))
            renglones.append(renglones)
        return renglones

    def tex_tabla(self):
        """
        Devuelve la fórmula con los separadores necesarios
        para crear la tabla en LaTeX.
        """
        if self.conectivo == None:
            cadenita = f"x_{{{repr(self.izquierda)}}}"
            return cadenita
        elif self.conectivo == 'N':
            cadenita2 = f"( & \lnot & {self.izquierda.tex_tabla()})"
            return cadenita2
        else:
            if self.conectivo == 'C':
                return f"({self.izquierda.tex_tabla()} & \land & {self.derecha.tex_tabla()})"
            elif self.conectivo == 'D':
                return f"({self.izquierda.tex_tabla()} & \lor & {self.derecha.tex_tabla()})"
            elif self.conectivo == 'I':
                return f"({self.izquierda.tex_tabla()} & \\to & {self.derecha.tex_tabla()})"
            else:
                return f"({self.izquierda.tex_tabla()} & \leftrightarrow & {self.derecha.tex_tabla()})"

    def _cabecera_tabla(self):
        """
        Devuelve la cabecera de la tabla de verdad en formato
        de tabla de LaTeX.
        """
        linea = "  "
        for formula in self.lista_variables():
            linea = linea + Formula(formula).tex_tabla() + " & "
        linea = linea + self.tex_tabla() + " \\\\\n"
        return linea

    def _renglon_verdad(self,
                   asignacion):
        """
        Devuelve un renglón de la tabla de verdad de la fórmula,
        en formato de tabla de LaTeX, correspondiente a la
        asignación de verdad recibida.
        """
        renglon = "  "
        evaluacion = self.evalua_sub(asignacion)
        for valor in asignacion:
            renglon += f"{valor} & "
        for subformula in self.aplana_sin_variables():
            if self == subformula:
                renglon += f"& \\mathbf{{{evaluacion[subformula]}}} & "
            else:
                renglon += f"& {evaluacion[subformula]} & "
        renglon += "\\\\\n"
        return renglon

    def tabla_verdad(self):
        """
        Devuelve la tabla de verdad de la fórmula en formato
        LaTeX.
        """
        numerito = len(self.lista_variables())
        numerito2 = pow(2,numerito)-1
        asignaciones = product([1,0], repeat=numerito)
        tablita = ""
        tablita += "\\begin{adjustbox}{max width=\\textwidth,array="+self.num_c(numerito)+"|"+self.num_c2()+"} \\\\\n"
        tablita += self._cabecera_tabla()
        tablita += "\\hline\n"
        for asig in asignaciones:
            tablita += self._renglon_verdad(asig)
        tablita += "\\end{adjustbox}\n"
        return tablita
    
    def num_c(self, numero):
        cadenita = ""
        for i in range(numero):
            cadenita += "c"
        return cadenita

    def num_c2(self):
        cadenita = ""
        for formula in self.aplana_sin_variables():
            if formula.conectivo == "N":
                cadenita += "c@{}c"
            else:
                cadenita += "cc"
        return cadenita + "c"

    def LaTeX(self, nombre_archivo):
        """
        Crea un archivo con nombre nombre_archivo.tex, que es un
        archivo mínimo en LaTeX para poder compilar la tabla de
        verdad asociada a la fórmula.
        """
        nombre = f"{nombre_archivo}/{nombre_archivo}.tex"
        pathlib.Path(f"{nombre_archivo}/").mkdir(parents= True, exist_ok=True)
        arch = open(nombre, "w+")
        arch.write("\\documentclass{article}\n\n")
        arch.write("\\usepackage{adjustbox}\n\n")
        arch.write("\\begin{document}\n\n")
        arch.write("\\[\n")
        arch.write(self.tabla_verdad())
        arch.write("\\]\n\n")
        arch.write("\\end{document}")
        arch.close()
