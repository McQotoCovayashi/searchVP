import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import tkinter as tk
import tkinter.filedialog as fdialog
import os


def select_image(option = 0):
    root = tk.Tk()
    root.withdraw()
    dir = os.getcwd()
    path = fdialog.askopenfilename(initialdir = dir, title = "select a image file.")
    if option == 0:
        image = Image.open(path)
        return image
    elif option == 1:
        return path
    else:
        raise Exception('Error!')


def image2array(image, option = 0):
    #option
    # 0:np.array
    # 1:width
    # 2:height
    # 3:[width, height]
    im_array = np.asarray(image)
    width = len(im_array[0])
    height = len(im_array)
    if option == 0:
        return im_array
    elif option == 1:
        return width
    elif option == 2:
        return height
    elif option == 3:
        return [width, height]
    else:
        raise Exception('Error!')
   

def make_wave(cycle_number, width, height):
    x = []
    y = []
    step = 360 * cycle_number
    for t in range(step):
        s = np.radians(t)
        amplitude = 0.5 * height -1
        xx = (width / step) * t
        yy = amplitude * np.sin(s) + 0.5 * height
        x.append(xx)
        y.append(yy)
    return [x, y]

def make_helix(Px, Py, width, height, helical_number = 10, d = 300):
    x = []
    y = []
    step = helical_number *360
    k = (0.5 * width - d)/(step)
    l = (0.5 * height - d)/(step)
    for t in range(step):
        s = np.radians(t)
        xx = int((k * t + d) * np.cos(s) + Px)
        yy = int((l * t + d) * np.sin(s) + Py)
        x.append(xx)
        y.append(yy)
    return [x, y]


def presearch(search_function, target_array):
    # search_function is list[x,y], and x, y are list too.
    # target_array is np.array.
    x = search_function[0]
    y = search_function[1]
    step = len(search_function[0])
    width = len(target_array[0])
    height = len(target_array)
    data = []
    degree = []
    for i in range(step):
        xx = int(x[i])
        yy = int(y[i])
        if xx < 0 or yy < 0 or xx > width or yy > height:
            continue
        value =  target_array[yy,xx]
        data.append(value)
        degree.append(i)
    datatable = [degree, data]
    return datatable


def differential(datatable, option = 1):
    # datatable is list[x,y], and x, y are list too.
    # option: differntial type
    #  0: dy = y[i] - y[i-1]
    #  1: dy = 0.5 * (y[i+1] - y[i-1])
    #  2: dy = 0.25 * (y[i+2] + y[i+1] - y[i-2] -y[i-1])
    x = datatable[0]
    y = datatable[1]
    step = len(datatable[0])
    xx = []
    dy = []
    if option == 0:
        i = 1
        for i in range(step):
            dx = x[i] - x[i-1]
            if dx != 1:
                continue
            xx.append(i)
            dy.append(int(y[i]) - int(y[i-1]))
    elif option == 1:
        i = 1
        for i in range(step - 1):
            dx = x[i+1] - x[i-1]
            if dx != 2:
                continue
            xx.append(i)
            dy.append(0.5 * (int(y[i+1])-int(y[i-1])))
    elif option == 2:
        i = 2
        for i in range(step - 2):
            dx = x[i+2] - x[i-2]
            if dx != 4:
                continue
            xx.append(i)
            dy.append(0.25 * (int(y[i+2]) + int(y[i+1]) - int(y[i-2]) -int(y[i-1])))
    else:
        raise Exception('Error!')
    return [xx, dy]


def list2csv(target_list):
    root = tk.Tk()
    root.withdraw()
    dir = os.getcwd()
    path = fdialog.asksaveasfilename(initialdir = dir, title = "save", filetype = ("",".csv"))
    data_frame = pd.DataFrame(target_list)
    data_frame.T.to_csv(path)


def plot(target_list, subplot = [1,1,1], label = None, color = "b", marker = None):
    plt.subplot(subplot[0],subplot[1],subplot[2])
    plt.plot(target_list[0], target_list[1], label = label, color = color, marker = marker)
    if type(label) is str :
        plt.legend()


def scatter(target_list, subplot = [1,1,1], label = None, color = "b", marker = ".", s = 5):
    plt.subplot(subplot[0],subplot[1],subplot[2])
    plt.scatter(target_list[0], target_list[1], label = label, color = color, marker = marker, s = s)
    if type(label) is str :
        plt.legend()


def pick_points(data, min, max):
    # data is list[x,y]. x and y are list too.
    x = data[0]
    y = data[1]
    result = []
    step = len(data[0])
    xx = []
    yy = []
    for i in range(step):
        if y[i] <= max and y[i] >= min:
            xx.append(x[i])
            yy.append(y[i])
        else:
            continue
    result = [xx, yy]
    return result


def wave2position(data, cycle_number, width, height):
    degree = data[0]
    x = []
    y = []
    step = cycle_number *360
    for t in degree:
        s = np.radians(t)
        amplitude = 0.5 * height -1
        xx = (width / step) * t
        yy = amplitude * np.sin(s) + 0.5 * height
        x.append(xx)
        y.append(yy)
    return [x, y]

def helix2position(data, Px, Py, helical_number, width, height, d = 300):
    degree = data[0]
    x = []
    y = []
    step = helical_number *360
    k = (0.5 * width - d)/(step)
    l = (0.5 * height - d)/(step)
    for t in degree:
        s = np.radians(t)
        xx = int((k * t + d) * np.cos(s) + Px)
        yy = int((l * t + d) * np.sin(s) + Py)
        x.append(xx)
        y.append(yy)
    return [x, y]

def plot_output(path = None, file_name = "data", dialog = True):
    if path is None:
        plt.show()
    if path is not None:
        if dialog is True:
            root = tk.Tk()
            root.withdraw()
            path  = fdialog.asksaveasfilename(initialdir = os.path.dirname(path), initialfile = file_name , defaultextension = "png")
        plt.savefig(path)