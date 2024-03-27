# Importation du package Image de la bibliothèque Pillow
# Importation du package Numpy
# Importation du programme manipulation histogrammme
from PIL import Image
import numpy as np
from manipulation_histogramme import calculer_distance_1
import random
"""
Diviser un ensemble de points dans un plan 2D en un nombre défini de groupes.
Arguments :
    data (numpy.ndarray): Un tableau 2d numpy représentant l'ensemble de données à partitionner. Chaque ligne du tableau
     représente un histogramme décrivant un point.
    k (int): Le nombre de groupes à identifier dans l'ensemble de données.
    max_iterations (int): Le nombre maximal d'itérations que l'algorithme exécutera. La valeur par défaut est 50.
Retourne :
    numpy.ndarray: Un tableau numpy 1D où chaque élément correspond à l'indice du centre le plus proche pour chaque 
    point de l'ensemble de données. C'est un vecteur d'entiers de la même longueur que le nombre de points dans 'data', 
    indiquant l'affectation de groupe pour chaque point.
"""
def regrouper_points(points, K=2, iterations=50):
    # Choisir K points aléatoires comme centres de groupes initiaux
    indices = np.random.choice(len(points), size=K, replace=False)
    centres = [points[i] for i in indices]


    for _ in range(iterations):
        # Assigner chaque point au groupe dont le centre est le plus proche
        groupes = [[] for _ in range(K)]
        for point in points:
            distances = [np.linalg.norm(point - centre) for centre in centres]
            groupe_index = np.argmin(distances)
            groupes[groupe_index].append(point)

        # Mettre à jour les centres des groupes
        centres = [np.mean(groupe, axis=0) for groupe in groupes if groupe]

    # Assigner chaque point au groupe correspondant
    resultats = []
    for point in points:
        distances = [np.linalg.norm(point - centre) for centre in centres]
        groupe_index = np.argmin(distances)
        resultats.append(groupe_index)

    labels2_array = np.array(resultats)
    return labels2_array
