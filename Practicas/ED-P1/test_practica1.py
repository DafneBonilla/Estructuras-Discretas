import unittest
import practica1 as p1
import itertools
class TestPractica1(unittest.TestCase):
    def test_mcd(self):
        t1 = p1.maximo_comun_divisor(950, 480)
        t2 = p1.maximo_comun_divisor(336,360)
        self.assertEqual(t1, 10)
        self.assertEqual(t2, 24)

    def test_palindroma(self):
        t1 = p1.es_palindroma("anita lava la tina")
        t2 = p1.es_palindroma("yo dono rosas oro no doy")
        t3 = p1.es_palindroma("aniita lava la tina")
        self.assertTrue(t1)
        self.assertTrue(t2)
        self.assertFalse(t3)


    def test_promedio_tuplas(self):
        t1 = p1.promedio_tuplas(((11,30,7,5.2),(4,1.3,2.222,5.0,9,10,19),(40,30,20,10)))
        t2 = p1.promedio_tuplas(((10,20,19),(1,2.1,3.9,4.8),
                                (200,2.00,14,1.9),(4,9,13.9,12.2)))
        self.assertEqual(t1, [13.3, 7.217428571428571, 25.0])
        self.assertEqual(t2, [16.333333333333332, 2.95, 54.475, 9.774999999999999])


    def test_permutaciones(self):
        r1 = [1,2,3]
        r2 = [1,2,3,4,5]
        t1 = itertools.permutations(r1)
        t2 = itertools.permutations(r2)
        t1_p = p1.permutaciones(r1)
        t2_p = p1.permutaciones(r2)
        self.assertEqual(len(t1_p), 6)
        self.assertEqual(len(t2_p),120)
        for p in t1:
            self.assertTrue(list(p) in t1_p)
        for p in t2:
            self.assertTrue(list(p) in t2_p)

    def test_filtrar_pares(self):
        r1 = [1,2,3,4,5,6,7]
        r2 = [1200, 1451, 1300, 129, 2001]
        self.assertEqual(p1.filtrar_pares(r1),[2,4,6])
        self.assertEqual(p1.filtrar_pares(r2),[1200, 1300])

    def test_frecuencia(self):
        f = open("texto1.txt","r")
        c1 = f.read()
        f.close()
        c2 = "hola mi nombre es Alma, ya les había dicho que mi nombre es Alma ?"
        c3 = "hola mi nombre es Alma ya les había dicho que mi nombre es Alma ?"
        rp1 = p1.frecuencia(c1)
        rp2 = p1.frecuencia(c2)
        rp3 = p1.frecuencia(c3)
        #respuestas esperadas
        r1 = [
            ('intenso', 1), ('En', 2), ('grito', 1), ('comprendió:', 1),
            ('No', 1), ('más', 2), ('pasar', 1), ('ese', 1), ('perdón', 1),
            ('por', 2), ('lo', 3), ('silencio', 1), ('de', 3), ('cimientos', 1),
            ('Tazaki', 1), ('fragilidad.', 1), ('con', 3), ('mediante', 1),
            ('sólo', 1), ('pérdida.', 1), ('Dolor', 1), ('herida.', 1),
            ('Ésos', 1), ('herida', 1), ('verdadera', 1), ('sangre,', 1),
            ('momento,', 1), ('acepó.', 1), ('humanos', 1), ('sí', 1),
            ('Se', 1), ('Fragilidad', 1), ('desgarrador,', 1), ('profundo', 1),
            ('Tsukuro', 1), ('se', 2), ('sin', 3), ('mismo,', 1),
            ('armonía.', 1), ('existe', 3), ('derrame', 1), ('son', 1),
            ('unen', 2), ('bien,', 1), ('dolor.', 1), ('la', 2), ('aceptación', 1),
            ('fin', 1), ('los', 2), ('sentimiento', 1), ('corazones', 1),
            ('no', 3), ('armonía', 1), ('que', 1), ('un', 2)]
        r2 = [('Alma,', 1), ('dicho', 1), ('les', 1), ('nombre', 2), ('ya', 1),
            ('hola', 1), ('que', 1), ('es', 2), ('había', 1), ('mi', 2),
            ('Alma', 1), ('?', 1)]
        r3 = [('dicho', 1), ('les', 1), ('nombre', 2), ('ya', 1), ('hola', 1),
            ('que', 1), ('es', 2), ('Alma', 2), ('había', 1), ('mi', 2),
            ('?', 1)]

        for tupla in r1:
            self.assertTrue(tupla in rp1)

        for tupla in r2:
            self.assertTrue(tupla in rp2)

        for tupla in r3:
            self.assertTrue(tupla in rp3)

    def test_suma_digitos(self):
        nums = [1238,49132,389123,32983,2302,9,0]
        res  = [5,1,8,7,7,9,0]
        r = []

        for num in nums:
            r += [p1.suma_digitos(num)]
        self.assertEqual(res, r)

    def test_reemplaza_espacios(self):
        cadenas = []
        cadenas  += ["   Hola, así es como tiene que quedar"]
        cadenas  += ["Hola, así es como tiene que quedar"]
        cadenas  += ["Hola,    así   es como   tiene que quedar"]
        respuestas = ["+"*9 + "Hola,asíescomotienequequedar"]
        respuestas += ["+"*6 + "Hola,asíescomotienequequedar"]
        respuestas += ["+"*13 + "Hola,asíescomotienequequedar"]

        for i in range(len(cadenas)):
            self.assertEqual(respuestas[i], p1.reemplaza_espacios(cadenas[i]))

    def test_dibuja_triangulo(self):
        triangulo1 =  '* \n\n'
        triangulo3 =  '  * \n\n  * \n * * \n\n  * \n * * \n* * * \n\n'
        triangulo5 =  '    * \n\n    * \n   * * \n\n    * \n   * * \n  * * * \n\n'
        triangulo5 += '    * \n   * * \n  * * * \n * * * * \n\n    * \n   * * '
        triangulo5 += '\n  * * * \n * * * * \n* * * * * \n\n'

        self.assertEqual(triangulo1, p1.dibuja_triangulo(1))
        self.assertEqual(triangulo3, p1.dibuja_triangulo(3))
        self.assertEqual(triangulo5, p1.dibuja_triangulo(5))

    def test_pascal(self):
        respuestas = ['[1]\n']
        respuestas.append('[1]\n[1 1]\n[1 2 1]\n')
        respuestas.append('[1]\n[1 1]\n[1 2 1]\n[1 3 3 1]\n')
        respuestas.append('[1]\n[1 1]\n[1 2 1]\n[1 3 3 1]\n[1 4 6 4 1]\n')
        respuestas.append('[1]\n[1 1]\n[1 2 1]\n[1 3 3 1]\n[1 4 6 4 1]\n[1 5 10 10 5 1]\n')
        obtenidas =[1,3,4,5,6]

        for i in range(len(respuestas)):
            self.assertEqual(respuestas[i],p1.pascal(obtenidas[i]))
