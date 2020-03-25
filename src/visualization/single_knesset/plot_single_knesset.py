from plot_helper import YeshuvType, PlotType
from matplotlib import pyplot as plt
import pandas as pd

from src.statistics.GeneralPopStats.AllKnessets import plot_style_helper


def __get_yt_title_single_knesset(yt: YeshuvType, pt: PlotType):
    if pt == PlotType.Vote_Percent:
        if yt == YeshuvType.Big:
            return "B. Jew Vs Non Jew 2K-100K Vote %"
        elif yt == YeshuvType.Huge:
            return "A. 100K+ Vote % Largest Cities"
        elif yt == YeshuvType.Others:
            return "C. Jew And Non Jew Small Yeshuv Types"


    if yt == YeshuvType.Big:
        return "B. Jew Vs Non Jew 2K-100K BZB"
    elif yt ==YeshuvType.Huge:
        return "A. 100K+ BZB Largest Cities"
    elif yt ==YeshuvType.Others:
        return "C. Jew And Non Jew Small Yeshuv Types"



def _set_graph_design_single_knesset(ax, knesset_num, pt: PlotType, yt: YeshuvType):
    ax.set_alpha(0.8)
    font = {'family': 'serif',
            'color': 'black',
            'weight': 'semibold'
            }
    ax.set_title(__get_yt_title_single_knesset(yt, pt), fontdict=font)

    ax.get_legend().remove()
    if pt == PlotType.Vote_Percent:
        if yt == YeshuvType.Big or YeshuvType.Huge:
            ax.set_ylim((40, 85))
        elif yt == YeshuvType.Others:
            ax.set_ylim((20, 85))
    elif pt == PlotType.Error:
        if yt == YeshuvType.Others:
            ax.set_ylim((0, 1.3))
        elif yt == YeshuvType.Huge:
            ax.set_ylim((0, 1))
        elif yt == YeshuvType.Big:
            ax.set_ylim((0.2, 1.1))

    elif pt == PlotType.AvgBzb:
        if yt == YeshuvType.Big or yt == YeshuvType.Huge:
            ax.set_ylim((580, 730))
        elif yt == YeshuvType.Others:
            ax.set_ylim((380, 635))



def _set_bar_graph_titles_single_knesset(fig, ax, pt: PlotType, yt: YeshuvType):
    if pt == PlotType.Vote_Percent:
        if yt == YeshuvType.Big or yt == YeshuvType.Huge:

            ax.set(xlabel='Yeshuv Size (In Thousands)', ylabel='Vote %')

        elif yt == YeshuvType.Others:
            fig.suptitle('Voting % By Yeshuv Type (Per Knesset)')
            ax.set(xlabel='Yeshuv Type', ylabel='Vote %')


    elif pt == PlotType.Error:
        if yt == YeshuvType.Big or yt == YeshuvType.Huge:

            ax.set(xlabel="Yeshuv Size (In Thousands)",
                       ylabel="Error Vote %")

        elif yt == YeshuvType.Others:
            fig.suptitle("Error Vote % By Yeshuv Type (Per Knesset)")

            ax.set(xlabel="Yeshuv Type",
                       ylabel="Error Vote %")


    elif pt == PlotType.AvgBzb:
        if yt == YeshuvType.Big or yt == YeshuvType.Huge:
            #fig.suptitle("Average BZB Per Kalfi By Yeshuv Size (Per Knesset)")

            ax.set(xlabel="Yeshuv Size (In Thousands)",
                       ylabel="Avg BZB Per Kalfi")


        elif yt == YeshuvType.Others:
            fig.suptitle("Average BZB Per Kalfi By Yeshuv Type (Per Knesset)")

            ax.set(xlabel="Yeshuv Type",
                       ylabel="Avg BZB Per Kalfi")




def _get_plot_idx_by_yt(yt: YeshuvType):
    if yt == YeshuvType.Huge:
        return [0,0]
    elif  yt == YeshuvType.Big:
       return [1,0]
    elif yt == YeshuvType.Others:
       return [0,1]






