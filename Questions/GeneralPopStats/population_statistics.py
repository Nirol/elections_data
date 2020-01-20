import matplotlib.pyplot as plt
from numpy import nanstd
from scipy.stats import pearsonr, kendalltau
import pandas as pd
from Parse.data_classes import ResultKnesset, PopulationInfo, PopVars, \
    PopulationStats
import Questions.GeneralPopStats.AllKnessets.all_knesets_stats_by_yeshuv_type
from Questions.Plots.box_plot import all_knessets_box_plot_graph
from Questions.Plots.general_pop_plot import graph_avg_bzb_vote_percent, \
    graph_general_stat
from constants import KNESSETS_LIST


def general_over_knesets_stats(kneset_data: ResultKnesset) -> None:
    x = ["18", "19", "20", "21", "22"]
    avg_bzb_per_kalfi_list = kneset_data.get_var_per_kneset(PopVars.AvgBzb)
    vote_percent_list = kneset_data.get_var_per_kneset(PopVars.VotePercent)
    graph_avg_bzb_vote_percent(x, avg_bzb_per_kalfi_list, vote_percent_list)

    bzb_per_kalfi_list = kneset_data.get_var_per_kneset(PopVars.Bzb)
    num_kalfi_list = kneset_data.get_var_per_kneset(PopVars.Num_Kalfi)
    unique_yeshuv = kneset_data.get_var_per_kneset(PopVars.Unq_Yeshuv)
    voters_list = kneset_data.get_var_per_kneset(PopVars.Voters)

    graph_general_stat(x, bzb_per_kalfi_list, num_kalfi_list, unique_yeshuv,
                       voters_list)





def stats_population_kneset_df(knesset_df: pd.DataFrame) -> PopulationInfo:
    population_stats = calculate_bzb_vote_percent_pearson(
        knesset_df['BZB'],
        knesset_df[
            'vote_percent'])
    total_bzb = knesset_df['BZB'].sum()
    total_voters = knesset_df['Voters'].sum()
    num_kalfi_total = len(knesset_df['SN'])
    num_unique_yeshuvim = len(set(knesset_df['SN']))
    filtered_population_stats = PopulationInfo(num_kalfi_total,
                                               num_unique_yeshuvim, total_bzb,
                                               total_voters, population_stats)
    return filtered_population_stats


def calculate_bzb_vote_percent_pearson(bzb_col: pd.Series,
                                       vote_percent_col: pd.Series) -> PopulationStats:
    pearson_res = pearsonr(bzb_col,
                           vote_percent_col)
    vote_percent_std = nanstd(vote_percent_col)
    tau, p_value = kendalltau(bzb_col, vote_percent_col)
    return PopulationStats(pearson_res, [tau, p_value], vote_percent_std)


def gather_data_by_yeshuve_type_group_by(kneset_data: ResultKnesset):
    dict_final = {}
    for kneset_num in KNESSETS_LIST:
        df = kneset_data.get_kneset_data(kneset_num)
        dict_final[kneset_num] = dict(tuple(df.groupby("Yeshuv_Type")))
    return dict_final


def stats_box_plot(results: ResultKnesset) -> None:
    dict_df = gather_data_by_yeshuve_type_group_by(results)
    all_knessets_box_plot_graph(dict_df, Questions.GeneralPopStats.AllKnessets.all_knesets_stats_by_yeshuv_type.PlotType.Vote_Percent_Box_Plot,
                                Questions.GeneralPopStats.AllKnessets.all_knesets_stats_by_yeshuv_type.YeshuvType.Big)
