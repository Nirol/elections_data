from pandas import Series, DataFrame

import plot_helper
from all_knesets_stats_by_yeshuv_type import \
    gather_data_by_yeshuve_type_group_by
from src.data.data_classes import ResultKnesset
from plot_helper import PlotType
from single_knesset.boxplot import create_boxplot
from single_knesset.plot_single_knesset import single_knesset_all_yeshuv_types

KNESSETS_NUM = "22"

def __get_variable_series(df: DataFrame, pt: PlotType):
    var_series: Series = None
    if pt == pt.Error_Percent:
        var_series = df.Error_Percent
    return var_series



def variable_explore(kneset_data: ResultKnesset, pt: PlotType):

    df = kneset_data.get_kneset_data(KNESSETS_NUM)
    grouped_by_var = gather_data_by_yeshuve_type_group_by(kneset_data,
                                                          plot_helper.PlotType.Error)
    single_knesset_all_yeshuv_types(grouped_by_var[KNESSETS_NUM],
                                    plot_helper.PlotType.Error)

    df["Error_Percent"] =( df["Error_Voters"] / df["Voters"] )*100
    create_boxplot(df,pt)

    #histogram
    var_series = __get_variable_series(df, pt)
    var_series.plot.hist(grid=True, bins=80, rwidth=0.9, range=(0,4.2),
                         color='#607c8e')
    import matplotlib.pyplot as plt
    plt.axvline(var_series.mean(), color='coral', linestyle='dashed',
                linewidth=2, alpha=0.6)

    plt.title('Kalfis Number By Error Vote % ')
    plt.xlabel('Error Vote %')
    plt.ylabel('N Kalfis')
    plt.grid(axis='y', alpha=0.75)
    mu, sigma = var_series.mean(), var_series.std()
    props = dict(boxstyle='round', facecolor='plum', alpha=0.4)
    plt.text(2, 1600,
             r'$\mu={}\%,\ \sigma={}$'.format(round(mu, 2), round(sigma, 2)),
             fontsize=14,
             verticalalignment='top', bbox=props)


def big_cities_non_jew_pop_graph():

    df = pd.read_csv("Data/yeshuv/arab_pop_major_cities.csv")

    # If you have a data frame?
    import squarify

    squarify.plot(sizes=df['Non Jewish Population'], label=df['Yeshuv'], color=["red","green","blue", "grey"], alpha=.5)

    import matplotlib.pyplot as plt
    plt.axis('off')
    plt.show()
