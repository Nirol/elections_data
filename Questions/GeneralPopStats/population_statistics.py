import matplotlib.pyplot as plt

from numpy import nanstd
from scipy.stats import pearsonr, kendalltau

import pandas as pd
from Parse.data_classes import ResultKnesset, PopulationStats, PopVars
from Questions.GeneralPopStats.AllKnessets import plot_style_helper
from Questions.GeneralPopStats.AllKnessets.all_knesets_stats_by_yeshuv_type import \
    YeshuvType, PlotType, _BIG_YESHUV_INDEX, _SMALL_YESHUV_INDEX, \
    _reverse_list_of_strings

from constants import KNESSETS_LIST


def graph_general_stat(x, bzb_per_kalfi_list, num_kalfi_list, unique_yeshuv,
                       voters_list):

    fig, axs = plt.subplots(2, 2, gridspec_kw={'hspace': 0.35, 'wspace': 0.4})
    fig.suptitle('General Knesset Elections Info', va='top')

    color = 'tab:red'
    # ax1.set_ylabel('BZB', color=color)
    axs[0, 0].semilogy(x, bzb_per_kalfi_list, 'r--', label="bzb")
    axs[0, 0].set_title('BZB')
    # ax1.tick_params(axis='y', labelcolor=color)



    color = 'tab:blue'
    # ax2.set_ylabel('Voters', color=color)
    axs[0, 1].semilogy(x, voters_list, 'c-.')
    axs[0, 1].set_title('Voters')
    # ax2.tick_params(axis='y', labelcolor=color)


    color = 'tab:pink'
    # ax3.set_ylabel('Kalfi\'s', color=color)
    axs[1, 0].plot(x, num_kalfi_list, 'm-')
    # ax3.tick_params(axis='y', labelcolor=color)
    axs[1, 0].set_title('Kalfi\'s')
    axs[1, 0].set(xlabel='Kneset')
    # axs[1, 0].tick_params(axis='y', labelcolor=color, labelsize=6)
    color = 'tab:green'
    # ax4.set_ylabel('Yeshuvim\'s', color=color)
    axs[1, 1].plot(x, unique_yeshuv, 'g:')
    # ax4.tick_params(axis='y', labelcolor=color)
    # ax4.set_xlabel('Kneset')
    axs[1, 1].set_title('Yeshuvim\'s')
    # fig.tight_layout()
    axs[1, 1].set(xlabel='Kneset')
    # axs[1, 1].tick_params(axis='y', labelcolor=color, labelsize=6)
    plt.show()


def general_over_knesets_stats(kneset_data: ResultKnesset):
    x = ["18", "19", "20", "21", "22"]
    avg_bzb_per_kalfi_list = kneset_data.get_var_per_kneset(PopVars.AvgBzb)
    vote_percent_list = kneset_data.get_var_per_kneset(PopVars.VotePercent)
    # graph_avg_bzb_vote_percent(x, avg_bzb_per_kalfi_list, vote_percent_list)

    bzb_per_kalfi_list = kneset_data.get_var_per_kneset(PopVars.Bzb)
    num_kalfi_list = kneset_data.get_var_per_kneset(PopVars.Num_Kalfi)
    unique_yeshuv = kneset_data.get_var_per_kneset(PopVars.Unq_Yeshuv)
    voters_list = kneset_data.get_var_per_kneset(PopVars.Voters)

    # graph_general_stat(x, bzb_per_kalfi_list, num_kalfi_list, unique_yeshuv,
    #                    voters_list)







def graph_avg_bzb_vote_percent(x, avg_bzb_per_kalfi_list, vote_percent_list):
    df = pd.DataFrame({'Kneset': x,
                       'Avg_bzb': avg_bzb_per_kalfi_list,
                       'Vote_percent': vote_percent_list})

    fig, ax1 = plt.subplots()
    fig.suptitle('Average BZB per Kalfi and Vote %', y = 1)
    color = 'tab:red'
    ax1.set_xlabel('Kneset')
    ax1.set_ylabel('Avg BZB per Kalfi', color=color, rotation='horizontal',
                   horizontalalignment='left', fontsize='small',
                   position=(0, 0.465))
    ax1.plot(x, avg_bzb_per_kalfi_list, 'r--', label="bzb")
    ax1.tick_params(axis='y', labelcolor=color, labelsize=10)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Vote %', color=color, rotation='horizontal',
                   fontsize='small')
    ax2.plot(x, vote_percent_list, 'c-.')
    ax2.tick_params(axis='y', labelcolor=color, labelsize=10)


    #add grids
    fig.tight_layout()
    plt.grid(True, axis="both", linestyle='--', linewidth=1, which='both')

    font = {'family': 'serif',
            'color': 'royalblue',
            'weight': 'semibold',
            'size': 9
            }
    # add value points for ax2 (vote percent )
    ax2.text("18", vote_percent_list[0] - 0.0025,
             str(round(vote_percent_list[0], 2)) + '%', ha="left",
             fontdict=font)

    ax2.text("19", vote_percent_list[1],
             str(round(vote_percent_list[1], 2)) + '%', ha="right",
             fontdict=font)

    ax2.text("20", vote_percent_list[2],
             str(round(vote_percent_list[2], 2)) + '%', ha="center",
             fontdict=font)

    ax2.text("21", vote_percent_list[3] - 0.0023,
             str(round(vote_percent_list[3], 2)) + '%', ha="center",
             fontdict=font)

    ax2.text("22", vote_percent_list[4] + 0.001,
             str(round(vote_percent_list[4], 2)) + '%', ha="center",
             fontdict=font)
    plt.show()


