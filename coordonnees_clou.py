# Importation des fonctions nécessaires pour le calcul des coordonnees des clous
from transformation_geometrique import*

"""
Cette fonction détermine les coordonnées d'un clou en suivant la paramétrisation illustrée dans la Figure 1.
Arguments : 
    A, B, C, D, E (float): Dimensions spécifiques du clou, utilisées pour calculer les coordonnées.

Retourne : 
    (list): Une liste de tuples, où chaque tuple contient :
        ● Une chaîne de caractères indiquant le nom du point (par exemple, "pt_0").
        ● Un tuple de deux nombres (float, float) représentant les coordonnées du point dans un plan 2D.
"""
def calculer_coordonnees_clou(A,B,C,D,E):
#calcul des coordonnees des clous
    pt_0 = (-B/2, C/2)
    pt_1 = (-B/2, -C/2)
    pt_2 = (-B/2 - D, -A/2)
    pt_3 = (-B/2 - D, +A/2)
    pk_0 = (B/2 + E, 0)
    pk_1 = (B/2, -C/2)
    pk_2 = (B/2, C/2)

    return([('pt_0', pt_0),('pt_1', pt_1),('pt_2', pt_2),('pt_3', pt_3), ('pk_2', pk_2), ('pk_0', pk_0),('pk_1', pk_1)])
"""
Cette fonction prend un ensemble de points clés représentant un clou et applique trois types de transformations 
géométriques : réflexion,rotation et inclinaison. Chaque transformation est appliquée séquentiellement à tous les 
points clés.
Arguments : 
    point_clou (list): Une liste de tuples, où chaque tuple contient :
        ● Une chaîne de caractères indiquant le nom du point (par exemple, "pt_0").
        ● Un tuple de deux nombres (float, float) représentant les coordonnées du point dans un plan 2D.
    centre_rotation (tuple) : Le centre de rotation pour la transformation
    angle_rotation (float): L'angle de rotation en degrés.
    angle_inclinaison (float): L'angle d'inclinaison en degrés.
    direction_inclinaison (str): La direction de l'inclinaison ('x' ou 'y').
    axe_reflexion (str): L'axe de réflexion ('x' ou 'y').
Retourne : 
    (tuple): Trois listes de tuples. Chaque liste correspond aux coordonnées des points clés après l'application d'une 
    des transformations (réflexion, rotation, inclinaison). Cela permet une analyse et une visualisation détaillées de 
    l'impact de chaque transformation sur la structure du clou.
"""
def appliquer_transformation_clou(points_clou, center_rotation, angle_rotation, direction_inclinaison,
    angle_inclinaison, axe_reflexion):

#initialisation des variables
    rang = 0
    coordonnee = []
    liste_reflexion = []
    liste_rotation = []
    liste_inclinaison = []

#parcours des listes de tuples
    while rang < len(points_clou):
        coordonnee = points_clou[rang]

        points_clou_x = coordonnee[1] #isolation du tuple des coordonnees
        points_clou_y = coordonnee[1] #isolation du tuple des coordonnees
        points_clou_x_2 = points_clou_x[0] #isolation coordonnee sur x
        points_clou_y_2 = points_clou_y[1] #isolation coordonnee sur y
        __REFLECTED_COORD = (coordonnee[0], calculer_reflexion_point(points_clou_x_2, points_clou_y_2, axe_reflexion))
        __ROTATED_COORD = (coordonnee[0], calculer_rotate_point(points_clou_x_2, points_clou_y_2, angle_rotation,
            center_rotation))
        __INCLIN_COORD = (coordonnee[0], calculer_inclinaison_point(points_clou_x_2, points_clou_y_2, angle_inclinaison,
            direction_inclinaison))


        liste_reflexion.append(__REFLECTED_COORD)
        liste_rotation.append(__ROTATED_COORD)
        liste_inclinaison.append(__INCLIN_COORD)

        rang += 1

    return liste_reflexion, liste_rotation, liste_inclinaison