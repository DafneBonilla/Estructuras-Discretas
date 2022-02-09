import unittest
import random
from listas import *


class TestLista(unittest.TestCase):
    def test_constructor_lista(self):
        """
        Prueba que el constructor de la lista sea correcto
        """
        vacia = Lista()
        elems = [random.randint(0,100) for i in range(5)]
        lista = Lista(elems)

        self.assertEqual(vacia.cabeza , None)
        self.assertEqual(vacia.cola , None)
        self.assertEqual(lista.cabeza , elems[0])
        self.assertEqual(lista.cola.cabeza , elems[1])
        self.assertEqual(lista.cola.cola.cabeza , elems[2])
        self.assertEqual(lista.cola.cola.cola.cabeza , elems[3])
        self.assertEqual(lista.cola.cola.cola.cola.cabeza , elems[4])

        
    def test_repr(self):
        """
        Prueba que __repr__ funcione para las Listas
        """
        vacia = Lista()
        elems = [random.randint(0,100) for i in range(5)]
        lista = Lista(elems)
        s = "({0} ({1} ({2} ({3} ({4} ())))))".format(elems[0],elems[1],elems[2],elems[3],elems[4])

        self.assertEqual(repr(vacia),"()")
        self.assertEqual(repr(lista),s)

        
    def test_agrega_principio(self):
        """
        Prueba que la función agrega_principio funcione correctamente.
        """
        vacia = Lista()
        elems1 = [random.randint(0,100) for i in range(5)]
        l1 = Lista(elems1)
        n = random.randint(0,100)
        l2 = Lista([n]+elems1)

        vacia.agrega_principio(n)
        l1.agrega_principio(n)
        self.assertEqual(vacia,Lista([n]))
        self.assertEqual(l1,l2)

        
    def test_agrega_final(self):
        """
        Prueba que la función agrega_final funcione correctamente.
        """
        vacia = Lista()
        elems1 = [random.randint(0,100) for i in range(5)]
        l1 = Lista(elems1)
        n = random.randint(0,100)
        l2 = Lista(elems1+[n])

        vacia.agrega_final(n)
        l1.agrega_final(n)
        self.assertEqual(vacia,Lista([n]))
        self.assertEqual(l1,l2)

        
    def test_longitud(self):
        """
        Prueba que la función longitud funcione correctamente.
        """
        vacia = Lista()
        n = random.randint(1,100)
        elems = [i for i in range(n)]
        lista = Lista(elems)

        self.assertEqual(vacia.longitud() , 0)
        self.assertEqual(lista.longitud() , n)

        
    def test_contiene(self):
        """
        Prueba que la función contiene funcione correctamente.
        """
        vacia = Lista()
        n = random.randint(1,100)
        m = random.randint(1,n)
        k = n+3
        elems = [i for i in range(n)]
        lista = Lista(elems)

        self.assertEqual(vacia.contiene(n),False)
        self.assertEqual(vacia.contiene(m),False)
        self.assertEqual(vacia.contiene(k),False)
        self.assertEqual(lista.contiene(m),True)
        self.assertEqual(vacia.contiene(k),False)

        
    def test_copia(self):
        """
        Prueba que la función copia funcione correctamente.
        """
        vacia = Lista()
        rl = random.sample(range(100), random.randint(1, 100))
        l = Lista(rl)
        
        self.assertEqual(vacia, vacia.copia())
        self.assertIsNot(vacia, vacia.copia())
        self.assertEqual(l, l.copia())
        self.assertIsNot(l, l.copia())

        
    def test_concatena(self):
        """
        Prueba que la función concatena funcione correctamente.
        """
        vacia = Lista()
        n = random.randint(0,100)
        m = random.randint(0,100)
        elems1 = [i for i in range(n)]
        elems2 = [i for i in range(m)]
        l1 = Lista(elems1)
        l2 = Lista(elems2)
        l3 = Lista(elems1+elems2)
        l4 = Lista(elems2+elems1)

        self.assertEqual(vacia.concatena(vacia),vacia)
        self.assertIsNot(vacia.concatena(vacia),vacia)
        self.assertEqual(l1.concatena(vacia),l1)
        self.assertIsNot(l1.concatena(vacia),l1)
        self.assertEqual(l1.concatena(l2),l3)
        self.assertEqual(l2.concatena(l1),l4)
        
        
    def test_reversa(self):
        """
        Prueba que la función reversa funcione correctamente.
        """
        vacia = Lista()
        elems1 = [random.randint(0,100) for i in range(5)]
        elems2 = elems1.copy()
        elems2.reverse()
        l1 = Lista(elems1)
        l2 = Lista(elems2)

        self.assertEqual(vacia.reversa(),vacia)
        self.assertIsNot(vacia.reversa(),vacia)
        self.assertEqual(l1.reversa(),l2)
        self.assertEqual(l2.reversa(),l1)

        
    def test_mapea(self):
        """
        Prueba que la función mapea funcione correctamente.
        """
        vacia = Lista()
        elems1 = [random.randint(0,100) for i in range(5)]
        elems2 = [j+2 for j in elems1]
        elems3 = [j*10 for j in elems2]
        l1 = Lista(elems1)
        l2 = Lista(elems2)
        l3 = Lista(elems3)

        self.assertIsNot(vacia, vacia.mapea(lambda x: x))
        self.assertEqual(l1.mapea(lambda x: x+2),l2)
        self.assertEqual(l2.mapea(lambda x: x*10),l3)

        
    def test_filtra(self):
        """
        Prueba que la función filtra funcione correctamente.
        """
        vacia = Lista()
        elems1 = [i for i in range(10)]
        elems2 = [i for i in range(6,10)]
        l1 = Lista(elems1)
        l2 = Lista(elems2)
        l3 = Lista(['h','o','l','a','m','u','n','d','o'])
        l4 = Lista(['h','l','a','m','u','n','d'])

        self.assertIsNot(vacia, vacia.filtra(lambda x: True))
        self.assertEqual(l1.filtra(lambda x: x > 5),l2)
        self.assertEqual(l2.filtra(lambda x: x == 6 or x == 8),Lista([6,8]))
        self.assertEqual(l3.filtra(lambda x: x != 'o'),l4)
