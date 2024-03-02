# Importation du package Image de la bibliothèque Pillow
from PIL import Image
import numpy as np
from math import log10

"""
Cette fonction transforme une image en couleur en une nouvelle image en niveaux de gris.
Arguments :
    chemin_image_couleur (str): Le chemin de l'image en couleur à transformer.
    chemin_sauvegarde_gris (str): Le chemin où sauvegarder l'image résultante en niveaux de gris.

Retourne :
    Rien : La fonction ne retourne rien mais sauvegarde l'image en niveaux de gris au chemin spécifié.
"""

def appliquer_rgb_to_gry(chemin_image_couleur, chemin_sauvegarde_gris):

    # Ouvrir l'image en utilisant PIL
    image = Image.open(chemin_image_couleur)

    # Obtenir les dimensions de l'image
    largeur, hauteur = image.size

    # Créer une nouvelle image en niveaux de gris
    nouvelle_image = Image.new("L", (largeur, hauteur))

    # Parcourir chaque pixel de l'image
    for y in range(hauteur):
        for x in range(largeur):
            # Obtenir la couleur du pixel à la position (x, y)
            couleur_pixel = image.getpixel((x, y))

            # Calculer la moyenne des composantes R, G, B
            rouge, vert, bleu = couleur_pixel
            moyenne = round((rouge + vert + bleu) / 3)

            # Remplacer le pixel dans la nouvelle image avec la moyenne en niveaux de gris
            nouvelle_image.putpixel((x, y), moyenne)

    # Enregistrer la nouvelle image en niveaux de gris
    nouvelle_image.save(chemin_sauvegarde_gris)

# Appel de la fonction en passant le chemin de l'image en argument
#appliquer_rgb_to_gry('image_couleur.jpg', 'image_niveaux_de_gris.jpg')


""""
Cette fonction prend une image en niveaux de gris sous forme d'un tableau NumPy 2D et applique une transformation pour 
simplifier et extraire des caractéristiques significatives de l'image.
Arguments :
    image_gris (numpy.ndarray): Un tableau 2D NumPy représentant une image en niveaux de gris.
Retourne : 
    numpy.ndarray: Un tableau 2D NumPy résultant de la transformation appliquée.
"""

def appliquer_transformation_1(image_gris):

    # Ouverture de l'image et conversion en tableau NumPy pour le traitement
    #img = Image.open(image_gris).convert('L')
    img_array = image_gris

    #image = np.array(image_gris)
    #img_array = image_gris
    # Obtenir les dimensions du tableau
    nombre_lignes = len(img_array)
    nombre_colonnes = len(img_array[0])

    #initialisation des variables
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
    return tableau_temp

#appliquer_transformation_1('image_gris.jpg')

def appliquer_transformation_2(img_array, rayon):

    # Obtenir les dimensions du tableau
    nombre_lignes, nombre_colonnes = img_array.shape

    # initialisation des variables
    tableau_sortie = np.zeros((nombre_lignes, nombre_colonnes))

    # Pour chaque pixel, on extrait ses valeurs des voisins (V=8).

    for x in range(rayon, nombre_lignes - rayon):
        for y in range(rayon, nombre_colonnes - rayon):
            tableau_sortie[x, y] += np.log10(1.0 + np.abs(img_array[x, y + rayon] - 2 * img_array[x, y] + img_array[x, y - rayon]))
            tableau_sortie[x, y] += np.log10(1.0 + np.abs(img_array[x + rayon, y] - 2 * img_array[x, y] + img_array[x - rayon, y]))
            tableau_sortie[x, y] += np.log10(
                1.0 + np.abs(img_array[x - rayon, y + rayon] - 2 * img_array[x, y] + img_array[x + rayon, y- rayon]))

    matrice = tableau_sortie.astype(np.int32)
    return matrice
