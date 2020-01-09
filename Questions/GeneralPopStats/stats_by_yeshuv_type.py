from enum import Enum

from matplotlib.pyplot import ylim

from IO.data_classes import BzbPerKalfiResult, PopVars
import pandas as pd
from matplotlib import pyplot as plt

_BIG_YESHUV_INDEX = ['50-100', '20-50', '10-20', '5-10', '2-5']
_SMALL_YESHUV_INDEX = ['מושב', 'מושב שיתופי', 'קיבוץ', 'כפר יהודי',
                       'ישוב קהילתי',
                       'כפר לא יהודי', 'שבט בדווי']


class YeshuvType(Enum):
    Big = 1
    Others = 2


class PlotType(Enum):
    Vote_Percent = 1



def _bar_graph_bzb_per_kalfi_smal_yeshuvs(series):
    barss = [series["310"], series["320"], series['330'], series['350'],
             series['370'], series['450'], series['460']]
    index_rev = ['מושב', 'מושב שיתופי', 'קיבוץ', 'כפר יהודי', 'ישוב קהילתי',
                 'כפר לא יהודי', 'שבט בדווי']
    index = reverse_list_of_strings(index_rev)
    df = pd.DataFrame({'Jew': barss}, index=index)
    ax = df.plot.bar(rot=0)
    ax.get_legend().remove()
    ax.set_alpha(0.8)
    font = {'family': 'serif',
            'color': 'black',
            'weight': 'semibold'
            }
    ax.set_title("Average BZB Per Kalfi By Yeshuv Size", fontsize=14,
                 fontdict=font)
    ax.set_xlabel("Yeshuv Size (In Thousands)", fontsize=11, fontdict=font)
    ax.set_ylabel("Avg BZB Per Kalfi", fontsize=11, fontdict=font)
    ylim((200, 600))
    x_location = [-0.319, 0.65, 1.65, 2.65, 3.65, 4.65, 5.65]
    y_bar_offset = 0.023
    x_offset = 0.06
    for i in range(len(barss)):
        ax.text(x_location[i] + x_offset, barss[i] + y_bar_offset,
                str(round(barss[i], 1)), color='chocolate',
                fontweight='semibold', fontsize=8)


def _bar_graph_bzb_per_kalfi_big_yeshuvs(series):
    bars_jews = [series["150"], series["160"], series['170'], series['180'],
                 series['190']]
    bars_arabs = [series["250"], series["260"], series['270'], series['280'],
                  series['290']]
    index = ['50-100', '20-50', '10-20', '5-10', '2-5']
    df = pd.DataFrame({'Jew': bars_jews, 'Non Jew': bars_arabs}, index=index)
    ax = df.plot.bar(rot=0)
    ax.set_alpha(0.8)

    font = {'family': 'serif',
            'color': 'black',
            'weight': 'semibold'
            }
    ax.set_title("Average BZB Per Kalfi By Yeshuv Size", fontsize=14,
                 fontdict=font)
    ax.set_xlabel("Yeshuv Size (In Thousands)", fontsize=11, fontdict=font)
    ax.set_ylabel("Avg BZB Per Kalfi", fontsize=11, fontdict=font)
    ylim((500, 700))
    x_location_jews_yeshuv = [-0.319, 0.65, 1.65, 2.65, 3.65, 4.65]
    x_location_jew_offset = 0
    x_location_arab_offset = 0.3
    y_bar_offset = 0.023
    for i in range(len(bars_jews)):
        ax.text(x_location_jews_yeshuv[i] + x_location_jew_offset,
                bars_jews[i] + y_bar_offset, str(round(bars_jews[i], 1)),
                color='steelblue', fontweight='semibold', fontsize=8)
        ax.text(x_location_jews_yeshuv[i] + x_location_arab_offset,
                bars_arabs[i] + y_bar_offset,
                str(round(bars_arabs[i], 1)), color='chocolate',
                fontweight='semibold', fontsize=8)

    print("asd")


