class Arbol:
    """
    Clase para representar árboles binarios recursivos. La variable 'raiz' es un
    elemento, 'izquierdo' es un árbol y 'derecho' es un árbol.
    """

    def __init__(self, raiz=None, izquierdo=None, derecho=None):
        """
        Constructor de la clase. Si raiz es None construye un árbol binario
        vacío, en otro caso, asigna a raiz como raíz del árbol, a izquierdo
        como subárbol izquierdo, y a derecho como subárbol derecho.
        """
        if raiz is None:
            self.raiz = self.izquierdo = self.derecho = None
        else:
            self.raiz = raiz
            if izquierdo is None:
                self.izquierdo = Arbol()
            elif not isinstance(izquierdo, Arbol):
                raise TypeError("¡El subárbol izquierdo debe ser árbol!")
            else:
                self.izquierdo = izquierdo
            if derecho is None:
                self.derecho = Arbol()
            elif not isinstance(derecho, Arbol):
                    raise TypeError("¡El subárbol derecho debe ser árbol!")
            else:
                self.derecho = derecho


    def __repr__(self):
        return self.auxi("")

    def auxi(self, tabulador):
        """
        Metodo auxiliar para poner espacios en repr
        """
        tab = "  " + tabulador
        if self.raiz is None:
            return "ø"
        else:
            return "({0}\n{3}{1}\n{3}{2})".format(self.raiz, self.izquierdo.auxi(tab), self.derecho.auxi(tab), tab)


    def es_vacio(self):
        if self.raiz is None:
            return True
        return False


    def es_hoja(self):
        if self.raiz is None:
            return False
        if self.izquierdo.es_vacio() and self.derecho.es_vacio():
            return True
        return False


    def copia(self):
        if self.es_vacio():
            return Arbol()
        else:
            copiadito = Arbol(self.raiz)
            copiadito.izquierdo = self.izquierdo.copia()
            copiadito.derecho = self.derecho.copia()
            return copiadito


    def num_nodos(self):
        if self.raiz is None:
            return 0
        return self.izquierdo.num_nodos() + self.derecho.num_nodos() + 1


    def direccion(self, elemento):
        direccioncita = ""
        if self.es_vacio():
            return False
        if self.es_hoja():
            if self.raiz == elemento:
                return direccioncita
            else:
                return False
        if isinstance(self.izquierdo.direccion(elemento), str):
            direccioncita += "0"
            direccioncita += self.izquierdo.direccion(elemento)
            return direccioncita
        if self.raiz == elemento:
            return direccioncita
        if isinstance(self.derecho.direccion(elemento), str):
            direccioncita += "1"
            direccioncita += self.derecho.direccion(elemento)
            return direccioncita
        else:
            return False


    def gira(self, direccion):
        if not isinstance(direccion, str):
            raise TypeError("Direccion mala")
        if self.raiz is None or self.es_hoja():
            return self.copia()
        nuevo = Arbol(self.raiz)
        if direccion == "":
            nuevo.izquierdo = self.derecho.copia()
            nuevo.derecho = self.izquierdo.copia() 
        else:
            if direccion[0] == "0":
                nuevo.izquierdo = self.izquierdo.gira(direccion[1:]) 
                nuevo.derecho = self.derecho.copia()
            elif direccion[0] == "1":
                nuevo.izquierdo = self.izquierdo.copia()
                nuevo.derecho = self.derecho.gira(direccion[1:]) 
        return nuevo


    def es_isomorfo(self, arbol):
        if not isinstance(arbol, Arbol):
            return False
        if self.__eq__(arbol):
            return True
        else:
            girando = arbol.gira("")
            return self.izquierdo.es_isomorfo(girando.izquierdo) or self.derecho.es_isomorfo(girando.izquierdo)


    def __eq__(self, arbol):
        if not isinstance(arbol, Arbol):
            return False
        if self.num_nodos() != arbol.num_nodos():
            return False
        if self.raiz == arbol.raiz:
            return self.izquierdo.__eq__(arbol.izquierdo) and self.derecho.__eq__(arbol.derecho)
        else:
            return False