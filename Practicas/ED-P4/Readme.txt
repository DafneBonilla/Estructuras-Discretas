Práctica 4: Listas
Integrantes: 2
Nombre                              No. de cuenta   Correo
Dafne Bonilla Reyes            -      319089660   -  daphnebonilla@ciencias.unam.mx
José Camilo García Ponce       -      319210536   -  jcamilo@ciencias.unam.mx

Comentarios(opcionales):
Alma usamos tu metodo concatena y fallo algunas veces las pruebas, tambien aveces fallaba contiene
estos son los errores que nos salieron:
======================================================================
ERROR: test_concatena (test_listas.TestLista)
Prueba que la función concatena funcione correctamente.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/Camilo/Practicas ED/ED-P4/test_listas.py", line 124, in test_concatena
    l2 = Lista(elems2)
  File "/home/Camilo/Practicas ED/ED-P4/listas.py", line 21, in init
    self.cabeza = elementos[0]
IndexError: list index out of range

----------------------------------------------------------------------
Ran 11 tests in 0.007s

FAILED (errors=1)
-
======================================================================
FAIL: test_contiene (test_listas.TestLista)
Prueba que la función contiene funcione correctamente.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/Camilo/Practicas ED/ED-P4/test_listas.py", line 96, in test_contiene
    self.assertEqual(lista.contiene(m),True)
AssertionError: False != True

----------------------------------------------------------------------
Ran 11 tests in 0.010s

FAILED (failures=1)