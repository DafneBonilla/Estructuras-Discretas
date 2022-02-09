import unittest
import random
from arboles import *

class TestArbol(unittest.TestCase):

    def test_constructor_arbol(self):
        """
        Prueba que el constructor de árboles sea correcto.
        """
        # El izquierdo debe ser árbol
        with self.assertRaises(TypeError):
            Arbol(1, 2, Arbol())
        # El derecho debe ser árbol
        with self.assertRaises(TypeError):
            Arbol(1, Arbol(), 2)
        # Constructor vacío
        a = Arbol()
        self.assertEqual(a.raiz, None)
        self.assertEqual(a.izquierdo, None)
        self.assertEqual(a.derecho, None)
        # Constructor con izquierdo y derecho
        a = Arbol(1, Arbol(2), Arbol(3))
        self.assertEqual(a.raiz, 1)
        self.assertEqual(a.izquierdo.raiz, 2)
        self.assertEqual(a.derecho.raiz, 3)

    def test_repr_arbol(self):
        """
        Prueba que la representación de árbol como cadena sea correcta.
        """
        # Árbol vacío
        a = Arbol()
        self.assertEqual(str(a), "ø")
        a = Arbol(2)
        c = "(" + str(a.raiz) + "\n  "
        c += "ø" + "\n  "
        c += "ø" + ")"        
        self.assertEqual(str(a), c)
        a = Arbol('a', Arbol('b', Arbol('c'), Arbol('d')), Arbol('e'))
        c = "(a\n  (b\n    (c\n      ø\n      ø)\n    (d\n      ø\n      ø))\n  (e\n    ø\n    ø))"
        self.assertEqual(str(a), c)

    def test_es_vacio(self):
        """
        Prueba que la función es_vacio funcione correctamente. 
        """
        a = Arbol()
        self.assertTrue(a.es_vacio())
        a = Arbol(1)
        self.assertFalse(a.es_vacio())

    def test_es_hoja(self):
        """
        Prueba que la función es_hoja funcione correctamente. 
        """
        a = Arbol()
        self.assertFalse(a.es_hoja())
        a = Arbol(1)
        self.assertTrue(a.es_hoja())
        a = Arbol(1, Arbol(2), None)
        self.assertFalse(a.es_hoja())

    def test_copia(self):
        """
        Prueba que la función copia funcione correctamente.
        """
        a = Arbol()
        b = a.copia()
        self.assertIsNot(a, b)
        self.assertEqual(a, b)
        a = Arbol(random.randint(0, 100))
        b = a.copia()
        self.assertIsNot(a, b)
        self.assertEqual(a, b)
        e = []
        for i in range(6):
            e.append(random.randint(0, 100))
        a = Arbol(e[0], Arbol(e[1], Arbol(e[2]), Arbol(e[3])), Arbol(e[4], Arbol(e[5]), None))
        b = a.copia()
        self.assertIsNot(a, b)
        self.assertEqual(a, b)
        self.assertIsNot(a.izquierdo, b.izquierdo)
        self.assertIsNot(a.derecho, b.derecho)

    def test_num_nodos(self):
        """
        Prueba que la función num_nodos funcione correctamente.
        """
        a = Arbol()
        self.assertEqual(a.num_nodos(), 0)
        a = Arbol(random.randint(0, 100))
        self.assertEqual(a.num_nodos(), 1)
        e = []
        for i in range(6):
            e.append(random.randint(0, 100))
        a = Arbol(e[0], Arbol(e[1], Arbol(e[2]), Arbol(e[3])), Arbol(e[4], Arbol(e[5]), None))
        self.assertEqual(a.num_nodos(), 6)
        
    def test_direccion(self):
        """
        Prueba que la función direccion funcione correctamente. 
        """
        elemento = 42
        arbol = Arbol()
        # Árbol vacío no contiene a nadie.
        self.assertFalse(arbol.direccion(elemento))
        izquierdo = Arbol(32, Arbol(10), Arbol(2))
        derecho = Arbol(5, Arbol(3), Arbol(21))
        arbol = Arbol(16, izquierdo, derecho)
        # El elemento no está contenido
        self.assertFalse(arbol.direccion(elemento))
        izquierdo.raiz = 42
        # El elemento está en la posición 0
        self.assertEqual(arbol.direccion(elemento), "0")
        izquierdo.raiz = 32
        derecho.izquierdo.raiz = 42
        # El elemento está en la posición 10
        self.assertEqual(arbol.direccion(elemento), "10")


    def test_gira(self):
        """
        Prueba que la función gira funcione correctamente. 
        """
        a = Arbol()
        b = a.gira("")
        self.assertIsNot(a, b)
        self.assertEqual(a, b)
        a = Arbol("hola")
        b = a.gira("")
        self.assertIsNot(a, b)
        self.assertEqual(a, b)
        izquierdo = Arbol(32, Arbol(10), Arbol(2))
        derecho = Arbol(5, Arbol(3), Arbol(21))
        a = Arbol(16, izquierdo, derecho)
        b = a.gira("")
        c = Arbol(16, derecho.copia(), izquierdo.copia())
        self.assertIsNot(b, c)
        self.assertEqual(b, c)
        b = a.gira("0")
        c = Arbol(16, Arbol(izquierdo.raiz, izquierdo.derecho.copia(), izquierdo.izquierdo.copia()), derecho.copia())
        self.assertIsNot(b, c)
        self.assertEqual(b, c)
        b = a.gira("1")
        c = Arbol(16, izquierdo.copia(), Arbol(derecho.raiz, derecho.derecho.copia(), derecho.izquierdo.copia()))
        self.assertIsNot(b, c)
        self.assertEqual(b, c)
        
    def test_es_isomorfo(self):
        """
        Prueba que la función es_isomorfo funcione correctamente. 
        """
        a = Arbol()
        b = Arbol()
        self.assertTrue(a.es_isomorfo(b))
        x = random.randint(0, 100)
        a = Arbol(x)
        b = Arbol(x)
        self.assertTrue(a.es_isomorfo(b))
        e = []
        for i in range(6):
            e.append(random.randint(0, 100))
        a = Arbol(e[0], Arbol(e[1]), Arbol(e[2]))
        b = Arbol(e[0], Arbol(e[1]), Arbol(e[2]))
        c = Arbol(e[0], Arbol(e[2]), Arbol(e[1]))
        self.assertTrue(a.es_isomorfo(b))
        self.assertTrue(c.es_isomorfo(b))
        self.assertTrue(a.es_isomorfo(a))
        a = Arbol(e[0], Arbol(e[1], Arbol(e[2]), Arbol(e[3])), Arbol(e[4], Arbol(e[5]), None))
        b = Arbol(e[0], Arbol(e[4], Arbol(e[5]), None), Arbol(e[1], Arbol(e[2]), Arbol(e[3])))
        c = Arbol(e[0], Arbol(e[1], Arbol(e[2]), Arbol(e[3])), Arbol(e[4], None, Arbol(e[5])))
        d = Arbol(e[0], Arbol(e[1], Arbol(e[3]), Arbol(e[2])), Arbol(e[4], None, Arbol(e[5])))
        self.assertTrue(a.es_isomorfo(b))
        self.assertTrue(c.es_isomorfo(b))
        self.assertTrue(a.es_isomorfo(a))
        self.assertTrue(a.es_isomorfo(d))
        self.assertTrue(c.es_isomorfo(d))
        self.assertTrue(b.es_isomorfo(d))
        c = a.copia()
        self.assertTrue(a.es_isomorfo(c))
        self.assertTrue(a.es_isomorfo(a))
        
    def test_eq_arbol(self):
        """
        Prueba que la función eq funcione correctamente en árboles. 
        """
        a = Arbol()
        b = Arbol()
        self.assertEqual(a, b)
        x = random.randint(0, 100)
        a = Arbol(x)
        b = Arbol(x)
        self.assertEqual(a, b)
        e = []
        for i in range(6):
            e.append(random.randint(0, 100))
        a = Arbol(e[0], Arbol(e[1]), Arbol(e[2]))
        b = Arbol(e[0], Arbol(e[1]), Arbol(e[2]))
        self.assertEqual(a, b)
        a = Arbol(e[0], Arbol(e[1], Arbol(e[2]), Arbol(e[3])), Arbol(e[4], Arbol(e[5]), None))
        b = Arbol(e[0], Arbol(e[1], Arbol(e[2]), Arbol(e[3])), Arbol(e[4], Arbol(e[5]), None))
        self.assertEqual(a, b)
        c = a.copia()
        self.assertEqual(a, c)
        self.assertEqual(a, a)
        
