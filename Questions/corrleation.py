import math

from scipy.stats import pearsonr
import numpy as np
import matplotlib.pyplot as plt

from Questions.query_helper import is_yeshuv_type_arab, is_yeshuv_single_kalfi, \
    is_yeshuv_above_two_kalfi, GLOBAL_ABOVE_X_PPK_VAR, Query


def _are_vars_valid(i_ppk, i_vote_percent_values):
    if i_ppk == 0 or i_vote_percent_values == 0 or np.isnan(i_ppk) or np.isinf(
            i_ppk) or np.isnan(i_vote_percent_values) or np.isinf(
        i_vote_percent_values) or math.isnan(i_ppk) or math.isnan(
        i_vote_percent_values):
        return False
    return True


def update_total_dict(ppk_vote_percent_total_dict,row):
    ppk_values, vote_percent_values, bzb_values, voters_values = _get_ppk_vote_percent_values(row)
    sn = row["SN_yeshuv"]
    for i in range(5):
        i_ppk = ppk_values[i]
        i_vote_percent_values = vote_percent_values[i]
        i_bzb = bzb_values[i]
        i_voters = voters_values[i]
        if not _are_vars_valid(i_ppk, i_vote_percent_values):

            print("Yeshuv {} excluded due to missing information".format(sn))
        else:
            if i_ppk > 10000:
                print("ppk error above 10000")
            ppk_vote_percent_total_dict['SN_yeshuv'].append(sn)
            ppk_vote_percent_total_dict['ppk'].append(i_ppk)
            ppk_vote_percent_total_dict['vote_percent'].append(
                100 * i_vote_percent_values)
            ppk_vote_percent_total_dict['BZB']  = ppk_vote_percent_total_dict['BZB']  + i_bzb
            ppk_vote_percent_total_dict['voters'] = ppk_vote_percent_total_dict['voters']  + i_voters


def is_sn_row_in_query(row, query):
    if query == Query.No_Single_Kalfi:
        if not is_yeshuv_single_kalfi(row) :
            return True
        return False
    elif query == Query.Arabs_Only:
        if is_yeshuv_type_arab(row["Yeshuv_Type"]):
            return True
        return False
    elif query == Query.Non_Arabs_Only:
        if not is_yeshuv_type_arab(row["Yeshuv_Type"]):
            return True
        return False
    elif query == Query.Above_Two_Kalfi:
        if is_yeshuv_above_two_kalfi(row):
            return True
        return False
    elif query == Query.Ppk_Above_X:
        ppk_values = row[['18_PPK', '19_PPK', '20_PPK', '21_PPK',
                          '22_PPK']].values.tolist()
        for ppk in ppk_values:
            if ppk < _GLOBAL_ABOVE_X_PPK_VAR:
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
    voters_values = row[
        ['18_Voters', '19_Voters', '20_Voters',
         '21_Voters', '22_Voters']].values.tolist()
    return ppk_values, vote_percent_values, bzb_values, voters_values


def is_sn_row_fit_query_list(row, query_list):
    for query in query_list:
        if  not is_sn_row_in_query(row,query):
            return False
    return True


def corr_per_query(yeshuvim, ppk_vote_percent_total_dict, query_list):
    for index, row in yeshuvim.iterrows():
        if is_sn_row_fit_query_list(row, query_list):
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


def _stats_population_in_dict(ppk_vote_percent_total_dict):

    num_samples = len(ppk_vote_percent_total_dict['SN_yeshuv'])
    num_unique_yeshuvim = len(set(ppk_vote_percent_total_dict['SN_yeshuv']))
    total_bzb= ppk_vote_percent_total_dict['BZB']
    total_voters = ppk_vote_percent_total_dict['voters']
    total_vote_percent = total_voters/total_bzb
    avg_bzb_per_yeshuv =   total_bzb/ (5*num_unique_yeshuvim)
    print("num_samples ={}".format(num_samples))
    print("num_unique_yeshuvim ={}".format(num_unique_yeshuvim))
    print("total_bzb ={}".format(total_bzb))
    print("total_voters ={}".format(total_voters))
    print("total_vote_percent ={}".format(total_vote_percent))
    print("avg_bzb_per_yeshuv ={}".format(avg_bzb_per_yeshuv))




def _corr_all_data(yeshuvim):

    ppk_vote_percent_total_dict = {'SN_yeshuv': [], 'ppk': [],
                                   'vote_percent': [], 'BZB': 0, 'voters' :0}

    query_list=[Query.No_Single_Kalfi, Query.Ppk_Above_X]

    corr_per_query(yeshuvim, ppk_vote_percent_total_dict, query_list)
    _stats_population_in_dict(ppk_vote_percent_total_dict)
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
    _corr_per_sn(yeshuvim, Query.Total)
    #_corr_all_data(yeshuvim)