def _bar_graph_error_small_yeshuvs(series):
    barss = [series["310"], series["320"], series['330'], series['350'],
             series['370'], series['450'], series['460']]
    index_rev = ['מושב', 'מושב שיתופי', 'קיבוץ', 'כפר יהודי', 'ישוב קהילתי',
                 'כפר לא יהודי', 'שבט בדווי']
    index = reverse_list_of_strings(index_rev)
    df = pd.DataFrame({'Jew': barss}, index=index)
    ax = df.plot.bar(rot=0)
    ax.get_legend().remove()
    ax.set_alpha(0.8)
    font = {'family': 'serif',
            'color': 'black',
            'weight': 'semibold'
            }
    ax.set_title("Error Vote % By Yeshuv Type", fontsize=14, fontdict=font)
    ax.set_xlabel("Yeshuv Type", fontsize=11, fontdict=font)
    ax.set_ylabel("Error Vote %", fontsize=11, fontdict=font)
    x_location = [-0.319, 0.65, 1.65, 2.65, 3.65, 4.65, 5.65]
    y_bar_offset = 0.023
    x_offset = 0.06
    for i in range(len(barss)):
        ax.text(x_location[i] + x_offset, barss[i] + y_bar_offset,
                str(round(barss[i], 2)) + '%', color='chocolate',
                fontweight='semibold', fontsize=10)


def _bar_graph_err_big_yeshuvs(series):
    bars_jews = [series["150"], series["160"], series['170'], series['180'],
                 series['190']]
    bars_arabs = [series["250"], series["260"], series['270'], series['280'],
                  series['290']]
    index = ['50-100', '20-50', '10-20', '5-10', '2-5']
    df = pd.DataFrame({'Jew': bars_jews, 'Non Jew': bars_arabs}, index=index)
    ax = df.plot.bar(rot=0)
    ax.set_alpha(0.8)

    font = {'family': 'serif',
            'color': 'black',
            'weight': 'semibold'
            }
    ax.set_title("Error Vote % By Yeshuv Size", fontsize=14, fontdict=font)
    ax.set_xlabel("Yeshuv Size (In Thousands)", fontsize=11, fontdict=font)
    ax.set_ylabel("Error Vote %", fontsize=11, fontdict=font)
    x_location_jews_yeshuv = [-0.319, 0.65, 1.65, 2.65, 3.65, 4.65]
    x_location_jew_offset = -0.051
    x_location_arab_offset = 0.35
    y_bar_offset = 0.023
    for i in range(len(bars_jews)):
        ax.text(x_location_jews_yeshuv[i] + x_location_jew_offset,
                bars_jews[i] + y_bar_offset, str(round(bars_jews[i], 2)) + '%',
                color='steelblue', fontweight='semibold', fontsize=8)
        ax.text(x_location_jews_yeshuv[i] + x_location_arab_offset,
                bars_arabs[i] + y_bar_offset,
                str(round(bars_arabs[i], 2)) + '%', color='chocolate',
                fontweight='semibold', fontsize=8)

    print("asd")


def reverse_list_of_strings(strings):
    return [x[::-1] for x in strings]


def _bar_graph_error_small_yeshuvs(series):
    barss = [series["310"], series["320"], series['330'], series['350'],
             series['370'], series['450'], series['460']]
    index_rev = ['מושב', 'מושב שיתופי', 'קיבוץ', 'כפר יהודי', 'ישוב קהילתי',
                 'כפר לא יהודי', 'שבט בדווי']
    index = reverse_list_of_strings(index_rev)
    df = pd.DataFrame({'Jew': barss}, index=index)
    ax = df.plot.bar(rot=0)
    ax.get_legend().remove()
    ax.set_alpha(0.8)
    font = {'family': 'serif',
            'color': 'black',
            'weight': 'semibold'
            }
    ax.set_title("Error Vote % By Yeshuv Type", fontsize=14, fontdict=font)
    ax.set_xlabel("Yeshuv Type", fontsize=11, fontdict=font)
    ax.set_ylabel("Error Vote %", fontsize=11, fontdict=font)
    x_location = [-0.319, 0.65, 1.65, 2.65, 3.65, 4.65, 5.65]
    y_bar_offset = 0.023
    x_offset = 0.06
    for i in range(len(barss)):
        ax.text(x_location[i] + x_offset, barss[i] + y_bar_offset,
                str(round(barss[i], 2)) + '%', color='chocolate',
                fontweight='semibold', fontsize=10)


