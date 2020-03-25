from matplotlib import pyplot as plt
from plot_helper import HUGE_YESHUV_LIST, BIG_JEW_YESHUV_LIST, NON_JEW_YESHUVS, \
    SMALL_JEW_YESHUV_LIST
import pandas as pd

def validate_all_yeshuves_in_series(b: pd.Series) -> None:
    bigger_100_list = HUGE_YESHUV_LIST
    between_10_100_jew_list = BIG_JEW_YESHUV_LIST
    smaller_yeshuv_jews_list = SMALL_JEW_YESHUV_LIST
    non_jew_yeshuves = NON_JEW_YESHUVS

    total_list = bigger_100_list + between_10_100_jew_list + \
        smaller_yeshuv_jews_list + non_jew_yeshuves

    for yeshuv_code in total_list:
        if yeshuv_code not in b:
            print("adding code={}".format(yeshuv_code))
            b[yeshuv_code] = 0

def _multi_plt_graph(bzb):
    bzb_22 = bzb['22']
    sum_bzb = bzb_22.sum()
    a = bzb_22.divide(sum_bzb, fill_value=0)
    b = a.multiply(
        100)

    validate_all_yeshuves_in_series(b)
    values = [b["120"], b["130"], b["140"], b["150"], b["160"], b['170'],
              b['180'], b['190']]

    bigger_100 = b["120"] + b["130"] + b["140"]
    bigger_100_list = [b["120"], b["130"], b["140"]]

    between_10_100_jew = b["150"] + b["160"] + b['170']
    between_10_100_jew_list = [b["150"], b["160"], b['170']]
    #340
    smaller_yeshuv_jews = b['310'] + b['320'] + b['192'] + b['191'] + b[
        '180'] + b['190'] + b['340'] + b['370'] + b['370'] + b['330'] + b[
                              '193']
    smaller_yeshuv_jews_list = [b['310'] + b['320'] + b['192'] + b['191'],
                                b['180'] + b['190'] + b['340'] + b['370'] + b[
                                    '370'], b['330'] + b['193']]

    non_jew_yeshuvs = b["250"] + b["260"] + b['270'] + b['280'] + b['290'] + b[
        '450'] + b['460']
    non_jew_yeshuvs_list = [b["250"], b["260"], b['270'] + b['280'],
                            b['290'] + b['450'], b['460']]

    group_names = ['Cities > 100K', 'Jews 10K-100K', 'Jews < 10K', 'Non Jews']
    group_size = [bigger_100, between_10_100_jew, smaller_yeshuv_jews,
                  non_jew_yeshuvs]

    subgroup_names = ['Jerusalem', '200K-500K', '100K-200K', '50K-100K',
                      '20K-50K', '10K-20K', 'Moshav', 'Yeshuv', 'Kibbutz',
                      '50K-100K', '20K-50K', '5K-20K', '<5k', 'Bedouin']

    subgroup_size = [b["120"], b["130"], b["140"], b["150"], b["160"],
                     b['170'], b['310'] + b['320'] + b['192'] + b['191'],
                     b['180'] + b['190'] + b['340'] + b['370'] + b['370'],
                     b['330'] + b['193'], b["250"], b["260"],
                     b['270'] + b['280'],
                     b['290'] + b['450'], b['460']]
    a, b, c, d = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens, plt.cm.Oranges]

    # First Ring (outside)
    fig, ax = plt.subplots()
    fig.suptitle("BZB Breakdown by Yeshuv Size & Type")
    ax.axis('equal')
    mypie, _,percent_out = ax.pie(group_size, radius=1, autopct='%1.1f%%', pctdistance=0.85,
                      labels=group_names,labeldistance=1.08,
                      colors=[a(0.6), b(0.6), c(0.6), d(0.6)])
    plt.setp(mypie, width=0.3, edgecolor='white')

    # Second Ring (Inside)
    mypie2, _ = ax.pie(subgroup_size, radius=1 - 0.3,labels =subgroup_names,labeldistance=0,
                       colors=[a(0.5), a(0.4),
                               a(0.3), b(0.5), b(0.4), b(0.3), c(0.5), c(0.4),
                               c(0.3),
                               d(0.5), d(0.4), d(0.3), d(0.2), d(0.1)])

    plt.setp(mypie2, width=0.25, edgecolor='white')
    plt.margins(0, 0)


    handles, labels = ax.get_legend_handles_labels()
    subgroup_names_legs = ['Jerusalem', '200K-500K', '100K-200K', '50K-100K',
                           '20K-50K', '10K-20K', 'Moshav', 'Yeshuv', 'Kibbutz',
                           '50K-100K', '20K-50K', '5K-20K', '<5k', 'Bedouin']
    ax.legend(handles[4:], subgroup_names_legs, loc='best')

    plt.show()
    print("kek")

    # aArray = np.array(bigger_100_list)
    # bArray = np.array(between_5_50_jew_list)
    # cArray = np.array(smaller_yeshuv_jews_list)
    # dArray = np.array(non_jew_yeshuvs_list)
    #
    # xArray = np.array(aArray, bArray, )
    #
    #
    # vals = xArray
    # fig, ax = plt.subplots()
    # size = 0.3
    #   #
    # cmap = plt.get_cmap("tab20c")
    # outer_colors = cmap(np.arange(3) * 4)
    # inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))
    #
    # ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
    #        wedgeprops=dict(width=size, edgecolor='w'))
    #
    # ax.pie(vals.flatten(), radius=1 - size, colors=inner_colors,
    #        wedgeprops=dict(width=size, edgecolor='w'))
    #
    # ax.set(aspect="equal", title='Pie plot with `ax.pie`')
    # plt.show()