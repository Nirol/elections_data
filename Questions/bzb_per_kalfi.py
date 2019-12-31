from scipy.stats import pearsonr

from IO.read_files_helper import KnesetData, read_metadata_yeshuv_type_to_dict
from Questions.population_statistics import PopulationStats
from Questions.query_helper import Query, filter_df_by_query
import pandas as pd



def find_in_dict(yeshuve_type_dict, sn_yeshuv):
    key =  str(int(sn_yeshuv))
    if  key in yeshuve_type_dict:
        return yeshuve_type_dict[key]
    return ""



def add_yeshuv_type(kneset : pd.DataFrame):
    kneset_type_dict = read_metadata_yeshuv_type_to_dict()
    kneset['Yeshuv_Type'] = kneset.apply(lambda row: find_in_dict(kneset_type_dict, row["SN"]), axis=1)




def _clean_kneset_data_for_task(kneset : pd.DataFrame):
    kneset = kneset.iloc[:, 1:7]
    kneset.dropna(inplace=True)
    kneset['vote_percent'] = kneset.apply(
        lambda row: 100 * (row.Voters / row.BZB), axis=1)
    add_yeshuv_type(kneset)

class BzbPerKalfiResult(object):
    pass


def _filter_kneset_data_by_query_list(kneset_num, kneset, query_list,bzb_per_kalfi_result :BzbPerKalfiResult ):
    for query in query_list:
        kneset = filter_df_by_query(kneset, query)
        print("Query: {}, filtered kalfi number down to:{}".format(query,len(kneset['SN'])))

    bzb_per_kalfi_result.
    kneset_stats = _stats_population_kneset_df(kneset)
    pearson = _calculate_pearson_for_dict(kneset)
    _scatter_plot(kneset)



def calc_bzb_per_kalfi(kneset_data : KnesetData, query_list_of_lists):
    bzb_per_kalfi_result = BzbPerKalfiResult()
    kneset_list = kneset_data.get_kneset_list()
    for kneset_num in kneset_list:
        print("Now running Kneset: {}".format(kneset_num))
        kneset = kneset_data.get_kneset_df(kneset_num)
        _clean_kneset_data_for_task(kneset)
        for query_list in query_list_of_lists:
            print("Query List: {}".format(query_list))
            _filter_kneset_data_by_query_list(kneset_num, kneset, query_list, bzb_per_kalfi_result)





def _stats_population_kneset_df(kneset_df):

    num_kalfis_total = len(kneset_df['SN'])
    num_unique_yeshuvim = len(set(kneset_df['SN']))
    total_bzb= kneset_df['BZB'].sum()
    total_voters = kneset_df['Voters'].sum()
    filtered_population_stats = PopulationStats(num_kalfis_total, num_unique_yeshuvim, total_bzb,total_voters )
    return filtered_population_stats






def set_run():
        kneset_data = KnesetData()
        kneset_data.load_kneset_data()

        query_list_of_lists =[]

        query_list1=[Query.Arabs_Only, Query.Kalfi_Above_X]
        query_list_of_lists.append(query_list1)

        bzb_per_kalfi_result = calc_bzb_per_kalfi(kneset_data, query_list_of_lists)