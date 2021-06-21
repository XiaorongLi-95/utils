import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)
fig = plt.figure(figsize=(6,3))
ax1 = fig.add_subplot(1,2,1)
x_ind = [2, 4, 6, 8, 10]
x_lab = [r'$\mathcal{T}_2$', r'$\mathcal{T}_4$', r'$\mathcal{T}_6$', r'$\mathcal{T}_8$', r'$\mathcal{T}_{{10}}$']
leg = [r'$\mathcal{T}_1$',r'$\mathcal{T}_2$',r'$\mathcal{T}_3$']
# fig, axs = plt.subplots(9,1)
# fig.subplots_adjust(hspace=0)
plt.xlabel('Task',fontsize=15)
plt.ylabel('Accuracy (\%)',fontsize=15)
plt.title('(a) 10-split CIFAR-100', y=-0.5, fontsize=15)
plt.ylim([50, 95])
ax1.plot([1,2,3,4,5,6,7,8,9,10], [87.4,83.7,85.0,82.8,85.5,84.6,83.6,84.7,83.5,83.7], label=leg[0], marker='*', markersize=5)#[89.1,82.0,84.6,83.6,85.1,84.1,82.7,82.2,82.4,84.2]
ax1.plot([2,3,4,5,6,7,8,9,10], [78.4,75.5,75.3,76.4,75.1,71.6,72.7,73.7,76.3], label=leg[1], marker='.', markersize=5)#[80.5,79.2,79.1,80.9,80.6,78.3,77.6,81,80.2]
ax1.plot([3,4,5,6,7,8,9,10], [79.9,73.2, 78.5,75.1,72.9,75.0,75.1,76.5], label=leg[2], marker='*', markersize=5)#[84.2,74.2,76.3,74.6,73.4,74.7,76.5,76.3]




plt.xticks(x_ind,x_lab,fontsize=12)
plt.yticks(size = 12)
# plt.legend(bbox_to_anchor=(1,0.48),fontsize=13)


ax2 = fig.add_subplot(1,2,2)
x_ind = [5, 10, 15, 20, 25]
x_lab = [r'$\mathcal{T}_5$', r'$\mathcal{T}_{{10}}$', r'$\mathcal{T}_{{15}}$', r'$\mathcal{T}_{{20}}$', r'$\mathcal{T}_{{25}}$']
# set_xlabel(r'$\mathcal{T}',fontsize=1)
# fig, axs = plt.subplots(9,1)
# fig.subplots_adjust(hspace=0)
plt.xlabel('Task',fontsize=15)
plt.ylabel('Accuracy (\%)',fontsize=15)
plt.title('(b) 25-split TinyImageNet', y=-0.5, fontsize=15)
plt.ylim([25, 75])
ax2.plot(list(range(1,26)), [68.25,65.75,65.75,60.25,64.75,63,59,60.25,53.75,57.25,54.5,57.5,52.75,56,57.25,56,55.25,57.5,54.75,56,54.75,56.75,59.5,54.25,58.5],marker='*', markersize=5)
ax2.plot(list(range(2,26)), [73,71.75,68.25,69.25,68.25,67,69,67.5,67.5,66.75,70.25,65.5,62.75,66,65.25,66.25,65.5,66,67.25,69.75,68.5,69.5,64.25,68.25],marker='.', markersize=5)
ax2.plot(list(range(3,26)), [72.0, 66.0, 65.0, 67.75, 68.5, 67.5,66.5,68.75, 69.0, 65.5,66.5,67.0,68.0,68.25,68.0,68.0,67.25,67.5, 66.5,68.0,62.75,59.75,71.0],marker='*', markersize=5)

plt.xticks(x_ind,x_lab,fontsize=12)
plt.yticks(size = 12)
# plt.legend(bbox_to_anchor=(1,0.48),fontsize=13)
plt.tight_layout()
plt.subplots_adjust(top=0.85, bottom=0.3)
fig.legend(bbox_to_anchor=(0.98,1),fontsize=12,ncol=3)
plt.savefig('acc.pdf') #,bbox_inches='tight'
plt.show()