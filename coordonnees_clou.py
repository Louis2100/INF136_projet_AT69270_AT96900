from transformation_geometrique import*

def calculer_coordonnees_clou(A,B,C,D,E):

    pt_0 = (-B/2, C/2)
    pt_1 = (-B/2, -C/2)
    pt_2 = (-B/2 - D, -A/2)
    pt_3 = (-B/2 - D, +A/2)
    pk_0 = (B/2 + E, 0)
    pk_1 = (B/2, -C/2)
    pk_2 = (B/2, C/2)

    return([('pt_0', pt_0),('pt_1', pt_1),('pt_2', pt_2),('pt_3', pt_3), ('pk_0', pk_0),('pk_1', pk_1),('pk_2', pk_2)])

def appliquer_transformation_clou(points_clou, center_rotation, angle_rotation, direction_inclinaison, angle_inclinaison, axe_reflexion):

    rang = 0
    v = []
    liste_reflexion = []
    liste_rotation = []
    liste_inclinaison = []

    while rang < len(points_clou):

        coordonnee = points_clou[rang]

        points_clou_x = coordonnee[1]
        points_clou_y = coordonnee[1]
        points_clou_x_2 = points_clou_x[0]
        points_clou_y_2 = points_clou_y[1]
        __REFLECTED_COORD = (coordonnee[0], calculer_reflexion_point(points_clou_x_2, points_clou_y_2, axe_reflexion))
        __ROTATED_COORD = (coordonnee[0], calculer_rotate_point(points_clou_x_2, points_clou_y_2, angle_rotation, center_rotation))
        __INCLIN_COORD = (coordonnee[0], calculer_inclinaison_point(points_clou_x_2, points_clou_y_2, angle_inclinaison, direction_inclinaison))


        liste_reflexion.append(__REFLECTED_COORD)
        liste_rotation.append(__ROTATED_COORD)
        liste_inclinaison.append(__INCLIN_COORD)

        rang += 1

    return liste_reflexion, liste_rotation, liste_inclinaison