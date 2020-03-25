import pandas as pd

from plot_helper import YeshuvType, PlotType
from constants import BIG_YESHUV_INDEX, SMALL_YESHUV_INDEX, HUGE_YESHUV_INDEX
from src.statistics.GeneralPopStats.AllKnessets.all_knesets_stats_by_yeshuv_type import \
    reverse_list_of_strings


def _set_bar_graph_titles(fig, axs, pt: PlotType, yt: YeshuvType):
    if pt == PlotType.Vote_Percent:
        if yt == YeshuvType.Big or yt == YeshuvType.Huge:
            fig.suptitle('Voting % By Yeshuv Size (Per Knesset)')
            for ax in axs.flat:
                ax.set(xlabel="Yeshuv Size (In Thousands)", ylabel='Vote %')
            for ax in axs.flat:
                ax.label_outer()
        elif yt == YeshuvType.Others:
            fig.suptitle('Voting % By Yeshuv Type (Per Knesset)')
            for ax in axs.flat:
                ax.set(xlabel="Yeshuv Type", ylabel='Vote %')
    elif pt == PlotType.Error:
        if yt == YeshuvType.Big or yt == YeshuvType.Huge:
            fig.suptitle("Error Vote % By Yeshuv Size (Per Knesset)")
            for ax in axs.flat:
                ax.set(xlabel="Yeshuv Size (In Thousands)",
                       ylabel="Error Vote %")
            for ax in axs.flat:
                ax.label_outer()
        elif yt == YeshuvType.Others:
            fig.suptitle("Error Vote % By Yeshuv Type (Per Knesset)")
            for ax in axs.flat:
                ax.set(xlabel="Yeshuv Type",
                       ylabel="Error Vote %")
            for ax in axs.flat:
                ax.label_outer()
    elif pt == PlotType.AvgBzb:
        if yt == YeshuvType.Big or yt == YeshuvType.Huge:
            fig.suptitle("Average BZB Per Kalfi By Yeshuv Size (Per Knesset)")
            for ax in axs.flat:
                ax.set(xlabel="Yeshuv Size (In Thousands)",
                       ylabel="Avg BZB Per Kalfi")
            for ax in axs.flat:
                ax.label_outer()
        elif yt == YeshuvType.Others:
            fig.suptitle("Average BZB Per Kalfi By Yeshuv Type (Per Knesset)")
            for ax in axs.flat:
                ax.set(xlabel="Yeshuv Type",
                       ylabel="Avg BZB Per Kalfi")
            for ax in axs.flat:
                ax.label_outer()


def create_df_from_series_per_knesset(series, yt: YeshuvType):
    if yt == YeshuvType.Big:
        index_list = BIG_YESHUV_INDEX
        bars_jews = [series["150"], series["160"], series['170'],
                     series['180'], series['190']]
        bars_non_jews = [series["250"], series["260"], series['270'],
                         series['280'],
                         series['290']]
        df = pd.DataFrame({'Jew': bars_jews, 'Non Jew': bars_non_jews},
                          index=index_list)
        return df
    elif yt == YeshuvType.Others:
        bars = [series["310"], series["320"], series['330'], series['350'],
                series['370'], series['450'], series['460']]

        index_list_rev = SMALL_YESHUV_INDEX
        index_list = reverse_list_of_strings(index_list_rev)
        df = pd.DataFrame({'data': bars}, index=index_list)
        return df
    elif yt == YeshuvType.Huge:
        bars = [series["120"], series["130"], series['140']]
        index_list = HUGE_YESHUV_INDEX
        df = pd.DataFrame({'data': bars}, index=index_list)
        return df


def __find_offsets(pt, yt):
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


def get_col_text_label(pt, row, yt):
    text_label_jew = ""
    text_label_data = ""
    text_label_non_jew = ""
    if yt == YeshuvType.Big:
        if pt == PlotType.Vote_Percent or pt == PlotType.Error:
            text_label_jew = str(round(row['Jew'], 2)) + '%'
            text_label_non_jew = str(round(row['Non Jew'], 2)) + '%'
        elif pt == PlotType.AvgBzb:
            text_label_jew = str(round(row['Jew'], 1))
            text_label_non_jew = str(round(row['Non Jew'], 1))
        return text_label_jew, text_label_non_jew
    elif yt == YeshuvType.Others or yt == YeshuvType.Huge:
        if pt == PlotType.Vote_Percent or pt == PlotType.Error:
            text_label_data = str(round(row['data'], 2)) + '%'
        elif pt == PlotType.AvgBzb:
            text_label_data = str(round(row['data'], 1))
        return text_label_data


def _set_graph_design(ax, knesset_num, pt: PlotType, yt: YeshuvType):
    ax.set_alpha(0.8)
    font = {'family': 'serif',
            'color': 'black',
            'weight': 'semibold'
            }
    ax.set_title(knesset_num, fontdict=font)

    ax.get_legend().remove()
    if pt == PlotType.Vote_Percent:
        if yt == YeshuvType.Big or YeshuvType.Huge:
            ax.set_ylim((40, 85))
        elif yt == YeshuvType.Others:
            ax.set_ylim((20, 85))
    elif pt == PlotType.Error:
        if yt == YeshuvType.Others:
            ax.set_ylim((0.2, 3.5))
        elif yt == YeshuvType.Huge:
            ax.set_ylim((0.4, 1.5))

    elif pt == PlotType.AvgBzb:
        if yt == YeshuvType.Big or yt == YeshuvType.Huge:
            ax.set_ylim((500, 700))
        elif yt == YeshuvType.Others:
            ax.set_ylim((200, 600))


def _add_column_text_labels(ax, df, pt: PlotType, yt: YeshuvType):
    x_bar_offset, x_bar_non_jew_offset, y_bar_offset = __find_offsets(pt, yt)
    if yt == YeshuvType.Big:

        x_index_location_on_figure = {'50-100': -0.319,
                                      '20-50': 0.65,
                                      '10-20': 1.65,
                                      '5-10': 2.65,
                                      '2-5': 3.65
                                      }

        for index, row in df.iterrows():
            text_label_jew, text_label_non_jew = get_col_text_label(pt, row,
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
            text_label_data = get_col_text_label(pt, row, yt)
            idx_num += 1
            ax.text(x_location[idx_num] + x_bar_offset,
                    row['data'] + y_bar_offset,
                    text_label_data, color='steelblue',
                    fontweight='semibold', fontsize=10)
    elif yt == YeshuvType.Huge:
        x_location = [-0.27, 0.71, 1.70]
        idx_num = -1
        for index, row in df.iterrows():
            text_label_data = get_col_text_label(pt, row, yt)
            idx_num += 1
            ax.text(x_location[idx_num] + x_bar_offset,
                    row['data'] + y_bar_offset,
                    text_label_data, color='steelblue',
                    fontweight='semibold', fontsize=12)


def get_plot_idx_by_knesset(knesset_num, yt: YeshuvType):
    if yt == YeshuvType.Big or yt == YeshuvType.Huge:
        knesset_graph_loc_dict = {'18': [0, 0],
                                  '19': [0, 1],
                                  '20': [1, 0],
                                  '21': [1, 1],
                                  '22': [1, 2]}
        return knesset_graph_loc_dict[knesset_num]
    elif yt == YeshuvType.Others:
        knesset_graph_loc_dict_others = {'18': [0, 0],
                                  '19': [1, 0],
                                  '20': [1, 1],
                                  '21': [2, 0],
                                  '22': [2, 1]}
        return knesset_graph_loc_dict_others[knesset_num]