def scatter_plot_population(kneset_df: pd.DataFrame):
    x = kneset_df['BZB']
    y = kneset_df['vote_percent']
    plt.scatter(x, y, alpha=0.5)
    plt.title('vote percent by BZB')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def stats_population_kneset_df(kneset_df):
    num_kalfis_total = len(kneset_df['SN'])
    num_unique_yeshuvim = len(set(kneset_df['SN']))
    total_bzb = kneset_df['BZB'].sum()
    total_voters = kneset_df['Voters'].sum()
    pearson, tau, vote_percent_std = calculate_bzb_vote_percent_pearson(kneset_df['BZB'],
                                                      kneset_df[
                                                          'vote_percent'])
    filtered_population_stats = PopulationStats(num_kalfis_total,
                                                num_unique_yeshuvim, total_bzb,
                                                total_voters, pearson, tau, vote_percent_std)
    return filtered_population_stats


def calculate_bzb_vote_percent_pearson(bzb_col, vote_percent_col):
    pearson_res = pearsonr(bzb_col,
                           vote_percent_col)
    vote_percent_std = nanstd(vote_percent_col)
    tau, p_value = kendalltau(bzb_col, vote_percent_col)
    return pearson_res, [tau, p_value],vote_percent_std







def gather_data_by_yeshuve_type_group_by(kneset_data, yt: YeshuvType):
    dict_final = {}
    from main import KNESSETS_LIST
    for kneset_num in KNESSETS_LIST:
        df = kneset_data.get_kneset_data(kneset_num)
        dict_of_companies = dict(tuple(df.groupby("Yeshuv_Type")))
        dict_final[kneset_num] = dict_of_companies
    return dict_final







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


    box_plot_dict = df.boxplot(rot=0, ax=axs[i, j], return_type='dict', patch_artist=True, vert=1, whis=1.5)
    axs[i, j].yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                   alpha=0.5)
    count_outliers(knesset_num,box_plot_dict)
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
        fig, axs = plt.subplots(2, 3, figsize=(12, 8),sharex='col',sharey='row',
                                gridspec_kw={'hspace': 0.15, 'wspace': 0.15})
    elif yt == YeshuvType.Others:
        fig, axs = plt.subplots(3, 2, sharex='col', sharey='row',
                                figsize=(19, 10),
                                gridspec_kw={'hspace': 0.18, 'wspace': 0.10})
    _set_bar_graph_titles_box_plot(fig, axs)

    for knesset_num in KNESSETS_LIST:
        dict = dict_df[knesset_num]

        # bars_non_jews = pd.DataFrame({'500+ (םילשורי)': dict["120"]["vote_percent"], '200-500' : dict["130"]["vote_percent"]
        #                                 ,'100-200': dict["140"]["vote_percent"]})
        index_list_rev = _SMALL_YESHUV_INDEX
        index_list = _reverse_list_of_strings(index_list_rev)
        df_jews = pd.DataFrame({index_list[0]: dict["310"]["vote_percent"],index_list[1] : dict["320"]["vote_percent"]
                                ,index_list[2]: dict["330"]["vote_percent"],index_list[3]: dict["350"]["vote_percent"],
                                index_list[4]: dict["370"]["vote_percent"], index_list[5]: dict["450"]["vote_percent"],
                                index_list[6]: dict["460"]["vote_percent"]
                                })

        # bars_non_jews = pd.DataFrame({'50-100': dict["250"]["vote_percent"], '20-50' : dict["260"]["vote_percent"]
        #                                 ,'10-20': dict["270"]["vote_percent"],'5-10': dict["280"]["vote_percent"],
        #                                 '2-5': dict["290"]["vote_percent"]
        #                                 })
        # df_jews = pd.DataFrame({'50-100': dict["150"]["vote_percent"], '20-50' : dict["160"]["vote_percent"]
        #                         ,'10-20': dict["170"]["vote_percent"],'5-10': dict["180"]["vote_percent"],
        #                         '2-5': dict["190"]["vote_percent"]
        #                         })

        print("319:{}".format(len(dict["310"]["vote_percent"])))
        print("20-50 arab:{}".format(len(dict["320"]["vote_percent"])))
        print("10-20 arab:{}".format(len(dict["330"]["vote_percent"])))
        print("5-10 arab:{}".format(len(dict["350"]["vote_percent"])))
        print("2-5 arab :{}".format(len(dict["370"]["vote_percent"])))
        print("2-5 arab :{}".format(len(dict["450"]["vote_percent"])))
        print("2-5 arab :{}".format(len(dict["460"]["vote_percent"])))

        _add_to_plot(knesset_num, df_jews, axs, pt, yt)

    plt.show()








def stats_box_plot(results):
   dict_df  = gather_data_by_yeshuve_type_group_by(results, YeshuvType.Others)

   all_knessets_box_plot_graph(dict_df, PlotType.Vote_Percent_Box_Plot,
                          YeshuvType.Big)
