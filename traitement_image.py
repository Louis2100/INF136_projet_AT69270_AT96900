# Importation du package Image de la bibliothèque Pillow
from PIL import Image
import numpy as np

"""
Cette fonction transforme une image en couleur en une nouvelle image
en niveaux de gris.
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
#appliquer_rgb_to_gry('image_couleur.jpg', 'image_gris.jpg')


def appliquer_transformation_1(image_gris):

    # Ouverture de l'image et conversion en tableau NumPy pour le traitement
    img = Image.open(image_gris).convert('L')
    img_array = np.array(img)

    #Nombre constant de voisin égal à 8
    NOMBRE_VOISIN = 8

    #initialisation des variables
    resultat = 0

    image = np.array(image_gris)
    # Obtenir les dimensions du tableau
    nombre_lignes = len(img_array)
    nombre_colonnes = len(img_array[0])

    print(nombre_lignes, nombre_colonnes)
    # Pour chaque pixel, on extrait ses valeurs des voisins (V=8).

    for i in range(nombre_lignes):

        for j in range(nombre_colonnes):

            valeur_pixel_central = img_array[i][j]

            tableau_temp = [[img_array[i-1, j-1]],[img_array[i-1]], [img_array[i-1, j+1]],
                            [img_array[i, j-1]],[img_array[i, j]], [img_array[i, j+1]],
                            [img_array[i+1, j-1]], [img_array[i+1]], [img_array[i+1, j+1]]]
            for h in range (len(tableau_temp)):
                for l in range (len(tableau_temp)):

                    valeur_pixel_voisin = tableau_temp[h][l]

                if valeur_pixel_voisin >= valeur_pixel_central:
                    s = 1

                    tableau_temp[h][l] = 1
                else:
                    s = 0
                    tableau_temp[h][l] = 0

                    for v in range(NOMBRE_VOISIN):

                        resultat += s(valeur_pixel_voisin - valeur_pixel_central)*2**v



appliquer_transformation_1('image_gris.jpg')