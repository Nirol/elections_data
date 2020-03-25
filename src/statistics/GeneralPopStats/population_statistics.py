from numpy import nanstd
from scipy.stats import pearsonr, kendalltau

from read_files_helper import KnesetVars
from src.data.data_classes import ResultKnesset, PopulationInfo, PopulationStats
from general_plots import graph_general_stat, graph_avg_bzb_vote_percent
from single_knesset.plot_single_knesset import single_knesset_all_yeshuv_types
import pandas as pd




def explore_variables_vote(kneset_data: ResultKnesset) -> None:
#all this commend were executed in console based on the results knesset data.
    #vote percent smallest 50 tables:
    df = kneset_data.get_kneset_data("22")
    stats = df.describe()

    from src.statistics.GeneralPopStats.AllKnessets.all_knesets_stats_by_yeshuv_type import \
        gather_data_by_yeshuve_type_group_by
    import plot_helper
    vote_percent_groupd_by = gather_data_by_yeshuve_type_group_by(kneset_data,
                                                                  plot_helper.PlotType.Vote_Percent)

    single_knesset_all_yeshuv_types(vote_percent_groupd_by["22"],
                                    plot_helper.PlotType.Vote_Percent)


    #boxplot
    import matplotlib.pyplot as plt
    fig3, ax = plt.subplots()
    ax.set_title('Vote % BoxPlot')
    boxplot = ax.boxplot(df.vote_percent)


    plt.ylabel('Vote %')
    plt.xlabel('')


    vp_series = df.vote_percent

    vp_series.plot.hist(grid=True, bins=20, rwidth=0.9,
                             color='#607c8e')

    plt.title('Vote % Per Kalfi ')
    plt.xlabel('Vote %')
    plt.ylabel('N Kalfis')
    plt.ylabel('n kalfis')



    mu, sigma = vp_series.mean(), vp_series.std()
    props = dict(boxstyle='round', facecolor='plum', alpha=0.4)
    plt.text(6, 1600,
             r'$\mu={},\ \sigma={}$'.format(round(mu, 2), round(sigma, 2)),
             fontsize=14,
             verticalalignment='top', bbox=props)


    plt.axvline(vp_series.mean(), color='coral', linestyle='dashed', linewidth=2,
                alpha=0.65)



    caps = boxplot['caps']
    capbottom = caps[0].get_ydata()[0]
    vote_outliers_df = df[df["vote_percent"] < capbottom]
    len(vote_outliers_df)
    vote_outliers_df.sort_values(by=['vote_percent'], ascending=False, inplace = True)

    len(vote_outliers_df["SN"].unique())
    vote_outliers_df_value_count = vote_outliers_df["Yeshuv"].value_counts()


    threshold = 2
    mask = vote_outliers_df_value_count > threshold
    tail_prob = vote_outliers_df_value_count.loc[~mask].sum()
    vote_outliers_df_value_count = vote_outliers_df_value_count.loc[mask]
    vote_outliers_df_value_count["Other"] = tail_prob


    ax = vote_outliers_df_value_count.plot.barh(
        title="Low Vote % Outliers Klafis Value Count By Yeshuv")
    ax.set_xlabel("N Kalfis")
    ax.invert_yaxis()
    ax.grid(axis='x')
    plt.tight_layout()




    #non jew part
    vote_small_non_jew = voters_small[voters_small.apply(
        lambda x: x['Yeshuv_Type'] in plot_helper.NON_JEW_YESHUVS, axis=1)]
    len(vote_small_non_jew)
    value_count_small_non_jew = vote_small_non_jew["Yeshuv"].value_counts()
    len(vote_small_non_jew["Yeshuv"].unique())
    print(value_count_small_non_jew.head(25))

    #jew part - for arabic printing
    vote_small_jew = voters_small[voters_small.apply(
        lambda x: x['Yeshuv_Type'] not in plot_helper.NON_JEW_YESHUVS, axis=1)]
    len(vote_small_jew)
    jew_arabic_printing = vote_small_jew[vote_small_jew['arab_printing']==1]
    len(jew_arabic_printing)














