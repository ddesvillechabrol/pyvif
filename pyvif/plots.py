# -*- coding: utf-8 -*-

"""Plot toolbox"""

import matplotlib.pyplot as plt

from pyvif.config import COLOR, BACKGROUND


def init_plot(title="", xlabel="", ylabel="", log=False):
    """ Init a matplotlib environment to create plot.

    :param str title: title plot.
    :param str xlabel: x label.
    :param str ylabel: y label.

    return figure and ax object.
    """
    fig = plt.figure(figsize=(10, 7.5))
    ax = plt.subplot(111)
    fig.patch.set_facecolor(BACKGROUND)
    ax.patch.set_facecolor(BACKGROUND)

    # remove top and right frame lines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    if log is True:
        ax.set_yscale('log')

    # increase label font size
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.title(title, fontsize=18)
    return fig, ax


def plot_histogram(data, title, xlabel, ylabel, filename=None, bins=100,
                   log=False):
    """ Plot histogram.
    """
    # init plot
    fig, _ = init_plot(title, xlabel, ylabel, log=log)

    plt.hist(data, bins=bins, color=COLOR)
    return generate_plot(filename, fig)

def generate_plot(filename, fig):
    if filename:
        plt.savefig(filename, bbox_inches="tight",
                    facecolor=fig.get_facecolor(), edgecolor='none')
        return filename
    plt.show()
