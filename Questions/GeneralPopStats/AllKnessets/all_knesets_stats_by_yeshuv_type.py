from enum import Enum
from Parse.data_classes import ResultKnesset, ThresholdsResultKnesset
import pandas as pd
from matplotlib import pyplot as plt





_BIG_YESHUV_INDEX = ['50-100', '20-50', '10-20', '5-10', '2-5']
_SMALL_YESHUV_INDEX = ['מושב', 'מושב שיתופי', 'קיבוץ', 'כפר יהודי',
                       'ישוב קהילתי',
                       'כפר לא יהודי', 'שבט בדווי']
_HUGE_YESHUV_INDEX = ['500+ (םילשורי)', '200-500', '100-200']


class YeshuvType(Enum):
    Big = 1
    Others = 2
    Huge = 3


class PlotType(Enum):
    Vote_Percent = 1
    Error = 2
    AvgBzb = 3
    Bzb = 4
    Vote_Percent_Box_Plot = 5

BIG_YESHUV_LIST = ["150", "160", '170', '180', '190', "250" ,"260" ,'270' ,'280','290']
HUGE_YESHUV_LIST = ["120", "130", "140"]
OTHER_YESHUV_LIST = ["310", "320", '330', '350', '370', '450', '460']

BIG_NON_JEW_YESHUV_LIST = BIG_YESHUV_LIST[:5]
BIG_JEW_YESHUV_LIST = BIG_YESHUV_LIST[5:]

def get_yeshuv_list(yt :YeshuvType, is_jew : bool ):
    if yt == YeshuvType.Others:
        return OTHER_YESHUV_LIST
    elif yt == YeshuvType.Huge:
        return HUGE_YESHUV_LIST
    elif yt == YeshuvType.Big:
        if is_jew:
            return BIG_JEW_YESHUV_LIST
        else:
            return BIG_NON_JEW_YESHUV_LIST



def _reverse_list_of_strings(strings):
    return [x[::-1] for x in strings]

from Questions.GeneralPopStats.AllKnessets import plot_style_helper
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


def all_knessets_bar_graph(list_series: pd.Series, pt: PlotType,
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
    ser_vote = gather_data_by_yeshuve_type_group_by(kneset_data, PlotType.Vote_Percent)

    # _all_knessets_bar_graph(ser_vote, PlotType.Vote_Percent_Box_Plot,
    #                         YeshuvType.Huge)
    all_knessets_bar_graph(ser_vote, PlotType.Vote_Percent_Box_Plot,
                            YeshuvType.Big)

    all_knessets_bar_graph(ser_vote, PlotType.Vote_Percent_Box_Plot,
                            YeshuvType.Others)

    # _all_knessets_bar_graph(ser_error, PlotType.Error,
    #                         YeshuvType.Huge)
    #
    # _all_knessets_bar_graph(ser_error, PlotType.Error,
    #                         YeshuvType.Big)
    #
    # _all_knessets_bar_graph(ser_error, PlotType.Error,
    #                         YeshuvType.Others)
    #
    #
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

    # _multi_plt_graph(bzb)


def stats_grpd_by_yeshuv_type_by_threshold(results : ThresholdsResultKnesset):
    from constants import THRESHOLD_LIST
    for threshold in THRESHOLD_LIST:
        result_per_threshold = results.get_threshold_kneset_dict(threshold)
        stats_grpd_by_yeshuv_type(result_per_threshold)