def _bar_graph_err_big_yeshuvs(series):
    bars_jews = [series["150"], series["160"], series['170'], series['180'],
                 series['190']]
    bars_arabs = [series["250"], series["260"], series['270'], series['280'],
                  series['290']]
    index = ['50-100', '20-50', '10-20', '5-10', '2-5']
    df = pd.DataFrame({'Jew': bars_jews, 'Non Jew': bars_arabs}, index=index)
    ax = df.plot.bar(rot=0)
    ax.set_alpha(0.8)

    font = {'family': 'serif',
            'color': 'black',
            'weight': 'semibold'
            }
    ax.set_title("Error Vote % By Yeshuv Size", fontsize=14, fontdict=font)
    ax.set_xlabel("Yeshuv Size (In Thousands)", fontsize=11, fontdict=font)
    ax.set_ylabel("Error Vote %", fontsize=11, fontdict=font)
    x_location_jews_yeshuv = [-0.319, 0.65, 1.65, 2.65, 3.65, 4.65]
    x_location_jew_offset = -0.051
    x_location_arab_offset = 0.35
    y_bar_offset = 0.023
    for i in range(len(bars_jews)):
        ax.text(x_location_jews_yeshuv[i] + x_location_jew_offset,
                bars_jews[i] + y_bar_offset, str(round(bars_jews[i], 2)) + '%',
                color='steelblue', fontweight='semibold', fontsize=8)
        ax.text(x_location_jews_yeshuv[i] + x_location_arab_offset,
                bars_arabs[i] + y_bar_offset,
                str(round(bars_arabs[i], 2)) + '%', color='chocolate',
                fontweight='semibold', fontsize=8)

    print("asd")

def _bar_graph_small_yeshuvs(series):
    barss = [series["310"], series["320"], series['330'], series['350'],
             series['370'], series['450'], series['460']]
    index_rev = ['מושב', 'מושב שיתופי', 'קיבוץ', 'כפר יהודי', 'ישוב קהילתי',
                 'כפר לא יהודי', 'שבט בדווי']
    index = reverse_list_of_strings(index_rev)
    df = pd.DataFrame({'Jew': barss}, index=index)
    ax = df.plot.bar(rot=0)
    ax.get_legend().remove()
    ax.set_alpha(0.8)
    font = {'family': 'serif',
            'color': 'black',
            'weight': 'semibold'
            }
    ax.set_title("Vote % By Yeshuv Type", fontsize=14, fontdict=font)
    ax.set_xlabel("Yeshuv Type", fontsize=11, fontdict=font)
    ax.set_ylabel("Vote %", fontsize=11, fontdict=font)
    ylim((20, 85))
    x_location = [-0.319, 0.65, 1.65, 2.65, 3.65, 4.65, 5.65]
    y_bar_offset = 0.18
    x_offset = 0.04
    for i in range(len(barss)):
        ax.text(x_location[i] + x_offset, barss[i] + y_bar_offset,
                str(round(barss[i], 2)) + '%', color='chocolate',
                fontweight='semibold', fontsize=10)





