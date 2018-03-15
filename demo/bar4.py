import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams
fig1 = plt.figure(2)
rects1 =plt.bar(left = (0.2),height = (0.5),color=('g'),label=(('no1')),width = 0.2,align="center",yerr=0.000001)
rects2 =plt.bar(left = (1),height = (1),color=('r'),label=(('no2')),width = 0.2,align="center",yerr=0.000001)
plt.legend()
plt.xticks((0.2,1),('frst','second'))
plt.title('Pe')
 
def autolabel(rects):
  for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%s' % float(height))
autolabel(rects1)
autolabel(rects2)
plt.show()

# 下面这个函数是用来垂直显示的，其中设置角度就可以以任意方式来显示。
# def autolabel(rects,Num=1.12,rotation1=90,NN=1):
#     for rect in rects:
#       height = rect.get_height()
#       plt.text(rect.get_x()-0.04+rect.get_width()/2., Num*height, '%s' % float(height*NN),rotation=rotation1)

# rects1 =plt.bar(left = (0.05),height = (Pe_FH),color=('b'),label=('FHMM'),width = 0.1,align="center",yerr=0.000001);
# autolabel(rects1,1.09);