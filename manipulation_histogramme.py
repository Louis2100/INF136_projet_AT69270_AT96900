# Importation du package Image de la bibliothèque Pillow
# Importation du package Numpy
# Importation de la bibliothèque de mathématiques
from PIL import Image
import numpy as np
"""
Génère un histogramme pour chaque pixel de l'image en utilisant un carré de voisinage de taille spécifiée.
Arguments :
    tableau_2D (numpy.ndarray): Un tableau 2D NumPy représentant une image.
    w (int): La taille du carré de voisinage autour de chaque pixel pour lequel l'histogramme est calculé.
Retourne :
    numpy.ndarray: Un tableau 2D NumPy où chaque ligne représente un histogramme pour le carré correspondant de l'image.
"""

def calculer_histogramme(tableau_2D, w):

    # Obtenir les dimensions du tableau
    nombre_lignes, nombre_colonnes = tableau_2D.shape

    # Recherche de la valeur maximale
    max_value = np.max(tableau_2D)

    # Création d'une matrice vide
    matrice = []
        #np.zeros((nombre_lignes - w + 1, nombre_colonnes - w + 1, 4), dtype=int))

    # Parcours des pixels du carré de taille W*W
    for x in range(nombre_lignes - w + 1):
        for y in range(nombre_colonnes - w + 1):

            # Extraire le carré
            window = tableau_2D[x:x+w, y:y+w]

            hist, _ = np.histogram(window, bins=[0, max_value / 4, max_value / 2, (3 * max_value) / 4, max_value],
                range=(0, max_value))

            matrice.append(hist)

    return np.array(matrice)

# Test avec les données fournies
#resultat = calculer_histogramme(np.array([[255,160,10,49],[20,170,1,121],[30,233,230,100],[255,23,155,88]]), 3)
#print(resultat)


def calculer_distance_1(histo_1, histo_2):

    distance = 0

    for element in range(0, len(histo_1)):

        distance += (histo_2[element]-histo_1[element])**2

    distance_finale = np.round(distance**0.5,2)

    return distance_finale

#calculer_distance_1([1,2,3,4,5],[2,3,4,5,6])

def calculer_distance_2(histo_1, histo_2):

    distance = 0

    for element in range(0, len(histo_1)):

        distance += abs(histo_2[element]-histo_1[element])

    distance_finale = round(distance, 2)

    return distance_finale

#calculer_distance_2([1,2,3,4,5],[2,3,4,5,6])