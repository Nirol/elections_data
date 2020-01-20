from enum import Enum
import pandas as pd


class PopVars(Enum):
    Num_Kalfi = 1
    Unq_Yeshuv = 2
    Bzb = 3
    Voters = 4
    AvgBzb = 5
    VotePercent = 6



class PopulationStats(object):
    def __init__(self, pearson, tau, vote_percent_std):
        self.pearson = pearson
        self.tau = tau
        self.vote_percent_std = vote_percent_std


class PopulationInfo(object):
    def __init__(self, num_kalfis_total, num_unique_yeshuvim, total_bzb,
                 total_voters, pop_stats):
        self.Num_Kalfi = num_kalfis_total
        self.Unq_Yeshuv = num_unique_yeshuvim
        self.Bzb = total_bzb
        self.Voters = total_voters
        self.VotePercent = total_voters / total_bzb
        self.AvgBzb = total_bzb / num_kalfis_total
        self.pop_stats = pop_stats


    def get_var(self, pop_var_enum: PopVars):
        object_dict = self.__dict__
        return object_dict[pop_var_enum.name]

    def get_vote_percent(self):
        return 100 * self.VotePercent

    def stats_to_row(self):
        return [self.Bzb, self.Num_Kalfi, self.Unq_Yeshuv, self.Voters,
                self.VotePercent, self.vote_percent_std, self.AvgBzb,
                self.pearson[0], self.pearson[1]]


class ResultKnesset():
    def __init__(self):
        self.knessets_dict = {}

    def add_kneset(self, kneset_num: str, kneset: pd.DataFrame,
                   kneset_stats: PopulationInfo) -> None:
        tmp_kneset_dict = {"num": kneset_num,
                           'data': kneset,
                           'stats': kneset_stats
                           }
        self.knessets_dict[kneset_num] = tmp_kneset_dict

    def get_kneset_data(self, kneset_num: int) -> pd.DataFrame:
        return self.knessets_dict[kneset_num]['data']

    def get_kneset_stats(self, kneset_num: int) -> PopulationInfo:
        return self.knessets_dict[kneset_num]['stats']

    def get_single_kneset_dict(self, kneset_num: str):
        return self.knessets_dict[kneset_num]

    def get_var_per_kneset(self, pop_var: PopVars):
        ans = []
        for k in self.knessets_dict.keys():
            pop_stats = self.knessets_dict[k]['stats']
            ans.append(pop_stats.get_var(pop_var))
        return ans


class ThresholdsResultKnesset():
    def __init__(self):
        self.threshold_kneset_dict_rang = {}

    def add_threshold_kneset_data(self,
                                  bzb_per_kalfi_result_per_threshold: ResultKnesset,
                                  threshold):
        self.threshold_kneset_dict_rang[
            threshold] = bzb_per_kalfi_result_per_threshold

    def get_threshold_kneset_dict(self, threshold: int) -> ResultKnesset:
        return self.threshold_kneset_dict_rang[threshold]
