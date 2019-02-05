import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import itertools as itt

def Intersection(Point1, Vector1, Point2, Vector2, plot = False, label = 'intersection Point', color = 'c', marker = 'x', s = 50):
    if la.norm(Vector1)==0 or la.norm(Vector2)==0 :
        return "Vectro1 or Vector2 are ZERO Vector. An intersection Point is NOT exist."
    if Vector1[0]/Vector1[1]==Vector2[0]/Vector2[1]:
        return "Vectro1 and Vector2 are PARALLEL. An intersection Point is NOT exist."
    array1 = np.array([Point1,Vector1])
    array2 = np.array([Point2,Vector2])
    arrayV = np.array([Vector1,Vector2])

    intersection = []

    for i in range(2):
        t = (Vector1[i]*la.det(array2)-Vector2[i]*la.det(array1))/la.det(arrayV)
        intersection.append(t)
    if plot == True:
        plt.scatter(intersection[0], intersection[1], label = label, color = color, marker = marker, s = s )
    return intersection

def plotVectorSet(Point, Vector, label = None, color = 'b', marker = 'o', s = 10):
    xV= []
    yV= []
    xV.append(Point[0])
    xV.append(Point[0]+Vector[0])
    yV.append(Point[1])
    yV.append(Point[1]+Vector[1])
    plt.scatter(Point[0],Point[1], label = label, color = color, marker = marker, s = s )
    plt.plot(xV,yV, color = color)

def plotView(xlabel = 'x', ylabel = 'y', title = None, legend = True):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title != None:
        plt.title(title)
    if legend == True:
        plt.legend()
    plt.show()