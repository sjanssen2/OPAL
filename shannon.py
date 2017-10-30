#!/usr/bin/env python

import math
import numpy as np
from collections import OrderedDict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from utils import constants as c


class Shannon:
    def __init__(self):
        pass


def create_colors_list():
    colors_list = []
    for color in plt.cm.tab10(np.linspace(0, 1, 10))[:-1]:
        colors_list.append(tuple(color))
    colors_list.append("black")
    for color in plt.cm.Set2(np.linspace(0, 1, 8)):
        colors_list.append(tuple(color))
    for color in plt.cm.Set3(np.linspace(0, 1, 12)):
        colors_list.append(tuple(color))
    return colors_list


def plot_shannon(rank_to_shannon_list, labels, output_dir):
    colors_list = create_colors_list()

    fig, axs = plt.subplots(figsize=(6, 5))

    # force axis to be from 0 to 100%
    axs.set_ylim([0.0, 1.0])

    x = list(range(1, len(c.ALL_RANKS) + 1))

    i = 0
    for rank_to_shannon in rank_to_shannon_list:
        y = [rank_to_shannon[rank].equitability for rank in c.ALL_RANKS]
        axs.plot(x, y, color=colors_list[i], marker='o', markersize=10)
        i += 1

    axs.set_xticklabels([''] + c.ALL_RANKS)
    plt.setp(axs.get_xticklabels(), fontsize=9, rotation=25)

    axs.set_ylabel('Shannon equitability')

    lgd = plt.legend(labels, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., handlelength=0, frameon=False)
    fig.savefig(output_dir + '/plot_shannon.pdf', dpi=100, format='pdf', bbox_extra_artists=(lgd,), bbox_inches='tight')


# Compute the Shannon index (diversity and equitability) with log base e
# The higher the index, the more equally distributed the taxa are
def compute_shannon_index(rank_to_taxid_to_percentage):
    rank_to_shannon = OrderedDict()
    for rank in c.ALL_RANKS:
        rank_to_shannon[rank] = Shannon()
        rank_to_shannon[rank].diversity = .0
        rank_to_shannon[rank].equitability = .0
        if rank not in rank_to_taxid_to_percentage:
            continue
        for taxid in rank_to_taxid_to_percentage[rank]:
            percentage = rank_to_taxid_to_percentage[rank][taxid] / 100.0
            if percentage > .0:
                rank_to_shannon[rank].diversity -= percentage * math.log(percentage)
        if len(rank_to_taxid_to_percentage[rank]) > 1:
            rank_to_shannon[rank].equitability = rank_to_shannon[rank].diversity / math.log(len(rank_to_taxid_to_percentage[rank]))
    return rank_to_shannon