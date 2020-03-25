import itertools

import seaborn as sns
import numpy as np

import plot_helper
from read_files_helper import KnesetVars


def corr_scatter_plot(df, yehuv_types_order,  ax, title, kvar1: KnesetVars, kvar2: KnesetVars,color_by: KnesetVars):
    # sns.scatterplot(x=kvar1.value, y=kvar2.value, data=df, hue=color_by.value,
    #                        hue_order=yehuv_types_order, ax=ax)
    sns.regplot(x=kvar1.value, y=kvar2.value, data=df, ax=ax)

    # ax.legend_.remove()
    ax.set_title(title)




def prepare_new_yeshuv_types_for_scatter_plot(df):
    jew_small_yeshuv_code_list = ["310", "320", '330', '350', '370', '191',
                                  '192', '193', '340', '510']
    arab_small_yeshuv_code_list = ['450', '460']
    smal_jew_yeshuv_representation = list(
        itertools.repeat("Small Jew Yeshuv", 10))
    smal_arab_yeshuv_representation = list(
        itertools.repeat("Small Arab Yeshuv", 2))

    dictionary = dict(
        zip(jew_small_yeshuv_code_list, smal_jew_yeshuv_representation))

    dictionary2 = dict(zip(arab_small_yeshuv_code_list,
                           smal_arab_yeshuv_representation))
    dictionary.update(dictionary2)

    big_jew_yeshuv_representation = list(
        itertools.repeat("Big Jew Yeshuv", 5))

    d3 = dict(zip(plot_helper.BIG_JEW_YESHUV_LIST,
                  big_jew_yeshuv_representation))
    dictionary.update(d3)

    big_arab_yeshuv_representation = list(
        itertools.repeat("Big Non Jew Yeshuv", 5))
    d4 = dict(zip(plot_helper.BIG_NON_JEW_YESHUV_LIST,
                  big_arab_yeshuv_representation))
    dictionary.update(d4)

    huge_cities_representation = list(
        itertools.repeat("Huge Cities", 3))
    d5 = dict(zip(plot_helper.HUGE_YESHUV_LIST,
                  huge_cities_representation))

    dictionary.update(d5)
    df['Yeshuv_Type'] = df['Yeshuv_Type'].astype(str)
    df["Yeshuv_Type"].replace(dictionary, inplace=True)

def corr_heatmap(df, title_grp):

    corr = df.corr(method='pearson')

    corr.columns = ["BZB", "Vote %", "Error %"]
    corr.index = ["BZB", "Vote %", "Error %"]
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax.set_title("Feature Correlation")
        ax = sns.heatmap(corr, annot=True, mask=mask, vmax=.3, square=True,
                         edgecolors='cyan', linewidths=3)
        plt.title(title_grp)


def get_corr_value(df, var1, var2):
    corr_value = df[var1].corr(df[var2])
    return corr_value






def corr_scatter_plots(df, yehuv_types_order):

    import matplotlib.pyplot as plt
    #create big plot fig for all scatter plots:

    fig, axs = plt.subplots(2, 3, figsize=(12, 8), sharex='col',
                            sharey='row',
                            gridspec_kw={'hspace': 0.15, 'wspace': 0.15})
    fig.suptitle('Voting % / Error Vote % Scatter Plot Different Yeshuv SubGroups')
    for ax in axs.flat:
        ax.set(xlabel="Vote %", ylabel='Eror Vote %')
    for ax in axs.flat:
        ax.label_outer()
    # scatter plot




    # total scatter plot
    corr_scatter_plot(df, yehuv_types_order,axs[0,0], "All Kalfis",KnesetVars.Vote_Percent, KnesetVars.Error_Vote_Percent, KnesetVars.Yeshuv_Type )




    huge_cities = df[df["Yeshuv_Type"] == "Huge Cities"]
    corr_scatter_plot(huge_cities, yehuv_types_order, axs[0, 1], "Huge Cities",KnesetVars.Vote_Percent, KnesetVars.Error_Vote_Percent, KnesetVars.Yeshuv_Type)


    small_arab = df[df["Yeshuv_Type"] == "Small Arab Yeshuv"]

    corr_scatter_plot(small_arab, yehuv_types_order, axs[0,2], "Small Arab Yeshuv",KnesetVars.Vote_Percent, KnesetVars.Error_Vote_Percent, KnesetVars.Yeshuv_Type)



    small_jew = df[df["Yeshuv_Type"] == "Small Jew Yeshuv"]

    corr_scatter_plot(small_jew, yehuv_types_order, axs[1,0],"Small Jew Yeshuv",KnesetVars.Vote_Percent, KnesetVars.Error_Vote_Percent, KnesetVars.Yeshuv_Type)




    big_arab = df[df["Yeshuv_Type"] == "Big Non Jew Yeshuv"]

    corr_scatter_plot(big_arab, yehuv_types_order, axs[1,1],"Big Non Jew Yeshuv",KnesetVars.Vote_Percent, KnesetVars.Error_Vote_Percent, KnesetVars.Yeshuv_Type  )




    big_jew = df[df["Yeshuv_Type"] == "Big Jew Yeshuv"]
    corr_scatter_plot(big_jew, yehuv_types_order, axs[1,2],"Big Jew Yeshuv",KnesetVars.Vote_Percent, KnesetVars.Error_Vote_Percent, KnesetVars.Yeshuv_Type  )




def correlation():
    import matplotlib.pyplot as plt
    df = kneset_data.get_kneset_data("22")



    # transform yeshuv types to fewer population groups.
    prepare_new_yeshuv_types_for_scatter_plot(df)
    yehuv_types_order = df["Yeshuv_Type"].unique()
    yehuv_types_order.sort()

    #scatter plot for the different grps:
    corr_scatter_plots(df, yehuv_types_order)

    sns.regplot(x="Vote_Percent", y="Error_Vote_Percent", data=df)

    #subgrps corrr:
    #only kalfis with bzb > 357:
    bzb_df = df[df["BZB"] >=700]
    a = get_corr_value(bzb_df, "Vote_Percent", "BZB" )



