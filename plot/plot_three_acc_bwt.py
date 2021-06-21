import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
import json
import numpy as np


def plot():
    names = ['cifar100-10.json', 'cifar100-20.json', 'tiny25.json']  # 'cifar100-20.json',
    title = ['(a) 10-split CIFAR-100',  
             '(b) 20-split CIFAR-100',
             '(c) 25-split TinyImageNet',
             ]
    tx = [0.36, 0.36, 0.35]
    ty = [0.7, 0.385, 0.07]
    fig = plt.figure(figsize=(32, 46))
    j = 0
    for i, dataname in enumerate(names):
        for metric in ['ACC', 'BWT']:
            j = j+1
            ax = fig.add_subplot(3, 2, j)
            # fmt = '%.0f%%'
            # yticks = ticker.FormatStrFormatter(fmt)
            # ax.yaxis.set_major_formatter(yticks)
            ax.tick_params(which='both', labelsize=50)
            # ax.set_xticks(range(1, tasks + 1))
            if 'cifar100-10' in dataname:
                x_major_locator = plt.MultipleLocator(2)
                tasks = 10
            elif 'cifar100-20' in dataname:
                x_major_locator = plt.MultipleLocator(4)
                tasks = 20
            else:
                x_major_locator = plt.MultipleLocator(5)
                tasks = 25
            ax.xaxis.set_major_locator(x_major_locator)
            with open(dataname, 'r') as f:
                res = json.load(f)
            if metric == 'ACC':
                resu = {}
                for method in res.keys():
                    resu.update({method: avg(res[method])})
                x = range(1, tasks + 1)
            else:
                resu = {}
                for method in res.keys():
                    resu.update({method: get_bwt(res[method], tasks, method)})
                x = range(2, tasks + 1)
            fig_legends = []
            for method, v in resu.items():
                style = get_style(method)
                fig_legends.append(style['legend'])
                if j == 1:
                    ax.plot(
                        x, v,
                        label=style['legend'],
                        linestyle=style['linestyle'],
                        linewidth=style['width'],
                        color=style['color'],
                        # marker="d",
                        # markersize=10
                    )
                elif j == 2:
                    ax.plot(
                        x, v,
                        # label=style['legend'],
                        linestyle=style['linestyle'],
                        linewidth=style['width'],
                        color=style['color'],
                        # marker="d",
                        # markersize=10
                    )
                else:
                    ax.plot(
                        x, v,
                        # label=style['legend'],
                        linestyle=style['linestyle'],
                        linewidth=style['width'],
                        color=style['color'],
                        # marker="d",
                        # markersize=10
                    )
                plt.draw()
            plt.xlabel('Task', fontsize=60)
            plt.ylabel('{} (%)'.format(metric), fontsize=60)
            plt.xlim((0.5, tasks+0.5))
        plt.figtext(tx[i], ty[i], title[i], fontsize=60)
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.13, top=0.99, hspace=0.3)
    fig.legend(
        loc='lower center', ncol=6, bbox_to_anchor=(0.52, 0.0),
        fontsize=53, frameon=True, labelspacing=0.25, handlelength=1.0,
        handletextpad=0.4
    )
    figname = 'three_acc_bwt' + '.pdf'
    plt.savefig(figname)
    figname = 'three_acc_bwt' + '.png'
    plt.savefig(figname)


def avg(method):
    avg = []
    for _, acc in method.items():
        avg.append(np.mean(acc))
    return avg


def get_bwt(method, tasks, approach):
    bwt = []
    for i in range(1, tasks):
        b = []
        t = 't' + str(i + 1)
        for j in range(i):
            tt = 't' + str(j+1)
            b.append(method[t][j] - method[tt][j])
        bwt.append(np.mean(b))
    # print('{}:'.format(approach))
    # print('{}\n'.format(bwt[-1]))
    return bwt


# def get_style(name):
#     wid = 5
#     style = {
#         'EWC': {'linestyle': (0, ()), 'color': 'lime', 'legend': 'EWC', 'width': wid},
#         'MAS': {'linestyle': (0, ()), 'color': 'black', 'legend': 'MAS', 'width': wid},
#         'MUC_MAS': {'linestyle': (0, ()), 'color': 'peru', 'legend': 'MUC_MAS', 'width': wid},
#         'InstAParam': {'linestyle': (0, ()), 'color': 'peru', 'legend': 'InstAParam', 'width': wid},
#         'SI': {'linestyle': (0, ()), 'color': 'blue', 'legend': 'SI', 'width': wid},
#         'LwF': {'linestyle': (0, ()), 'color': 'cyan', 'legend': 'LwF', 'width': wid},
#         'GD': {'linestyle': (0, ()), 'color': 'darkorange', 'legend': 'GD', 'width': wid},
#         'GD+WILD': {'linestyle': (0, ()), 'color': 'yellowgreen', 'legend': 'GD+WILD', 'width': wid},
#         'GEM': {'linestyle': (0, ()), 'color': 'gold', 'legend': 'GEM', 'width': wid},
#         'A-GEM': {'linestyle': (0, ()), 'color': 'steelblue', 'legend': 'A-GEM', 'width': wid},
#         'MEGA': {'linestyle': (0, ()), 'color': 'purple', 'legend': 'MEGA', 'width': wid},
#         'DFD': {'linestyle': (0, ()), 'color': 'red', 'legend': 'DFD', 'width': 9},
#         'Ours': {'linestyle': (0, ()), 'color': 'red', 'legend': 'Ours', 'width': wid}
#     }
#     return style[name]

def get_style(name):
    wid = 5
    style = {
        'EWC': {'linestyle': '--', 'color': 'teal', 'legend': 'EWC', 'width': wid},
        'MAS': {'linestyle': '--', 'color': 'black', 'legend': 'MAS', 'width': wid},
        'MUC_MAS': {'linestyle': '--', 'color': 'peru', 'legend': 'MUC_MAS', 'width': wid},
        'InstAParam': {'linestyle': '--', 'color': 'olive', 'legend': 'InstAParam', 'width': wid},
        'SI': {'linestyle': '--', 'color': 'blue', 'legend': 'SI', 'width': wid},
        'LwF': {'linestyle': '--', 'color': 'cyan', 'legend': 'LwF', 'width': wid},
        'GD': {'linestyle': '--', 'color': 'darkorange', 'legend': 'GD', 'width': wid},
        'GD+WILD': {'linestyle': '--', 'color': 'yellowgreen', 'legend': 'GD+WILD', 'width': wid},
        'GEM': {'linestyle': '--', 'color': 'gold', 'legend': 'GEM', 'width': wid},
        'A-GEM': {'linestyle': '--', 'color': 'steelblue', 'legend': 'A-GEM', 'width': wid},
        'MEGA': {'linestyle': '--', 'color': 'purple', 'legend': 'MEGA', 'width': wid},
        'DFD': {'linestyle': (0, ()), 'color': 'red', 'legend': 'DFD', 'width': 9},
        'Ours': {'linestyle': (0, ()), 'color': 'red', 'legend': 'Ours', 'width': wid}
    }
    return style[name]


if __name__ == '__main__':
    plot()