def _bar_graph_big_yeshuvs(series):
    bars_jews = [series["150"], series["160"], series['170'], series['180'],
                 series['190']]
    bars_arabs = [series["250"], series["260"], series['270'], series['280'],
                  series['290']]
    index = ['50-100', '20-50', '10-20', '5-10', '2-5']
    df = pd.DataFrame({'Jew': bars_jews, 'Non Jew': bars_arabs}, index=index)
    ax = df.plot.bar(rot=0)
    ax.set_alpha(0.8)

    font = {'family': 'serif',
            'color': 'black',
            'weight': 'semibold'
            }
    ax.set_title("Vote % By Yeshuv Size", fontsize=14, fontdict=font)
    ax.set_xlabel("Yeshuv Size (In Thousands)", fontsize=11, fontdict=font)
    ax.set_ylabel("Vote %", fontsize=11, fontdict=font)
    ylim((40, 85))

    ax.legend(loc='upper left', shadow=True)
    x_location_jews_yeshuv = [-0.319, 0.65, 1.65, 2.65, 3.65, 4.65]
    x_location_arab_offset = 0.35
    y_bar_offset = 0.18
    for i in range(len(bars_jews)):
        ax.text(x_location_jews_yeshuv[i], bars_jews[i] + y_bar_offset,
                str(round(bars_jews[i], 2)) + '%', color='steelblue',
                fontweight='semibold', fontsize=8)
        ax.text(x_location_jews_yeshuv[i] + x_location_arab_offset,
                bars_arabs[i] + y_bar_offset,
                str(round(bars_arabs[i], 2)) + '%', color='chocolate',
                fontweight='semibold', fontsize=8)


def gather_data_by_yeshuve_type(kneset_data, x,
                                vote_percent_per_yeshuv_type_series_list):
    for kneset_num in x:
        df = kneset_data.get_kneset_data(kneset_num)
        bzb_grpd = df.groupby("Yeshuv_Type")['BZB'].sum()
        voters_grpd = df.groupby("Yeshuv_Type")['Voters'].sum()
        vote_percent_per_yeshuv_type = voters_grpd.divide(bzb_grpd,
                                                          fill_value=0)
        into_percent_representation = vote_percent_per_yeshuv_type.multiply(
            100)
        vote_percent_per_yeshuv_type_series_list.append(
            into_percent_representation)


def stats_grpd_by_yeshuv_type(kneset_data: BzbPerKalfiResult):
    vote_percent_per_yeshuv_type_series_list = []
    from main import KNESSETS_LIST
    gather_data_by_yeshuve_type(kneset_data, KNESSETS_LIST,
                                vote_percent_per_yeshuv_type_series_list)
    # turn list into pandas series:
    ser = pd.Series(vote_percent_per_yeshuv_type_series_list,
                    index=KNESSETS_LIST)


    # for kneset_num in x:
    #     df = kneset_data.get_kneset_data(kneset_num)
    #     kalfi_count = df.groupby("Yeshuv_Type")['Kalfi_Num'].count()
    #     bzb_grpd = df.groupby("Yeshuv_Type")['BZB'].sum()
    #     voters_grpd = df.groupby("Yeshuv_Type")['Voters'].sum()
    #     error_grpd  = df.groupby("Yeshuv_Type")['Error_Voters'].sum()
    #
    #     vote_percent_per_yeshuv_type = voters_grpd.divide(bzb_grpd, fill_value=0)
    #     a = vote_percent_per_yeshuv_type.multiply(100)
    #     _bar_graph_big_yeshuvs(a)
    #     _bar_graph_small_yeshuvs(a)
    #
    #     err = error_grpd.divide(voters_grpd, fill_value=0)
    #     a = err.multiply(100)
    #     # _bar_graph_err_big_yeshuvs(a)
    #     # _bar_graph_error_small_yeshuvs(a)
    #
    #     avrg_bzb_by_yeshuv_type =   bzb_grpd.divide(kalfi_count, fill_value=0)
    #     # _bar_graph_bzb_per_kalfi_big_yeshuvs(avrg_bzb_by_yeshuv_type)
    #     # _bar_graph_bzb_per_kalfi_smal_yeshuvs(avrg_bzb_by_yeshuv_type)
    #
    #
    #     # grpd_data_sum = grpd_data.sum()
    #     grpd_data_mean = df.groupby("Yeshuv_Type").mean()
    #
    #
    #
    #
    #     # count for big cities maybe num kalfis or give examples.
