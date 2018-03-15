import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams
fig1 = plt.figure(2)
rects =plt.bar(left = (0.2,1),height = (1,0.5),color=('r','g'),width = 0.2,align="center",yerr=0.000001)
plt.title('Pe')
def autolabel(rects):
  for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%s' % float(height))
autolabel(rects)
plt.xticks((0.2,1),('frst','second'))
plt.show()