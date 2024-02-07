from math import cos
from math import sin
from math import tan

PI = 3.14159265359

def calculer_reflexion_point(x,y,axe):

    if axe == 'x':
        y = -y
    else:
        x = -x

    return(x, y)

def calculer_rotate_point(x,y,angle,centre=(0,0)):

    if angle > 0:
        x_2 = x*cos(angle*PI/180) - y*sin(angle*PI/180)
        y_2 = x*sin(angle*PI/180) + y*cos(angle*PI/180)
    else:
        x_2 = - x*cos(angle*PI/180) + y*sin(angle*PI/180)
        y_2 = - x*sin(angle*PI/180) + y*cos(angle*PI/180)

    return(round(x_2, 2), round(y_2, 2))

def calculer_inclinaison_point(x,y,angle,direction):

    m = tan(angle * PI / 180)

    if direction == 'x':

        x_a = x + m*y
        y_a = y

    elif direction == 'y':
        x_a = x
        y_a = m*x + y


    return(round(float(x_a), 2), round(float(y_a), 2))