def error_rate_explore(kneset_data):
    df = kneset_data.get_kneset_data("22")


    avg_error = gather_data_by_yeshuve_type_group_by(kneset_data,
                                                     plot_helper.PlotType.Error)
    single_knesset_all_yeshuv_types(avg_error["22"],
                                    plot_helper.PlotType.Error)

    #boxplot

    df["Error_Percent"] =( df["Error_Voters"] / df["Voters"] )*100
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.set_title('Klafis Error Votes Percent BoxPlot')
    ax.set_ylim((-1, 6))
    boxplot = ax.boxplot(df.Error_Percent)
    __make_labels_box_plot(ax, boxplot)
    #outliers
    caps = boxplot['caps']
    captop = caps[1].get_ydata()[0]
    error_outliers_df = df[df["Error_Percent"] > captop]
    len(error_outliers_df)
    error_outliers_df.sort_values(by=['Error_Percent'], ascending=False, inplace = True)

    len(error_outliers_df["SN"].unique())
    error_outliers_df_value_count = error_outliers_df["Yeshuv"].value_counts()
    threshold = 10
    mask = error_outliers_df_value_count > threshold
    tail_prob = error_outliers_df_value_count.loc[~mask].sum()
    error_outliers_df_value_count = error_outliers_df_value_count.loc[mask]
    error_outliers_df_value_count["Other"] = tail_prob

    fig, ax = plt.subplots()
    ax = error_outliers_df_value_count.plot.barh(title = "Error Vote Outliers Klafis Value Count By Yeshuv")
    ax.set_xlabel( "N Kalfis")
    ax.invert_yaxis()
    ax.grid(axis='x')
    plt.tight_layout()


    print(error_outliers_df_value_count.head(50))

    # non jew part
    error_otulier_non_jew = error_outliers_df[error_outliers_df.apply(
        lambda x: x['Yeshuv_Type'] in plot_helper.NON_JEW_YESHUVS, axis=1)]
    len(error_otulier_non_jew)
    value_count_small_non_jew = error_otulier_non_jew["Yeshuv"].value_counts()
    len(error_otulier_non_jew["Yeshuv"].unique())
    print(value_count_small_non_jew.head(25))





    #histogram

    error_percent_series = df.Error_Percent

    error_percent_series.plot.hist(grid=True, bins=80, rwidth=0.9, range=(0,4.2),
                         color='#607c8e')
    import matplotlib.pyplot as plt
    plt.axvline(error_percent_series.mean(), color='coral', linestyle='dashed',
                linewidth=2, alpha=0.6)

    plt.title('Kalfis Number By Error Vote % ')
    plt.xlabel('Error Vote %')
    plt.ylabel('N Kalfis')
    plt.grid(axis='y', alpha=0.75)
    mu, sigma = error_percent_series.mean(), error_percent_series.std()
    props = dict(boxstyle='round', facecolor='plum', alpha=0.4)
    plt.text(2, 1600,
             r'$\mu={}\%,\ \sigma={}$'.format(round(mu, 2), round(sigma, 2)),
             fontsize=14,
             verticalalignment='top', bbox=props)


def bzb_threshold_plot_explore(kneset_data):
    df_thresh = kneset_data.get_threshold_kneset_dict(357)
    df_tocompare = kneset_data.get_threshold_kneset_dict(0)

    avg_bzb_groupd_by = gather_data_by_yeshuve_type_group_by(df_thresh, plot_helper.PlotType.AvgBzb)
    avg_bzb_groupd_tocomp = gather_data_by_yeshuve_type_group_by(df_tocompare,
                                                                 plot_helper.PlotType.AvgBzb)

    avg_bzb_groupd_by_22 = avg_bzb_groupd_by["22"]
    avg_bzb_groupd_tocomp_22 = avg_bzb_groupd_tocomp["22"]
    single_knesset_all_yeshuv_types(avg_bzb_groupd_by["22"], plot_helper.PlotType.AvgBzb)


