from typing import List

class Lista:
    """
    Clase para representar listas recursivas.
    """
    def __init__(self,elementos=None):
        """
        Constructor de la clase. Si elementos es None, construye una Lista
        vacía, en otro caso, asigna el primer elemento como la cabeza de la
        Lista y llama recursivamente el constructor para construir la cola de
        la lista utilizando el resto de elementos.
        """
        if elementos != None:
            if not isinstance(elementos,List):
                raise TypeError("Debe recibir una lista de elementos")
            elif len(elementos) == 1:
                self.cabeza = elementos[0]
                self.cola = Lista()
            else:
                self.cabeza = elementos[0]
                self.cola = Lista(elementos[1:])
        else:
            self.cabeza = None
            self.cola = None

    def __repr__(self):
        resultado = ""
        if self.cabeza == None:
            resultado = "()"
        else:
            resultado = "({0} {1})".format(repr(self.cabeza), repr(self.cola))
        return resultado

    def agrega_principio(self, elemento):
        if self.cabeza == None:
            self.cabeza = elemento
            self.cola = Lista()
        else:
            aux = self.cabeza
            self.cabeza = elemento
            self.cola.agrega_principio(aux)

    def agrega_final(self,elemento):
        if self.cabeza == None:
            self.cabeza = elemento
            self.cola = Lista()
        else:
            listita = self.reversa()
            listita.agrega_principio(elemento)
            listita = listita.reversa()
            self.cabeza = listita.copia().cabeza
            self.cola = listita.copia().cola

    def longitud(self):
        if self.cabeza == None:
            return 0
        return 1 + self.cola.longitud()

    def contiene(self,elemento):
        if self.cabeza == None:
            return False
        if self.cabeza == elemento:
            return True
        return self.cola.contiene(elemento)

    def copia(self):
        listita = self.reversa().reversa()
        return listita

    def concatena(self, lista):
        if not isinstance(lista,Lista):
            raise TypeError("No es una lista")
        elif lista.cabeza == None:
            return self.copia()
        elif self.cabeza == None:
            return lista.copia()
        else:
            listita = Lista([self.cabeza])
            if self.cola.cabeza == None:
                listita.cola = lista.copia()
            else:
                listita.cola = self.cola.concatena(lista)
            return listita

    def reversa(self):
        listita = Lista()
        listita = self.rev_auxi(listita)
        return listita

    def rev_auxi(self,listita):
        if self.cabeza == None:
            return listita
        listita.agrega_principio(self.cabeza)
        return self.cola.rev_auxi(listita)

    def mapea(self,f):
        if f == None:
            return self
        if self.cabeza == None:
            return Lista()
        listota = self.copia()
        listitita = Lista().map_aux(listota, f)
        return listitita

    def map_aux(self, original, f):
        if original.cabeza == None:
            return self
        elemento = f(original.cabeza)
        self.agrega_final(elemento)
        return self.map_aux(original.cola, f)

    def filtra(self,f):
        if f == None:
            return self
        if self.cabeza == None:
            return Lista()
        listota = self.copia()
        listitita = Lista().fil_aux(listota, f)
        self.cabeza = listitita.cabeza
        self.cola = listitita.cola
        return self.copia()

    def fil_aux(self, original, f):
        if original.cabeza == None:
            return self
        if f(original.cabeza) == True:
            self.agrega_final(original.cabeza)
        return self.fil_aux(original.cola, f)

    def __eq__(self, lista):
        """
        Compara dos listas y devuelve si son iguales.
        """
        if not isinstance(lista,Lista):
            return False
        if self.longitud() != lista.longitud():
            return False
        elif self.cabeza == lista.cabeza:
            return self.cola == lista.cola
        else:
            return False
