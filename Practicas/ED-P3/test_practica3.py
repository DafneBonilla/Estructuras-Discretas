import unittest
import practica3 as p3

class TestPractica3(unittest.TestCase):

    def test_encripta_cadena(self):
        cadenas =  ["este es el grupo de discretas"]
        cadenas += ["ya casi acabamos el año"]
        cadenas += ["perros o gatitos?"]

        respuestas =  ['pstes ee e lrguido  edecsrats']
        respuestas += ['bs yacaai caeoams al ño']
        respuestas += [' reprso oiagtots?']

        for i in range(len(cadenas)):
            self.assertEqual(p3.encripta_cadena(cadenas[i]), respuestas[i])

    def test_es_primo(self):
        self.assertTrue(p3.es_primo(19))
        self.assertFalse(p3.es_primo(20))
        self.assertTrue(p3.es_primo(47))
        self.assertFalse(p3.es_primo(890))

    def test_decimal_binario(self):
        """
        Prueba que la función decimal_binario funcione.
        """
        self.assertEqual(p3.decimal_binario(0),0)
        self.assertEqual(p3.decimal_binario(2),10)
        self.assertEqual(p3.decimal_binario(15),1111)

    def test_suma_triangulo(self):
        """
        Prueba que la función suma_triangulo funcione.
        """
        l1=[1,2,3,4,5]
        l2=[6,3,9,12]
        self.assertEqual(p3.suma_triangulo([]),[[]])
        self.assertEqual(p3.suma_triangulo(l1),[[48], [20, 28], [8, 12, 16], [3, 5, 7, 9], [1, 2, 3, 4, 5]])
        self.assertEqual(p3.suma_triangulo(l2),[[54], [21, 33], [9, 12, 21], [6, 3, 9, 12]])

    def test_suma_consecutivos(self):
        """
        Prueba que la función suma_consecutivos funcione.
        """
        l1=p3.suma_consecutivos([7,8,26,1])
        l2=p3.suma_consecutivos([3,7,4,0,2])

        self.assertEqual(p3.suma_consecutivos([]),[])
        self.assertEqual(p3.suma_consecutivos([1]),[1])
        self.assertEqual(l1,[15,34,27])
        self.assertEqual(l2,[10,11,4,2])
        self.assertEqual(p3.suma_consecutivos(l1),[49,61])
        self.assertEqual(p3.suma_consecutivos(l2),[21,15,6])
        self.assertEqual(p3.suma_consecutivos([49,61]),[110])

    def test_suma_potencias(self):
        numeros = [243, 23, 867]
        al_cuadrado = [29,13,149]
        al_cubo = [99,35,1071]

        for i in range(len(numeros)):
            self.assertEqual(p3.suma_potencias(numeros[i], 2),al_cuadrado[i])
            self.assertEqual(p3.suma_potencias(numeros[i], 3),al_cubo[i])

    def test_oculta_caracter(self):
        respuestas = ['(x)', '((x))', '(((x)))', '((((x))))', '(((((x)))))']
        respuestas += [ '((((((x))))))', '(((((((x)))))))', '((((((((x))))))))']
        respuestas += [ '(((((((((x)))))))))']

        for i in range(1, 10):
            self.assertEqual(p3.oculta_caracter("x",i),respuestas[i-1])

    def test_numero_de_formas(self):
        escalones = [5,6,7,8,9,30]
        resultados = [13,24,44,81,149,53798080]

        for i in range(len(escalones)):
            self.assertEqual(p3.numero_de_formas(escalones[i]),resultados[i])

    def test_consonante_a_f(self):
        """
        Prueba que la función consonante_a_f funcione.
        """
        s1="anita lava la tina"
        s2="Hola Mundo"
        s3="supercalifragilisticoespialidoso"

        self.assertEqual(p3.consonante_a_f("a"),"a")
        self.assertEqual(p3.consonante_a_f("b"),"f")
        self.assertEqual(p3.consonante_a_f(s1),"afifa fafa fa fifa")
        self.assertEqual(p3.consonante_a_f(s2),"fofa fuffo")
        self.assertEqual(p3.consonante_a_f(s3),"fufeffafiffafififfifoeffiafifofo")