def explore_variables_bzb(kneset_data: ResultKnesset) -> None:
    df = kneset_data.get_kneset_data("22")
    df_thresh = kneset_data.get_threshold_kneset_dict(357).get_kneset_data("22")
    stats = df.describe()
    #boxplot
    import matplotlib.pyplot as plt
    fig3, ax3 = plt.subplots()
    ax3.set_title('Klafis BZB BoxPlot')
    my_boxes = ax3.boxplot(df.BZB)
    make_labels(ax3, my_boxes)



    bzb_series = df.BZB

    bzb_series.describe()
    bzb_series.plot.hist(grid=True, bins=80, rwidth=0.9,
                       color='#607c8e')

    plt.axvline(bzb_series.mean(), color='coral', linestyle='dashed', linewidth=2, alpha=0.6)
    plt.title('BZB per kalfi ')
    plt.xlabel('BZB')
    plt.ylabel('n kalfis')
    plt.grid(axis='y', alpha=0.75)
    mu, sigma = bzb_series.mean(), bzb_series.std()
    props = dict(boxstyle='round', facecolor='plum', alpha=0.4)
    plt.text(60,1600,  r'$\mu={},\ \sigma={}$'.format(round(mu,2),round(sigma,2)), fontsize=14,
            verticalalignment='top', bbox=props)




    BZB_small = df.nsmallest(331, "BZB")

    len(BZB_small["Yeshuv"].unique())
    BZB_small_value_count = BZB_small["Yeshuv"].value_counts()
    print(BZB_small_value_count.head(50))



    voters_big = df.nlargest(200, "BZB")
    len(voters_big["Yeshuv"].unique())
    value_count_voters_small = voters_big["Yeshuv"].value_counts()
    print(value_count_voters_small.head(25))

    #non jew part
    vote_small_non_jew = voters_big[voters_big.apply(
        lambda x: x['Yeshuv_Type'] in plot_helper.NON_JEW_YESHUVS, axis=1)]
    len(vote_small_non_jew)
    value_count_small_non_jew = vote_small_non_jew["Yeshuv"].value_counts()
    len(vote_small_non_jew["Yeshuv"].unique())
    print(value_count_small_non_jew.head(25))


    print((df[df['SN'] == 3000]["BZB"]).describe())
    print((df[df['SN'] == 5000]["BZB"]).describe())
    print((df[df['SN'] == 4000]["BZB"]).describe())
    print((df[df['SN'] == 8300]["BZB"]).describe())
    print((df[df['SN'] == 7900]["BZB"]).describe())
    print((df[df['SN'] == 70]["BZB"]).describe())


    print(df[df['SN'] == 5000]["BZB"].mean())
    print(df[df['SN'] == 4000]["BZB"].mean())
    print(df[df['SN'] == 8300]["BZB"].mean())
    print( df[df['SN'] == 7900]["BZB"].mean())
    print( df[df['SN'] == 70]["BZB"].mean())

    print(df[df['SN'] == 3000]["BZB"].stats())
    print(df[df['SN'] == 5000]["BZB"].mean())
    print(df[df['SN'] == 4000]["BZB"].mean())
    print(df[df['SN'] == 8300]["BZB"].mean())
    print( df[df['SN'] == 7900]["BZB"].mean())
    print( df[df['SN'] == 70]["BZB"].mean())

    kfar = df[df['Yeshuv_Type'] == '450']
    len(kfar)
    bdui = df[df['Yeshuv_Type'] == '460']
    len(bdui)
    kfar_df = kfar.sort_values(by=['BZB'], ascending=False)[:].head(10)
    kfar_df.to_csv(r'Data/output/data_exploration/bzb/kfar_badui_top_bzb.csv')
    bdui = bdui.sort_values(by=['BZB'], ascending=False)[:].head(10)
    bdui.to_csv(r'Data/output/data_exploration/bzb/kfar_badui_real_top_bzb.csv')
    kfar_stat = kfar.describe()
    bdui_stat = bdui.describe()








def general_over_knesets_stats_graph(kneset_data: ResultKnesset) -> None:
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
        knesset_df[KnesetVars.BZB.value],
        knesset_df[
            KnesetVars.Vote_Percent.value])
    total_bzb = knesset_df[KnesetVars.BZB.value].sum()
    total_voters = knesset_df[KnesetVars.Voters.value].sum()
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


