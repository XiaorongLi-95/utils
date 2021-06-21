import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import json
import numpy as np


def plot(ename, exception, tasks):
    dataname = ename + '.json'
    with open(dataname, 'r') as f:
        res = json.load(f)

    avg_res = {}
    for method in res.keys():
        avg_res.update({method: avg(res[method])})

    fig = plt.figure(figsize=(28, 18))
    ax = fig.add_subplot(1, 1, 1)
    fmt = '%.0f%%'
    yticks = ticker.FormatStrFormatter(fmt)
    ax.yaxis.set_major_formatter(yticks)
    ax.tick_params(which='both', labelsize=50)
    # ax.set_xticks(range(1, tasks + 1))
    if tasks == 10:
        x_major_locator = plt.MultipleLocator(2)
    elif tasks == 20:
        x_major_locator = plt.MultipleLocator(4)
    else:
        x_major_locator = plt.MultipleLocator(5)
    ax.xaxis.set_major_locator(x_major_locator)
    fig_legends = []
    for method, avg_acc in avg_res.items():
        if method == exception:
            continue
        style = get_style(method)
        fig_legends.append(style['legend'])
        x = range(1, len(avg_acc) + 1)
        ax.plot(
            x, avg_acc,
            label=style['legend'],
            linestyle=style['linestyle'],
            linewidth=style['width'],
            color=style['color'],
            marker="d",
            markersize=19
        )
        plt.draw()

    plt.xlabel('Task', fontsize=50, labelpad=25)
    plt.ylabel('ACC', fontsize=50)
    plt.xlim((0.5, tasks+0.5))

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.24, top=0.99)
    fig.legend(
        loc='lower center', ncol=6, bbox_to_anchor=(0.5, -0.013),
        fontsize=45, frameon=True, labelspacing=0.3, handlelength=1.0,
        handletextpad=0.4
    )
    figname = ename + '-' + exception + '.pdf'
    plt.savefig(figname)
    figname = ename + '-' + exception + '.png'
    plt.savefig(figname)


def avg(method):
    avg = []
    for _, acc in method.items():
        avg.append(np.mean(acc))
    return avg


def get_style(name):
    style = {
        'EWC': {'linestyle': ':', 'color': 'lime', 'legend': 'EWC', 'width': 8},
        'MAS': {'linestyle': ':', 'color': 'black', 'legend': 'MAS', 'width': 8},
        'MUC_MAS': {'linestyle': ':', 'color': 'peru', 'legend': 'MUC_MAS', 'width': 8},
        'InstAParam': {'linestyle': ':', 'color': 'peru', 'legend': 'InstAParam', 'width': 8},
        'SI': {'linestyle': ':', 'color': 'blue', 'legend': 'SI', 'width': 8},
        'LwF': {'linestyle': ':', 'color': 'cyan', 'legend': 'LwF', 'width': 8},
        'GD': {'linestyle': ':', 'color': 'darkorange', 'legend': 'GD', 'width': 8},
        'GD+WILD': {'linestyle': ':', 'color': 'yellowgreen', 'legend': 'GD+WILD', 'width': 8},
        'GEM': {'linestyle': ':', 'color': 'gold', 'legend': 'GEM', 'width': 8},
        'A-GEM': {'linestyle': ':', 'color': 'steelblue', 'legend': 'A-GEM', 'width': 8},
        'MEGA': {'linestyle': ':', 'color': 'purple', 'legend': 'MEGA', 'width': 8},
        'DFD': {'linestyle': (0, ()), 'color': 'red', 'legend': 'DFD', 'width': 8},
        'Ours': {'linestyle': (0, ()), 'color': 'red', 'legend': 'Ours', 'width': 8}
    }
    return style[name]


if __name__ == '__main__':
    plot('cifar100-10', 'Ours', 10)
    # plot('cifar100-10', 'DFD', 10)

    # plot('cifar100-20', 'Ours', 20)
    # plot('cifar100-20', 'DFD', 20)

    plot('tiny25', 'Ours', 25)
    # plot('tiny25', 'DFD', 25)
