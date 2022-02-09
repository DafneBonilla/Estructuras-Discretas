import unittest
from formulas import *

class TestFormula(unittest.TestCase):
    def test_tex_tabla(self):
        """
        Prueba que el método tex_tabla devuelva correctamente la fórmula con los separadores.
        """
        x1 = Formula(1)
        x2 = Formula(2)
        x3 = Formula(3)

        f1 = Formula(x3,'N')
        f2 = Formula(f1,'D',x2)
        f3 = Formula(x1,'C',x2)
        f4 = Formula(f1,'B',f3)
        f5 = Formula(x3,'I',f4)

        self.assertEqual(x1.tex_tabla(),'x_{1}')
        self.assertEqual(f1.tex_tabla(), '( & \lnot & x_{3})')
        self.assertEqual(f2.tex_tabla(), '(( & \lnot & x_{3}) & \lor & x_{2})')
        self.assertEqual(f3.tex_tabla(), '(x_{1} & \land & x_{2})')
        self.assertEqual(f4.tex_tabla(), '(( & \lnot & x_{3}) & \leftrightarrow & (x_{1} & \land & x_{2}))')
        self.assertEqual(f5.tex_tabla(), '(x_{3} & \\to & (( & \lnot & x_{3}) & \leftrightarrow & (x_{1} & \land & x_{2})))')


    def test_cabecera_tabla(self):
        """
        Prueba que el método _cabecera_tabla devuelva correctamente la cabecera
        de la tabla de verdad.
        """
        x1 = Formula(1)
        x2 = Formula(2)
        x3 = Formula(3)

        f1 = Formula(x1,'N')
        f2 = Formula(x1,'C',x2)
        f3 = Formula(f1,'D',x3)
        f4 = Formula(f3,'I',f2)
        f5 = Formula(f4,'B',f1)

        self.assertEqual(x1._cabecera_tabla(), '  x_{1} & x_{1} \\\\\n')
        self.assertEqual(f1._cabecera_tabla(), '  x_{1} & ( & \lnot & x_{1}) \\\\\n')
        self.assertEqual(f2._cabecera_tabla(), '  x_{1} & x_{2} & (x_{1} & \land & x_{2}) \\\\\n')
        self.assertEqual(f3._cabecera_tabla(), '  x_{1} & x_{3} & (( & \lnot & x_{1}) & \lor & x_{3}) \\\\\n')
        self.assertEqual(f4._cabecera_tabla(), '  x_{1} & x_{2} & x_{3} & ((( & \lnot & x_{1}) & \lor & x_{3}) & \\to & (x_{1} & \land & x_{2})) \\\\\n')
        self.assertEqual(f5._cabecera_tabla(), '  x_{1} & x_{2} & x_{3} & (((( & \lnot & x_{1}) & \lor & x_{3}) & \\to & (x_{1} & \land & x_{2})) & \leftrightarrow & ( & \lnot & x_{1})) \\\\\n')

    def test_renglon_verdad_negacion(self):
        """
        Prueba que el método _renglon_verdad genere correctamene los renglones
        de verdad para la negación.
        """
        x1 = Formula(1)
        x2 = Formula(2)
        f1 = Formula(x1,'N')
        f2 = Formula(Formula(f1,'C',x2),'N')
        asignaciones = list(product([1,0], repeat=1))

        self.assertEqual(f1._renglon_verdad(asignaciones[0]),"  1 & & \mathbf{0} & \\\\\n")
        self.assertEqual(f1._renglon_verdad(asignaciones[1]),"  0 & & \mathbf{1} & \\\\\n")


    def test_renglon_verdad_conjuncion(self):
        """
        Prueba que el método _renglon_verdad genere correctamene los renglones
        de verdad para la conjunción.
        """
        x1 = Formula(1)
        x2 = Formula(2)
        f1 = Formula(x1,'N')
        f2 = Formula(f1,'C',x2)

        asignaciones = list(product([1,0], repeat=2))

        self.assertEqual(f2._renglon_verdad(asignaciones[0]), "  1 & 1 & & 0 & & \mathbf{0} & \\\\\n")
        self.assertEqual(f2._renglon_verdad(asignaciones[1]), "  1 & 0 & & 0 & & \mathbf{0} & \\\\\n")
        self.assertEqual(f2._renglon_verdad(asignaciones[2]), "  0 & 1 & & 1 & & \mathbf{1} & \\\\\n")
        self.assertEqual(f2._renglon_verdad(asignaciones[3]), "  0 & 0 & & 1 & & \mathbf{0} & \\\\\n")

    def test_renglon_verdad_disyuncion(self):
        """
        Prueba que el método _renglon_verdad genere correctamene los renglones
        de verdad para la disyunción.
        """
        x1 = Formula(1)
        x2 = Formula(2)
        f1 = Formula(x1,'C',x2)
        f2 = Formula(x2,'D',f1)

        asignaciones = list(product([1,0], repeat=2))

        self.assertEqual(f2._renglon_verdad(asignaciones[0]), "  1 & 1 & & \mathbf{1} & & 1 & \\\\\n")
        self.assertEqual(f2._renglon_verdad(asignaciones[1]), "  1 & 0 & & \mathbf{0} & & 0 & \\\\\n")
        self.assertEqual(f2._renglon_verdad(asignaciones[2]), "  0 & 1 & & \mathbf{1} & & 0 & \\\\\n")
        self.assertEqual(f2._renglon_verdad(asignaciones[3]), "  0 & 0 & & \mathbf{0} & & 0 & \\\\\n")

    def test_renglon_verdad_implicacion(self):
        """
        Prueba que el método _renglon_verdad genere correctamene los renglones
        de verdad para la implicación.
        """
        x1 = Formula(1)
        x2 = Formula(2)
        f1 = Formula(x2,'D',x1)
        f2 = Formula(x2,'I',f1)

        asignaciones = list(product([1,0], repeat=2))

        self.assertEqual(f2._renglon_verdad(asignaciones[0]), "  1 & 1 & & \mathbf{1} & & 1 & \\\\\n")
        self.assertEqual(f2._renglon_verdad(asignaciones[1]), "  1 & 0 & & \mathbf{1} & & 1 & \\\\\n")
        self.assertEqual(f2._renglon_verdad(asignaciones[2]), "  0 & 1 & & \mathbf{1} & & 1 & \\\\\n")
        self.assertEqual(f2._renglon_verdad(asignaciones[3]), "  0 & 0 & & \mathbf{1} & & 0 & \\\\\n")

    def test_renglon_verdad_bicondicional(self):
        """
        Prueba que el método _renglon_verdad genere correctamene los renglones
        de verdad para la bicondicional.
        """
        x1 = Formula(1)
        x2 = Formula(2)
        f1 = Formula(x1,'I',x2)
        f2 = Formula(x2,'B',f1)

        asignaciones = list(product([1,0], repeat=2))

        self.assertEqual(f2._renglon_verdad(asignaciones[0]), "  1 & 1 & & \mathbf{1} & & 1 & \\\\\n")
        self.assertEqual(f2._renglon_verdad(asignaciones[1]), "  1 & 0 & & \mathbf{1} & & 0 & \\\\\n")
        self.assertEqual(f2._renglon_verdad(asignaciones[2]), "  0 & 1 & & \mathbf{1} & & 1 & \\\\\n")
        self.assertEqual(f2._renglon_verdad(asignaciones[3]), "  0 & 0 & & \mathbf{0} & & 1 & \\\\\n")


if __name__ == "__main__":
    unittest.main()
