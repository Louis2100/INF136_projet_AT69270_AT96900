from manipulation_histogramme import *
def test_calculer_histogramme(tableau_2D, w):

    print(calculer_histogramme(tableau_2D, w),' = [[[4 0 2 3], [3 2 2 2]], [[4 0 2 3],[2 3 2 2]]]')

test_calculer_histogramme(np.array([[255,160,10,49],[20,170,1,121],[30,233,230,100],[255,23,155,88]]),3)