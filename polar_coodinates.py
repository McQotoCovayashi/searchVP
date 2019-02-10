import numpy as np

def xy2polar(x_list, y_list, o_x, o_y):
    #This function converts the orthogonal coordinates of x - y into polar coordinates.
    #x_list, y_list: the orthogonal coordinates
    #o_x , o_y : Position of polar origin
    if len(x_list) != len(y_list):
        raise Exception('Error!:x and y must be lists of the same size.')
    r = [np.sqrt((x_list[i] - o_x) ** 2 + (y_list[i] - o_y) ** 2) for i in range(len(x_list)) ]
    s = [np.arccos((x_list[i] - o_x)/r[i]) for i in range(len(x_list))]
    polar = [(r[i], s[i]) for i in range(len(r))]
    return polar

def get_Linear_equation(data_1, data_2):
    # This function gives distance and angle of perpendicular_line.
    # Linear curvature equation is "r * cos(s - s_p) = r_p"
    # In addition, this function can also find the intersection 
    # by inputting two straight line equations.
    ###############################################################
    # data:Taple (r, s)
    # r : Radius or distance between a point of data to polar origin.
    # s : Angle in radians.
    r1 = data_1[0]
    r2 = data_2[0]
    a = r1 / r2
    s1 = data_1[1]
    s2 = data_2[1] 
    s_p = np.arctan(- (a * np.cos(s1) - np.cos(s2))/(a * np.sin(s1) - np.sin(s2)))
    r_p = r1 * (np.cos(s1 - s_p))
    result = [r_p, s_p]
    return result
