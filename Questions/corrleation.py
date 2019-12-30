import math
from enum import Enum

from scipy.stats import pearsonr
import numpy as np
import matplotlib.pyplot as plt
_ARABS_YESHUV_TYPES_LIST = ["250", "260", "270", "280", "290", "440", "450"]
_BADUIM = [460]

class Query(Enum):
    Total = 1
    No_Single_Kalfi = 2

    Arabs_Only = 3
    Arabs_Only_No_Single_Kalfi = 4
    Non_Arabs_Only = 5
    Non_Arabs_Only_No_Single_Kalfi = 6
    Above_Two_Kalfi = 7
    Above_Two_Kalfi_Arab_Only = 8
    Above_Two_Kalfi_Non_Arab_Only = 9
    Ppk_Above_550 = 10


def _are_vars_valid(i_ppk, i_vote_percent_values):
    if i_ppk == 0 or i_vote_percent_values == 0 or np.isnan(i_ppk) or np.isinf(
            i_ppk) or np.isnan(i_vote_percent_values) or np.isinf(
        i_vote_percent_values) or math.isnan(i_ppk) or math.isnan(
        i_vote_percent_values):
        return False
    return True


def update_total_dict(ppk_vote_percent_total_dict,row):
    ppk_values, vote_percent_values, bzb_values, voters_values = _get_ppk_vote_percent_values(row)

    for i in range(5):
        i_ppk = ppk_values[i]
        i_vote_percent_values = vote_percent_values[i]
        i_bzb =
        i_voters =
        if not _are_vars_valid(i_ppk, i_vote_percent_values):

            print("Found a problem with yeshuv {}".format(sn))
        else:
            ppk_vote_percent_total_dict['SN_yeshuv'].append(sn)
            ppk_vote_percent_total_dict['ppk'].append(i_ppk)
            ppk_vote_percent_total_dict['vote_percent'].append(
                100 * i_vote_percent_values)

            ppk_vote_percent_total_dict['voters'].append(bzb)


def is_yeshuv_type_arab(yeshuv_type):
    if yeshuv_type in _ARABS_YESHUV_TYPES_LIST:
        return True
    return False

def is_yeshuv_single_kalfi(row):
    if row["18_Kalfi_Num"] == 1 and row["19_Kalfi_Num"] == 1 and row[
        "20_Kalfi_Num"] == 1 and row["21_Kalfi_Num"] == 1 and row[
        "22_Kalfi_Num"] == 1:
        return True
    else:
        return False


def is_yeshuv_above_two_kalfi(row):
    if row["18_Kalfi_Num"] > 2 and row["19_Kalfi_Num"] > 2 and row[
        "20_Kalfi_Num"] > 2 and row["21_Kalfi_Num"] > 2 and row[
        "22_Kalfi_Num"] > 2:
        return True
    else:
        return False


def is_sn_row_in_query(row, query):
    if query == Query.Total:
        return True

    elif query == Query.No_Single_Kalfi:
        if not is_yeshuv_single_kalfi(row) :
            return True
        return False
    elif query == Query.Arabs_Only:
        if is_yeshuv_type_arab(row["Yeshuv_Type"]):
            return True
        return False
    elif query == Query.Arabs_Only_No_Single_Kalfi:
        if is_yeshuv_type_arab(row["Yeshuv_Type"]) and not is_yeshuv_single_kalfi(row):
            return True
        return False
    elif query == Query.Above_Two_Kalfi:
        if is_yeshuv_above_two_kalfi(row):
            return True
        return False
    elif query == Query.Above_Two_Kalfi_Arab_Only:
        if is_yeshuv_above_two_kalfi(row) and is_yeshuv_type_arab(row["Yeshuv_Type"]):
            return True
        return False
    elif query == Query.Above_Two_Kalfi_Non_Arab_Only:
        if is_yeshuv_above_two_kalfi(row) and not is_yeshuv_type_arab(row["Yeshuv_Type"]):
            return True
        return False
    elif query == Query.Ppk_Above_550:
        ppk_values = row[['18_PPK', '19_PPK', '20_PPK', '21_PPK',
                          '22_PPK']].values.tolist()
        for ppk in ppk_values:
            if ppk < 550:
                return False
        return True




def _get_ppk_vote_percent_values(row):
    ppk_values = row[['18_PPK', '19_PPK', '20_PPK', '21_PPK',
                      '22_PPK']].values.tolist()
    vote_percent_values = row[
        ['18_vote_percent', '19_vote_percent', '20_vote_percent',
         '21_vote_percent', '22_vote_percent']].values.tolist()

    bzb_values = row[
        ['18_BZB', '19_BZB', '20_BZB',
         '21_BZB', '22_BZB']].values.tolist()




    sn = row["SN_yeshuv"]
    bzb = row["BZB"]
    return ppk_values, vote_percent_values



def corr_per_query(yeshuvim, ppk_vote_percent_total_dict, query):
    for index, row in yeshuvim.iterrows():
        if is_sn_row_in_query(row, query):
            update_total_dict(ppk_vote_percent_total_dict, row)



def _calculate_pearson_for_dict(ppk_vote_percent_total_dict):

    pearson_res = pearsonr(ppk_vote_percent_total_dict['ppk'],
                           ppk_vote_percent_total_dict['vote_percent'])
    print(pearson_res)


def _scatter_plot(ppk_vote_percent_total_dict):

    x = ppk_vote_percent_total_dict['ppk']
    y = ppk_vote_percent_total_dict['vote_percent']
    plt.scatter(x, y, alpha=0.5)
    plt.title('Scatter plot pythonspot.com')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def _corr_all_data(yeshuvim):

    ppk_vote_percent_total_dict = {'SN_yeshuv': [], 'ppk': [],
                                   'vote_percent': [], 'BZB': 0}
    corr_per_query(yeshuvim, ppk_vote_percent_total_dict, Query.Ppk_Above_550)
    _calculate_pearson_for_dict(ppk_vote_percent_total_dict)
    _scatter_plot(ppk_vote_percent_total_dict)








def _calculate_cor_per_sn(yeshuvim, query, corr_ppk_vote_percent):
    for index, row in yeshuvim.iterrows():
        sn = row["SN_yeshuv"]
        if is_sn_row_in_query(row, query):
            ppk_values, vote_percent_values = _get_ppk_vote_percent_values(row)
            if np.isnan(ppk_values).any() or np.isnan(
                    vote_percent_values).any():
                pass
            else:
                pearson_res = pearsonr(ppk_values, vote_percent_values)
                sn_corr = [sn, pearson_res[0]]
                corr_ppk_vote_percent.append(sn_corr)


def _analyze_corr_per_sn_result(corr_per_sn):
    pass


def _corr_per_sn(yeshuvim,query):
    corr_ppk_vote_percent = []
    _calculate_cor_per_sn(yeshuvim,query,corr_ppk_vote_percent)
    _analyze_corr_per_sn_result(corr_ppk_vote_percent)







def calculate_corrleation(yeshuvim):
    #_corr_per_sn(yeshuvim, Query.Total)
    _corr_all_data(yeshuvim)
    print("asd")


