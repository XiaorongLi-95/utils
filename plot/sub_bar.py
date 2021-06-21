import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('text', usetex=True)
y_acc = [77.21, 77.37, 77.63] #ACC corresponding method
x_lab = [r'$\lambda=1$', r'$r=3$', r'$r=5$'] #method name
colors = {r'$r=1$': 'lightgreen',
          r'$r=3$': 'lightsalmon',
           r'$r=5$': 'lightskyblue'
#           'DFD': 'C3'
          }
y_bwt = [-2.92,-2.85, -2.46]
x_ind = np.arange(len(y_bwt))
def autolabel(rects, ax, off):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, off),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    

fig = plt.figure(figsize=(5,2))

ax1 = fig.add_subplot(1,2,1)
for xi, yi, li in zip(x_ind, y_acc, x_lab):
    rec = ax1.bar(xi, yi, label= li, color=colors[li])
    autolabel(rec, ax1, 3)

plt.ylim(70,80)
plt.ylabel('ACC(\%)',fontsize=12)
plt.xticks([],[])
# plt.xlabel( r'$\lambda=1$',fontsize=12)


ax2 = fig.add_subplot(1,2,2)
for xi, yi, li in zip(x_ind, y_bwt, x_lab):
    rec = ax2.bar(xi, yi,color=colors[li])
    autolabel(rec, ax2, -14)
    
plt.ylabel('BWT(\%)')
plt.ylim(-4,0)
plt.tight_layout()
plt.subplots_adjust(bottom=0.23)
fig.legend(bbox_to_anchor=(0.8,0.17),fontsize=10,ncol=3)


plt.xticks([],[])
# plt.xlabel( r'$\lambda=2$',fontsize=12)


plt.savefig('bar.pdf',bbox_inches='tight')
plt.show()
