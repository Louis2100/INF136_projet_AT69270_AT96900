# Importation des fonctions nécessaires pour tester le calcul des transformations
# géométriques des points.
from transformation_geometrique import *

def test_calculer_reflexion_point_1(x,y,axe):

    print(calculer_reflexion_point(x,y,axe)==(2,-4),'= (2,-4) : calculer_reflexion_point')

test_calculer_reflexion_point_1(2,4,'x')

def test_calculer_reflexion_point_2(x,y,axe):

    print(calculer_reflexion_point(x, y, axe)==(-2,4),'= (-2,4) : calculer_reflexion_point')

test_calculer_reflexion_point_2(2,4,'y')

def test_rotate_point(x,y,angle,centre=(0,0)):

    print(calculer_rotate_point(x,y,angle,centre=(0,0))==(-0.27, 4.46),'= (-0.27, 4.46) : calculer_rotate_point')

test_rotate_point(2,4,30)

def test_calculer_inclinaison_point_1(x,y,angle,direction):

    print(calculer_inclinaison_point(x,y,angle,direction)==(2.35, 4.0),'= (2.35, 4.0) : calculer_inclinaison_point')

test_calculer_inclinaison_point_1(2,4,5,'x')

def test_calculer_inclinaison_point_2(x,y,angle,direction):

    print(calculer_inclinaison_point(x, y, angle, direction) == (2.0, 4.17), '= (2.0, 4.17) : = calculer_inclinaison_point')

test_calculer_inclinaison_point_2(2,4,5,'y')

