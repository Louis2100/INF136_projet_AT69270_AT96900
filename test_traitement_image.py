import numpy as np

img_array = [[2,5,3,9,15],
             [6,7,9,1,5],
             [3,8,4,2,9],
             [2,3,5,8,2],
             [1,2,3,2,1]]
# Obtenir les dimensions du tableau
nombre_lignes = len(img_array)
nombre_colonnes = len(img_array[0])
tableau_temp = np.zeros((nombre_lignes+1,nombre_colonnes+1))
#print(img_array)
#print(nombre_lignes, nombre_colonnes)
#print(tableau_temp)
# Pour chaque pixel, on extrait ses valeurs des voisins (V=8).

for i in range(nombre_lignes-2):

    for j in range(nombre_colonnes-2):

        valeur_pixel_central = img_array[i+1][j+1]

        tableau_temp2 = [[img_array[i][0]], [img_array[0][j+1]], [img_array[0][j+2]],
                        [[img_array[i+1][0]], [img_array[i+1][j+1]], [img_array[i+1][j+2]],
                        [img_array[i+2][0]], [img_array[i+2][j+1]], [img_array[i+2][j+2]]]]
        #print(tableau_temp2)
        res = 0
        NOMBRE_VOISIN = 7
        for h in range(len(tableau_temp)):
            for l in range(len(tableau_temp)):
                valeur_pixel_voisin = tableau_temp[h][l]

            if valeur_pixel_voisin >= valeur_pixel_central:
                s = 1

                res += 2**NOMBRE_VOISIN

            else:
                s = 0

            NOMBRE_VOISIN -= 1
        print(res)
        tableau_temp [i,j] = res

print(tableau_temp)