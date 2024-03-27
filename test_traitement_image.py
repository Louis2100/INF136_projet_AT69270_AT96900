import numpy as np
from traitement_image import *
def test_appliquer_transformation_1_a(image_gris):

    print(appliquer_transformation_1(image_gris))

test_appliquer_transformation_1_a(np.array([[2,5,3,9,15],[6,7,9,1,5],[3,8,4,2,9],[2,3,5,8,2],[1,2,3,2,1]]))

def test_appliquer_transformation_2_a(image_gris):

    print(appliquer_transformation_1(image_gris))

test_appliquer_transformation_2_a(np.array([[88,20,56,49,145,123],[60,17,99,121,55,56],[80,8,45,100,99,30],
    [255,23,155,88,12,78],[100,200,23,82,155,254]]))
def test_appliquer_transformation_2_a(tableau, rayon):

    print(appliquer_transformation_2(tableau, rayon))

test_appliquer_transformation_2_a(np.array([[88,102,133,49,145,123],[14,100,200,121,55,56],[40,101,92,100,99,30],
    [255,23,155,88,12,78], [100,200,23,82,155,254]]), 1)
def test_appliquer_transformation_2_b(tableau, rayon):

    print(appliquer_transformation_2(tableau, rayon))

test_appliquer_transformation_2_b(np.array([[88,102,133,49,145,123],[14,100,200,121,55,56],[40,101,92,100,99,30],
    [255,23,155,88,12,78], [100,200,23,82,155,254]]), 2)
