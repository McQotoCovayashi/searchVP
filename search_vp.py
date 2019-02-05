from PIL import Image
from intersection import *
from edge_search import * 

import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import itertools as itt

def inPoint(Data):
    Point = []
    Vector = []
    colorList = ["r", "g", "b", "c", "m", "y", "k"]
    for i in range(len(Data)):
        Point.append(Data[i][0])
        Vector.append([Data[i][1][0]-Point[i][0], Data[i][1][1]-Point[i][1]])
        plotVectorSet(Point[i], Vector[i], color = colorList[i % 7], label = "Vetor{}".format(i), s = 20)

    p = list(itt.combinations(Point, 2))
    #print(p)
    v = list(itt.combinations(Vector, 2))
    #print(v)    
    inPoint = []
    for j in range(len(v)):
        (Point1, Point2) = p[j]
        (Vector1, Vector2) = v[j] 
        xPoint = Intersection(Point1, Vector1, Point2, Vector2, label = "", plot = True,  marker = ",", s = 10)
        if xPoint == 'These 2 Vectors are PARALLEL.':
            continue
        inPoint.append(xPoint)

    return inPoint


Data = [
    [
        [149.00,196.00],[1425.82,796.00]
    ],[
        [3288.67,74.00],[2243.67,684.67]
    ],[
        [147.00,1756.00],[851.00,1413.00]
    ],[
        [3838.73,1940.73],[2254.73,1186.73]
    ]
]

im = select_image()
im_array = image2array(im)

plt.imshow(im_array)

x = inPoint(Data)
print(x)
plotView()
