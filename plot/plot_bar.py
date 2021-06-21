from mpl_toolkits.axes_grid1 import host_subplot
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)
x_ind = [1, 3, 5]
x_lab = [r'$r=1$', r'$r=3$', r'$r=5$']
plt.figure(figsize=(5,2))
plt.plot([1,3,5], [1.06, 3.18, 5.3],marker='*', markersize=5)
plt.xticks(x_ind,x_lab,fontsize=12)
plt.ylabel("Ratio(\%)",fontsize=12)
#set legend text color
# for text in leg.get_texts():
#     plt.setp(text, color = 'black')
# leg.texts[0].set_color(p1.get_color())
# leg.texts[1].set_color(p2.get_color())
plt.tight_layout()
plt.savefig('mem.pdf',bbox_inches='tight')

plt.show()
