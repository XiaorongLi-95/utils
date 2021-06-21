from mpl_toolkits.axes_grid1 import host_subplot
import matplotlib.pyplot as plt
# from matplotlib import rc
# rc('text', usetex=True)
plt.figure(figsize=(5,2))
plt.subplot(121)
plt.plot([0.7, 0.9, 1, 1.1, 1.3, 2], [75.6, 75.52, 77.21, 75.24, 75.38, 74.39], label='DFD', marker='*', markersize=5)
plt.axhline(y=70.7, color='darkseagreen', linestyle='solid',label='EWC')
plt.ylim(60,80)
plt.legend(loc='lower right',fontsize=10)
# plt.ylabel("ACC(\%)",fontsize=12)
# plt.xlabel(r'$\lambda$',fontsize=12)

plt.subplot(122)
plt.plot([0.7, 0.9, 1, 1.1, 1.3, 2], [-2.56, -2.31, -2.92, -2.3, -1.65, -2.36], label='DFD', marker='+', markersize=5, color ='red')
plt.axhline(y=-2.83, color='darkseagreen', linestyle='dashed',label='EWC')
plt.legend(loc='lower right',fontsize=10)
plt.ylim(-5,-1)
# plt.ylabel("BWT(\%)",fontsize=12)
# plt.xlabel(r'$\lambda$',fontsize=12)
# fig, axes = plt.subplots(12,figsize=(5,2.5))

# axes[0].plot()
# axes[0].axhline(y=70.7, color='darkseagreen', linestyle='solid',label='ACC-EWC')
# axes[0].set_ylim(55,80)
# #
#
# axes[1].set_ylabel("BWT(%)",fontsize=12)
# axes[1].set_xlabel('lambda')
# axes[1].plot([0.7, 0.9, 1, 1.1, 1.3, 2], [-2.56, -2.31, -2.92, -2.3, -1.65, -2.36], label='BWT', marker='+', markersize=5, color ='red')
# axes[1].axhline(y=-2.83, color='darkseagreen', linestyle='dashed',label='BWT-EWC')
# # axes[1].plt.ylim(-5,0)

# host.set_xlabel(r'$\lambda$',fontsize=16)
# host.yaxis.get_label().set_color(p1.get_color()) #ACC label text color
# par.yaxis.get_label().set_color(p2.get_color()) #BWT label text color


# leg =plt.legend(bbox_to_anchor=(0.7,0.5))

# plt.ylim(55,80)

# par.set_ylim(-5,0)


#set legend text color
# for text in leg.get_texts():
#     plt.setp(text, color = 'black')
# leg.texts[0].set_color(p1.get_color())
# leg.texts[1].set_color(p2.get_color())
plt.tight_layout()
plt.savefig('zhexian.pdf',bbox_inches='tight')

plt.show()
