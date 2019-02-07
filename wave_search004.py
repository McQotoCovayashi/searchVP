from edge_search import *
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

path = select_image(1)
im = Image.open(path)
im_array = image2array(im)
width = im.width
height = im.height
helical_number = 200
threshold = 2000
d = 100
Px = 1775
Py = 962

helix = make_helix(Px, Py, width, height, helical_number, d)
result = presearch(helix, im_array)
dif1 = differential(result, 1)
dif1_a = np.array(dif1)
dif12 = [dif1_a[0], dif1_a[1] ** 2]

picked_list = pick_points(dif12, threshold, 65535)
picked_point = helix2position(picked_list, Px, Py, helical_number, width, height, d)

plt.imshow(im_array)
scatter(picked_point, color = "r", marker = "x", s = 1, label = "cycle:{0}\nthreshold\n:{1}\n{2} points".format(helical_number,threshold,len(picked_list[0])))

plot_output()


