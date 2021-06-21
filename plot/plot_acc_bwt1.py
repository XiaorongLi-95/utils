import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import json
import numpy as np


def plot():
    names = ['cifar100-20.json']  # 'cifar100-20.json', ,  'tiny25.json'
    title = '20-split CIFAR-100'
    tx = 0.4
    ty = 0.16
    fig = plt.figure(figsize=(26, 15))
    for i, dataname in enumerate(names):
        ax = fig.add_subplot(1, 2, i+1)
        with open(dataname, 'r') as f:
            res = json.load(f)

        avg_res = {}
        for method in res.keys():
            avg_res.update({method: avg(res[method])})
        fmt = '%.0f%%'
        yticks = ticker.FormatStrFormatter(fmt)
        ax.yaxis.set_major_formatter(yticks)
        ax.tick_params(which='both', labelsize=50)
        # ax.set_xticks(range(1, tasks + 1))
        if 'cifar100-10' in dataname:
            x_major_locator = plt.MultipleLocator(2)
            tasks = 10
        # TODO
        elif 'cifar100-20' in dataname:
            x_major_locator = plt.MultipleLocator(4)
            tasks = 20
        else:
            x_major_locator = plt.MultipleLocator(5)
            tasks = 25
        ax.xaxis.set_major_locator(x_major_locator)
        fig_legends = []
        for method, avg_acc in avg_res.items():
            style = get_style(method)
            fig_legends.append(style['legend'])
            x = range(1, len(avg_acc) + 1)
            if i == 0:
                ax.plot(
                    x, avg_acc,
                    label=style['legend'],
                    linestyle=style['linestyle'],
                    linewidth=style['width'],
                    color=style['color'],
                    # marker="d",
                    # markersize=10
                )
            else:
                ax.plot(
                    x, avg_acc,
                    linestyle=style['linestyle'],
                    linewidth=style['width'],
                    color=style['color'],
                    # marker="d",
                    # markersize=10
                )

            plt.draw()
        plt.figtext(tx, ty, title, fontsize=50)
        # plt.title('20-split CIFAR-100', y=-5, fontsize=50)
        plt.xlabel('Task', fontsize=50)
        if i == 0:
            plt.ylabel('ACC', fontsize=50)
        plt.xlim((0.5, tasks+0.5))

    start = 1
    for j, dataname in enumerate(names, start=start):
        ax = fig.add_subplot(1, 2, j+1)
        i = j - start
        fmt = '%.0f%%'
        yticks = ticker.FormatStrFormatter(fmt)
        ax.yaxis.set_major_formatter(yticks)
        ax.tick_params(which='both', labelsize=50)
        # ax.set_xticks(range(1, tasks + 1))
        if 'cifar100-10' in dataname:
            x_major_locator = plt.MultipleLocator(2)
            tasks = 10
        # TODO
        elif 'cifar100-20' in dataname:
            x_major_locator = plt.MultipleLocator(4)
            tasks = 20
        else:
            x_major_locator = plt.MultipleLocator(5)
            tasks = 25
        ax.xaxis.set_major_locator(x_major_locator)
        fig_legends = []

        with open(dataname, 'r') as f:
            res = json.load(f)

        bwt_res = {}
        for method in res.keys():
            bwt_res.update({method: get_bwt(res[method], tasks, method)})

        for method, bwt in bwt_res.items():
            style = get_style(method)
            fig_legends.append(style['legend'])
            x = range(2, len(bwt) + 2)
            ax.plot(
                x, bwt,
                linestyle=style['linestyle'],
                linewidth=style['width'],
                color=style['color'],
                # marker="d",
                # markersize=10
            )

            plt.draw()
        # plt.figtext(tx[j], ty[j], title[j], fontsize=50)
        plt.xlabel('Task', fontsize=50)
        if i == 0:
            plt.ylabel('BWT', fontsize=50)
        plt.xlim((0.5, tasks+0.5))

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.3, top=0.99, hspace=0.3)
    fig.legend(
        loc='lower center', ncol=6, bbox_to_anchor=(0.52, -0.02),
        fontsize=43, frameon=True, labelspacing=0.25, handlelength=1.0,
        handletextpad=0.4
    )
    figname = 'acc_bwt' + '.pdf'
    plt.savefig(figname)
    figname = 'acc_bwt' + '.png'
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