def __find_offsets_single_knesset(pt, yt):
    x_bar_offset = 0
    x_bar_non_jew_offset = 0
    y_bar_offset = 0

    if pt == PlotType.Vote_Percent:
        if yt == YeshuvType.Big:
            x_bar_non_jew_offset = 0.35
            y_bar_offset = 0.18
        elif yt == YeshuvType.Others:
            x_bar_offset = 0.04
            y_bar_offset = 0.023

    elif pt == PlotType.Error:
        if yt == YeshuvType.Big:
            x_bar_offset = -0.051
            x_bar_non_jew_offset = 0.35
            y_bar_offset = 0.023
        elif yt == YeshuvType.Others:
            y_bar_offset = 0.023
            x_bar_offset = 0.06
    elif pt == PlotType.AvgBzb:
        if yt == YeshuvType.Big:
            x_bar_offset = 0
            x_bar_non_jew_offset = 0.3
            y_bar_offset = 0.023
        elif yt == YeshuvType.Others:
            y_bar_offset = 0.023
            x_bar_offset = 0.06
    return x_bar_offset, x_bar_non_jew_offset, y_bar_offset


def __add_column_text_labels_single_knesset(ax, df, pt: PlotType, yt: YeshuvType):
    x_bar_offset, x_bar_non_jew_offset, y_bar_offset = __find_offsets_single_knesset(pt, yt)
    if yt == YeshuvType.Big:

        x_index_location_on_figure = {'50-100': -0.319,
                                      '20-50': 0.65,
                                      '10-20': 1.65,
                                      '5-10': 2.65,
                                      '2-5': 3.65
                                      }

        for index, row in df.iterrows():
            text_label_jew, text_label_non_jew = plot_style_helper.get_col_text_label(pt, row,
                                                                                      yt)

            ax.text(x_index_location_on_figure[index] + x_bar_offset,
                    row['Jew'] + y_bar_offset,
                    text_label_jew, color='steelblue',
                    fontweight='semibold', fontsize=8)
            ax.text(x_index_location_on_figure[index] + x_bar_non_jew_offset,
                    row['Non Jew'] + y_bar_offset,
                    text_label_non_jew, color='chocolate',
                    fontweight='semibold', fontsize=8)

    elif yt == YeshuvType.Others:
        x_location = [-0.319, 0.65, 1.65, 2.65, 3.65, 4.65, 5.65]
        idx_num = -1
        for index, row in df.iterrows():
            text_label_data = plot_style_helper.get_col_text_label(pt, row, yt)
            idx_num += 1
            ax.text(x_location[idx_num] + x_bar_offset,
                    row['data'] + y_bar_offset,
                    text_label_data, color='steelblue',
                    fontweight='semibold', fontsize=10)
    elif yt == YeshuvType.Huge:
        x_location = [-0.20, 0.78, 1.78]
        idx_num = -1
        for index, row in df.iterrows():
            text_label_data = plot_style_helper.get_col_text_label(pt, row, yt)
            idx_num += 1
            ax.text(x_location[idx_num] + x_bar_offset,
                    row['data'] + y_bar_offset,
                    text_label_data, color='steelblue',
                    fontweight='semibold', fontsize=12)



def _add_to_plot_knesset(fig, df: pd.DataFrame, axs, pt: PlotType, yt: YeshuvType ):
    i, j = _get_plot_idx_by_yt(yt)
    if yt == YeshuvType.Big:
        a = df.plot.bar(rot=0, ax=axs[i,j])
        fig.legend([a],  # The line objects
                   labels=["Jews", "Non Jews"],  # The labels for each line
                   loc='lower left',  # Position of legend
                   borderaxespad=0.1,  # Small spacing around legend box
                   title=""
                   )
    elif yt == YeshuvType.Others or YeshuvType.Huge:
        print("i,j={}{}".format(i,j))
        df.plot.bar(rot=0, ax=axs[i,j], color='chocolate')

    _set_graph_design_single_knesset(axs[i,j], "22", pt, yt)
    __add_column_text_labels_single_knesset(axs[i,j], df, pt, yt)


def single_knesset_all_yeshuv_types(data_series, pt: PlotType):

    fig, axs = plt.subplots(2, 2, figsize=(12, 8),
                            gridspec_kw={'hspace': 0.28,
                                         'wspace': 0.18, 'width_ratios':[1, 1.8]})




    for yt in YeshuvType:
        i, j = _get_plot_idx_by_yt(yt)
        ax = axs[i,j]
        _set_bar_graph_titles_single_knesset(fig, ax, pt, yt)
        df = plot_style_helper.create_df_from_series_per_knesset(data_series, yt)
        _add_to_plot_knesset(fig, df, axs, pt, yt)
    plt.tight_layout()
    plt.show()