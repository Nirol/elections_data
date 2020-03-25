from src.data.data_classes import ResultKnesset, ThresholdsResultKnesset
import pandas as pd
from matplotlib import pyplot as plt

from plot_helper import HUGE_YESHUV_LIST, OTHER_YESHUV_LIST, \
    BIG_NON_JEW_YESHUV_LIST, BIG_JEW_YESHUV_LIST, YeshuvType, PlotType
from single_knesset.plot_single_knesset import single_knesset_all_yeshuv_types
from single_knesset.bzb_pie import _multi_plt_graph


def get_yeshuv_list(yt : YeshuvType, is_jew : bool):
    if yt == YeshuvType.Others:
        return OTHER_YESHUV_LIST
    elif yt == YeshuvType.Huge:
        return HUGE_YESHUV_LIST
    elif yt == YeshuvType.Big:
        if is_jew:
            return BIG_JEW_YESHUV_LIST
        else:
            return BIG_NON_JEW_YESHUV_LIST



def reverse_list_of_strings(strings):
    return [x[::-1] for x in strings]


import plot_style_helper


def _add_to_plot(fig, knesset_num, df: pd.DataFrame, axs, pt: PlotType,
                 yt: YeshuvType):
    i, j = plot_style_helper.get_plot_idx_by_knesset(knesset_num, yt)
    if yt == YeshuvType.Big:
        a = df.plot.bar(rot=0, ax=axs[i, j])
        fig.legend([a],  # The line objects
                   labels=["Jews", "Non Jews"],  # The labels for each line
                   loc="center right",  # Position of legend
                   borderaxespad=0.1,  # Small spacing around legend box
                   title=""
                   )
    elif yt == YeshuvType.Others or YeshuvType.Huge:
        print("i,j={}{}".format(i,j))
        df.plot.bar(rot=0, ax=axs[i, j], color='chocolate')

    plot_style_helper._set_graph_design(axs[i, j], knesset_num, pt, yt)
    plot_style_helper._add_column_text_labels(axs[i, j], df, pt, yt)


def _all_knessets_bar_graph(list_series: pd.Series, pt: PlotType,
                           yt: YeshuvType):
    fig, axs = None, None
    if yt == YeshuvType.Big or yt == YeshuvType.Huge:
        fig, axs = plt.subplots(2, 3, figsize=(12, 8),
                                gridspec_kw={'hspace': 0.15, 'wspace': 0.15})
    elif yt == YeshuvType.Others:
        fig, axs = plt.subplots(3, 2, sharex='col', sharey='row',
                                figsize=(15, 8),
                                gridspec_kw={'hspace': 0.18, 'wspace': 0.10})
    plot_style_helper._set_bar_graph_titles(fig, axs, pt, yt)

    for series_key in list_series.keys():
        series = list_series[series_key]
        df = plot_style_helper.create_df_from_series_per_knesset(series, yt)
        knesset_num = series_key
        _add_to_plot(fig, knesset_num, df, axs, pt, yt)
    plt.show()



def _append_to_list(list_to_append, to_divide,
                    divide_by, is_percent):
    vote_percent_per_yeshuv_type = to_divide.divide(divide_by,
                                                    fill_value=0)
    if is_percent:
        into_percent_representation = vote_percent_per_yeshuv_type.multiply(
            100)
        list_to_append.append(
            into_percent_representation)
    else:
        list_to_append.append(
            vote_percent_per_yeshuv_type)


def _select_groupd_by_data_(df, plot_type_list, pt : PlotType):
    is_percent = True
    if pt == PlotType.AvgBzb:
        is_percent = False
        bzb_grpd = df.groupby("Yeshuv_Type")['BZB'].sum()
        kalfi_count = df.groupby("Yeshuv_Type")['Kalfi_Num'].count()
        _append_to_list(plot_type_list, bzb_grpd, kalfi_count, is_percent)
    elif pt == PlotType.Vote_Percent:
        voters_grpd = df.groupby("Yeshuv_Type")['Voters'].sum()
        bzb_grpd = df.groupby("Yeshuv_Type")['BZB'].sum()
        _append_to_list(plot_type_list, voters_grpd,
                        bzb_grpd, is_percent)
    elif pt == PlotType.Error:
        voters_grpd = df.groupby("Yeshuv_Type")['Voters'].sum()
        error_grpd = df.groupby("Yeshuv_Type")['Error_Voters'].sum()
        _append_to_list(plot_type_list, error_grpd,
                        voters_grpd, is_percent)
    elif pt == PlotType.Bzb:
        bzb_grpd = df.groupby("Yeshuv_Type")['BZB'].sum()
        plot_type_list.append(bzb_grpd)


def gather_data_by_yeshuve_type_group_by(kneset_data : pd.DataFrame, pt : PlotType):
    plot_type_series_list = []
    from constants import KNESSETS_LIST
    for kneset_num in KNESSETS_LIST:
        df = kneset_data.get_kneset_data(kneset_num)
        _select_groupd_by_data_(df,plot_type_series_list, pt)

    ser_plot = pd.Series(plot_type_series_list,
                         index=KNESSETS_LIST)
    return ser_plot




def stats_grpd_by_yeshuv_type(kneset_data: ResultKnesset):
    # ser_vote = gather_data_by_yeshuve_type_group_by(kneset_data, PlotType.Vote_Percent)

    # _all_knessets_bar_graph(ser_vote, PlotType.Vote_Percent_Box_Plot,
    #                         YeshuvType.Huge)
    # all_knessets_bar_graph(ser_vote, PlotType.Vote_Percent_Box_Plot,
    #                        YeshuvType.Big)
    #
    # all_knessets_bar_graph(ser_vote, PlotType.Vote_Percent_Box_Plot,
    #                        YeshuvType.Others)

    # _all_knessets_bar_graph(ser_error, PlotType.Error,
    #                         YeshuvType.Huge)
    #
    # _all_knessets_bar_graph(ser_error, PlotType.Error,
    #                         YeshuvType.Big)
    #
    # _all_knessets_bar_graph(ser_error, PlotType.Error,
    #                         YeshuvType.Others)
    #

    avg_bzb_groupd_by = gather_data_by_yeshuve_type_group_by(kneset_data, PlotType.AvgBzb)

    single_knesset_all_yeshuv_types(avg_bzb_groupd_by["22"], PlotType.AvgBzb)
    # _all_knessets_bar_graph(avg_bzb_groupd_by, PlotType.AvgBzb,
    #                         YeshuvType.Huge)
    #
    # _all_knessets_bar_graph(avg_bzb_groupd_by, PlotType.AvgBzb,
    #                         YeshuvType.Big)
    #
    # _all_knessets_bar_graph(avg_bzb_groupd_by, PlotType.AvgBzb,
    #                         YeshuvType.Others)

    # _pie_graph(bzb, PlotType.Bzb,
    #                        YeshuvType.Big)

    bzb = gather_data_by_yeshuve_type_group_by(kneset_data,
                                                    PlotType.Bzb)
    #plot pie bzb graph
    _multi_plt_graph(bzb)


def stats_grpd_by_yeshuv_type_by_threshold(results : ThresholdsResultKnesset):
    from constants import THRESHOLD_LIST
    for threshold in THRESHOLD_LIST:
        result_per_threshold = results.get_threshold_kneset_dict(threshold)
        stats_grpd_by_yeshuv_type(result_per_threshold)
