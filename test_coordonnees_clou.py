from coordonnees_clou import *

def test_coordonnees_clou(A,B,C,D,E):

    print(calculer_coordonnees_clou(A,B,C,D,E) == [('pt_0', (-5.0, 0.5)), ('pt_1', (-5.0, -0.5)), ('pt_2',
(-5.75, -1.5)), ('pt_3', (-5.75, 1.5)), ('pk_2', (5.0, 0.5)), ('pk_0', (7.0, 0)), ('pk_1', (5.0, -0.5))])

A = 3
B = 10
C = 1
D = 0.75
E = 2

test_coordonnees_clou(A,B,C,D,E)
