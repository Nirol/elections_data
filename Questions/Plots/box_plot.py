import pandas as pd
from matplotlib import pyplot as plt

from Questions.GeneralPopStats.AllKnessets.all_knesets_stats_by_yeshuv_type import \
    PlotType, YeshuvType, _SMALL_YESHUV_INDEX, _reverse_list_of_strings
from constants import KNESSETS_LIST
from Questions.GeneralPopStats.AllKnessets import plot_style_helper
def _set_graph_design_box_plot(ax, knesset_num, pt: PlotType, yt: YeshuvType):
    ax.set_alpha(0.8)
    font = {'family': 'serif',
            'color': 'black',
            'weight': 'semibold'
            }
    ax.set_title(knesset_num, fontdict=font)


def count_outliers(knesset_num, dict):
    print("Printing outliers count for Kneseet:{}".format(knesset_num))
    fliers = dict['fliers']

    for j in range(len(fliers)):
        # the y and x positions of the fliers
        yfliers = dict['fliers'][j].get_ydata()
        xfliers = dict['fliers'][j].get_xdata()
        # the unique locations of fliers in y
        ufliers = set(yfliers)
        print(len(yfliers))

def _add_to_plot(knesset_num, df: pd.DataFrame, axs, pt: PlotType,
                 yt: YeshuvType):
    i, j = plot_style_helper.get_plot_idx_by_knesset(knesset_num, yt)

    box_plot_dict = df.boxplot(rot=0, ax=axs[i, j], return_type='dict',
                               patch_artist=True, vert=1, whis=1.5)
    axs[i, j].yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                         alpha=0.5)
    count_outliers(knesset_num, box_plot_dict)
    for flier in box_plot_dict['fliers']:
        flier.set(marker='o', color='rosybrown', alpha=0.1)

    for median in box_plot_dict['medians']:
        median.set(color='rosybrown', linewidth=1.8)

    for cap in box_plot_dict['caps']:
        cap.set(color='rosybrown', linewidth=2)

    for whisker in box_plot_dict['whiskers']:
        whisker.set(color='silver', linewidth=1.9)

    for box in box_plot_dict['boxes']:
        # change outline color
        box.set(color='silver', linewidth=1.6)

    _set_graph_design_box_plot(axs[i, j], knesset_num, pt, yt)


def _set_bar_graph_titles_box_plot(fig, axs):
    fig.suptitle('Voting % Box Plot By Yeshuv Size (Per Knesset)')
    for ax in axs.flat:
        ax.set(xlabel="Yeshuv Size (In Thousands)", ylabel='Vote %')
    for ax in axs.flat:
        ax.label_outer()

def all_knessets_box_plot_graph(dict_df, pt: PlotType,
                                yt: YeshuvType):
    fig, axs = None, None
    if yt == YeshuvType.Big or yt == YeshuvType.Huge:
        fig, axs = plt.subplots(2, 3, figsize=(12, 8), sharex='col',
                                sharey='row',
                                gridspec_kw={'hspace': 0.15, 'wspace': 0.15})
    elif yt == YeshuvType.Others:
        fig, axs = plt.subplots(3, 2, sharex='col', sharey='row',
                                figsize=(19, 10),
                                gridspec_kw={'hspace': 0.18, 'wspace': 0.10})
    _set_bar_graph_titles_box_plot(fig, axs)

    for knesset_num in KNESSETS_LIST:
        dict = dict_df[knesset_num]
        index_list_rev = _SMALL_YESHUV_INDEX
        index_list = _reverse_list_of_strings(index_list_rev)
        df_jews = pd.DataFrame({index_list[0]: dict["310"]["vote_percent"],
                                index_list[1]: dict["320"]["vote_percent"]
                                   ,
                                index_list[2]: dict["330"]["vote_percent"],
                                index_list[3]: dict["350"]["vote_percent"],
                                index_list[4]: dict["370"]["vote_percent"],
                                index_list[5]: dict["450"]["vote_percent"],
                                index_list[6]: dict["460"]["vote_percent"]
                                })
        print("319:{}".format(len(dict["310"]["vote_percent"])))
        print("20-50 arab:{}".format(len(dict["320"]["vote_percent"])))
        print("10-20 arab:{}".format(len(dict["330"]["vote_percent"])))
        print("5-10 arab:{}".format(len(dict["350"]["vote_percent"])))
        print("2-5 arab :{}".format(len(dict["370"]["vote_percent"])))
        print("2-5 arab :{}".format(len(dict["450"]["vote_percent"])))
        print("2-5 arab :{}".format(len(dict["460"]["vote_percent"])))

        _add_to_plot(knesset_num, df_jews, axs, pt, yt)
    plt.show()