from enum import Enum

import pandas as pd
from matplotlib import pyplot as plt



class PopVars(Enum):
    Num_Kalfi = 1
    Unq_Yeshuv = 2
    Bzb = 3
    Voters = 4
    AvgBzb = 5
    VotePercent = 6


class PopulationStats(object):
    # parameterized constructor

    def __init__(self,num_kalfis_total, num_unique_yeshuvim, total_bzb,total_voters, pearson, tau):
        self.Num_Kalfi = num_kalfis_total
        self.Unq_Yeshuv = num_unique_yeshuvim
        self.Bzb = total_bzb
        self.Voters = total_voters
        self.VotePercent = total_voters / total_bzb
        self.AvgBzb = total_bzb / num_kalfis_total
        self.pearson = pearson
        self.tau = tau

    def get_var(self, pop_var_enum: PopVars):
        object_dict = self.__dict__
        return object_dict[pop_var_enum.name]



    def get_vote_percent(self):
        return 100*self.total_vote_percent





class BzbPerKalfiResult():
    def __init__(self ):
        self.knesets_dict = {}
    #todo fix multi functions into a single getter
    def add_kneset(self, kneset_num :str, kneset : pd.DataFrame, kneset_stats: PopulationStats):
        tmp_kneset_dict = {"num": kneset_num,
                'data': kneset,
                'stats': kneset_stats
                }
        self.knesets_dict[kneset_num] = tmp_kneset_dict


    def get_kneset_data(self, kneset_num):
        return self.knesets_dict[kneset_num]['data']


    def get_single_kneset_dict(self,kneset_num :str ):
        return self.knesets_dict[kneset_num]


    def get_var_per_kneset(self, pop_var :PopVars ):
        ans = []
        for k in self.knesets_dict.keys():
            pop_stats = self.knesets_dict[k]['stats']
            ans.append(pop_stats.get_var(pop_var))
        return ans

    #
    #
    # def get_avg_bzb_per_kneset(self):
    #     ans = []
    #     for k in self.knesets_dict.keys():
    #         pop_stats = self.knesets_dict[k]['stats']
    #         ans.append(pop_stats.get_var(PopVars.AvgBzb))
    #     return ans
    #
    # def get_vote_percent_per_kneset(self):
    #     ans = []
    #     for k in self.knesets_dict.keys():
    #         pop_stats = self.knesets_dict[k]['stats']
    #         ans.append(pop_stats.get_vote_percent(PopVars.AvgBzb))
    #     return ans
    #
    # def get_voters_per_kneset(self):
    #     ans = []
    #     for k in self.knesets_dict.keys():
    #         pop_stats = self.knesets_dict[k]['stats']
    #         ans.append(pop_stats.get_voters())
    #     return ans


class BzbPerKalfiResult_AboveBZBRange():
    def __init__(self):
        self.threshold_kneset_dict_rang = {}
    def add_threshold_kneset_data(self, bzb_per_kalfi_result_per_threshold: BzbPerKalfiResult,
                                  threshold):
        self.threshold_kneset_dict_rang[threshold] = bzb_per_kalfi_result_per_threshold


    def get_plot_idx_by_threshold(self, threshold):
        plot_title = "{}+ BZB".format(threshold)
        if threshold == 150:
            return 0,0, plot_title
        elif threshold == 200:
            return 0,1, plot_title
        elif threshold == 250:
            return 0,2, plot_title
        elif threshold == 300:
            return 1,0, plot_title
        elif threshold == 350:
            return 1,1, plot_title
        elif threshold == 400:
            return 1,2 ,plot_title
        elif threshold == 450:
            return 2,0, plot_title
        elif threshold == 500:
            return 2, 1,plot_title
        elif threshold == 550:
            return 2,2,plot_title


    def add_to_plot(self, threshold, bzb, vote_percent, axs):
        i,j, plot_title = self.get_plot_idx_by_threshold(threshold)
        axs[i, j].scatter(bzb, vote_percent, alpha=0.5)
        axs[i, j].set_title(plot_title, fontsize= 10)



    def plot_all_scatter(self ):
        threshold_kneset_dict_rang =self.threshold_kneset_dict_rang
        kneset_num = "18"
        # fig, (ax150, ax200, ax250, ax300, ax350, ax400, ax450, ax500,
        #       ax550) = plt.subplots(9, sharex=True)
        fig, axs = plt.subplots(3, 3, sharex='col', sharey='row',
                                gridspec_kw={'hspace': 0.15, 'wspace': 0.15})
        fig.suptitle('Voting % By Kalfi BZB ')
        for threshold, v in threshold_kneset_dict_rang.items():
            bzb_per_kalfi_result =  threshold_kneset_dict_rang[threshold]
            single_kneset_dict = bzb_per_kalfi_result.get_single_kneset_dict(kneset_num)
            bzb = single_kneset_dict["data"]["BZB"]
            vote_percent = single_kneset_dict["data"]["vote_percent"]
            self.add_to_plot(threshold, bzb, vote_percent, axs)


            # for ax in axs.flat:
            #     ax.label_outer()

        plt.show()


