import numpy as np
from traitement_image import *
def test_appliquer_transformation_1_a(img_array):

    # Obtenir les dimensions du tableau
    nombre_lignes = len(img_array)
    nombre_colonnes = len(img_array[0])
    tableau_temp = np.zeros((nombre_lignes, nombre_colonnes))
    resultat = 0

    # Pour chaque pixel, on extrait ses valeurs des voisins (V=8).

    for i in range(1, nombre_lignes - 1):

        for j in range(1, nombre_colonnes - 1):

            tableau_temp2 = np.array([[img_array[i - 1][j - 1], img_array[i - 1][j], img_array[i - 1][j + 1]],
                                      [img_array[i][j - 1], img_array[i][j], img_array[i][j + 1]],
                                      [img_array[i + 1][j - 1], img_array[i + 1][j], img_array[i + 1][j + 1]]])

            valeur_pixel_central = img_array[i][j]

            if tableau_temp2[0][0] >= valeur_pixel_central:
                nombre_voisin = 7
                resultat += 2 ** nombre_voisin

            if tableau_temp2[0][1] >= valeur_pixel_central:
                nombre_voisin = 6
                resultat += 2 ** nombre_voisin

            if tableau_temp2[0][2] >= valeur_pixel_central:
                nombre_voisin = 5
                resultat += 2 ** nombre_voisin

            if tableau_temp2[1][2] >= valeur_pixel_central:
                nombre_voisin = 4
                resultat += 2 ** nombre_voisin

            if tableau_temp2[2][2] >= valeur_pixel_central:
                nombre_voisin = 3
                resultat += 2 ** nombre_voisin

            if tableau_temp2[2][1] >= valeur_pixel_central:
                nombre_voisin = 2
                resultat += 2 ** nombre_voisin

            if tableau_temp2[2][0] >= valeur_pixel_central:
                nombre_voisin = 1
                resultat += 2 ** nombre_voisin

            if tableau_temp2[1][0] >= valeur_pixel_central:
                nombre_voisin = 0
                resultat += 2 ** nombre_voisin

            tableau_temp[i][j] = resultat
            resultat = 0

    print(np.array(img_array),end="\n"), print(tableau_temp)

#test_appliquer_transformation_1_a([[2,5,3,9,15],[6,7,9,1,5],[3,8,4,2,9],[2,3,5,8,2],[1,2,3,2,1]])

def test_appliquer_transformation_2_a(img_array):

    print(test_appliquer_transformation_1_a(img_array))

#test_appliquer_transformation_2_a([[88,20,56,49,145,123],[60,17,99,121,55,56],[80,8,45,100,99,30],[255,23,155,88,12,78],[100,200,23,82,155,254]])

def test_appliquer_transformation_2_a(tableau, rayon):

    print(appliquer_transformation_2(tableau, rayon))

test_appliquer_transformation_2_a(np.array([[88,102,133,49,145,123],[14,100,200,121,55,56],[40,101,92,100,99,30],[255,23,155,88,12,78], [100,200,23,82,155,254]]), 1)
def test_appliquer_transformation_2_b(tableau, rayon):

    print(appliquer_transformation_2(tableau, rayon))

test_appliquer_transformation_2_b(np.array([[88,102,133,49,145,123],[14,100,200,121,55,56],[40,101,92,100,99,30],[255,23,155,88,12,78], [100,200,23,82,155,254]]), 2)
