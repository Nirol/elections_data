import matplotlib.pyplot as plt
from scipy.stats import pearsonr


def _scatter_plot_population(kneset_df : pd.DataFrame):

    x = kneset_df['BZB']
    y = kneset_df['vote_percent']
    plt.scatter(x, y, alpha=0.5)
    plt.title('vote percent by BZB')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def _calculate_bzb_vote_percent_pearson(bzb_col, vote_percent_col):

    pearson_res = pearsonr(bzb_col,
                           vote_percent_col)
    return pearson_res


class PopulationStats(object):
    # parameterized constructor
    def __init__(self,num_kalfis_total, num_unique_yeshuvim, total_bzb,total_voters):
        self.total_num_kalfi = num_kalfis_total
        self.unique_yeshuv = num_unique_yeshuvim
        self.total_bzb = total_bzb
        self.total_voters = total_voters
        self.total_vote_percent = total_voters / total_bzb
        self.avg_bzb_per_yeshuv = total_bzb / num_kalfis_total




        #
        #
        # print("num_kalfis_total ={}".format(num_kalfis_total))
        # print("num_unique_yeshuvim ={}".format(num_unique_yeshuvim))
        # print("total_bzb ={}".format(total_bzb))
        # print("total_voters ={}".format(total_voters))
        # print("total_vote_percent ={}".format(total_vote_percent))
        # print("avg_bzb_per_yeshuv ={}".format(avg_bzb_per_yeshuv))
        #