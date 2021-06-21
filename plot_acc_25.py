import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)
plt.figure(figsize=(5,3))
x_ind = [2, 4, 6, 8, 10]
x_lab = [r'$\mathcal{T}_2$', r'$\mathcal{T}_4$', r'$\mathcal{T}_6$', r'$\mathcal{T}_8$', r'$\mathcal{T}_{{10}}$']
# set_xlabel(r'$\mathcal{T}',fontsize=1)
# fig, axs = plt.subplots(9,1)
# fig.subplots_adjust(hspace=0)
plt.xlabel('Task',fontsize=12)
plt.ylabel('Accuracy',fontsize=12)
plt.ylim([50, 95])
plt.plot([1,2,3,4,5,6,7,8,9,10], [89.1,82.0,84.6,83.6,85.1,84.1,82.7,82.2,82.4,84.2], label=r'$\mathcal{T}_1$', marker='*', markersize=5)
plt.plot([2,3,4,5,6,7,8,9,10], [80.5,79.2,79.1,80.9,80.6,78.3,77.6,81,80.2], label=r'$\mathcal{T}_2$', marker='.', markersize=5)
plt.plot([3,4,5,6,7,8,9,10], [84.2,74.2,76.3,74.6,73.4,74.7,76.5,76.3], label=r'$\mathcal{T}_3$', marker='*', markersize=5)

plt.xticks(x_ind,x_lab,fontsize=10)
plt.legend(bbox_to_anchor=(1,0.48),fontsize=11)
plt.savefig('loss.pdf',bbox_inches='tight')
plt.show()