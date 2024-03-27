# Importation des modules nécessaires pour le calcul des transformations géométriques des points.
from math import cos
from math import sin
from math import tan

# Définition de la constante PI
PI = 3.14159265359
"""
Cette fonction applique une réflexion (miroir) à un point par rapport à un axe spécifié.
Arguments : 
    point (tuple): Un tuple (x, y) représentant les coordonnées du point à réfléchir. 
    axe (str): L'axe de réflexion.
    
Retourne : 
    (tuple): Un tuple (x', y') représentant les nouvelles coordonnées du point après la réflexion.
"""
def calculer_reflexion_point(x,y,axe):
#l'axe est 'x', la réflexion se produit par rapport à l'axe vertical (mirroir horizontal),changeant la coordonnée y du
# point.
    if axe == 'x':
        y = -y
#Si l'axe est 'y', la réflexion se produit par rapport à l'axe horizontal (mirroir vertical),changeant la coordonnée x.
    else:
        x = -x

    return(x, y)

"""
Cette fonction prend un point dans le plan cartésien et le fait pivoter autour d'un point central donné (le centre 
de rotation) d'un certain angle.
Arguments : 
    point (tuple): Un tuple (x, y) représentant les coordonnées du point à
faire pivoter.
    angle (float): L'angle de rotation en degrés.
    centre (tuple) : Un tuple représentant les coordonnées du centre de rotation. Par défaut, il s'agit de 
    l'origine (0, 0).

Retourne : 
    (tuple): Un tuple (x', y') représentant les nouvelles coordonnées du point après la rotation.
"""
def calculer_rotate_point(x,y,angle,centre=(0,0)):
#Une valeur positive entraîne une rotation antihoraire,
    if angle > 0:
        x_2 = x*cos(angle*PI/180) - y*sin(angle*PI/180) #transformation angle en radian
        y_2 = x*sin(angle*PI/180) + y*cos(angle*PI/180) #transformation angle en radian
#Une valeur négative entraîne une rotation horaire.
    else:
        x_2 = - x*cos(angle*PI/180) + y*sin(angle*PI/180) #transformation angle en radian
        y_2 = - x*sin(angle*PI/180) + y*cos(angle*PI/180) #transformation angle en radian
#Les résultats sont arrondis à deux chiffres après la virgule.
    return(round(x_2, 2), round(y_2, 2))

"""
Cette fonction applique une transformation d'inclinaison (cisaillement) sur un point. L'inclinaison est déterminée par 
un angle en degrés et peut être appliquée selon l'axe des x ou l'axe des y.
Arguments :
    point (tuple): Un tuple (x, y) représentant les coordonnées du point à incliner.
    angle (float): L'angle d'inclinaison en degrés. L'angle détermine l'intensité de la transformation de cisaillement.
    direction (str) : La direction de l'inclinaison

Retourne : 
    (tuple): Un tuple (x', y') représentant les nouvelles coordonnées du point après l'inclinaison.
"""

def calculer_inclinaison_point(x,y,angle,direction):
#m=tan(angle) est la tangente de l'angle d'inclinaison, et cette valeur détermine le degré d'inclinaison.
    m = tan(angle * PI / 180) #transformation angle en radian
#pour une inclinaison horizontale
    if direction == 'x':

        x_a = x + m*y
        y_a = y
#pour une inclinaison verticale
    elif direction == 'y':
        x_a = x
        y_a = m*x + y
#Les résultats sont arrondis à deux chiffres après la virgule.
    return(round(float(x_a), 2), round(float(y_a), 2))








