from IO.clean_kneset_data import BzbPerKalfiResult, \
    BzbPerKalfiResult_AboveBZBRange
from IO.edit_yeshuvim_data import add_yeshuv_type_kneset
from IO.read_files_helper import KnesetData
from Questions.GeneralPopStats.population_statistics import stats_population_kneset_df
from Questions.query_helper import filter_df_by_query, GLOBAL_ABOVE_X_PPK_VAR
import pandas as pd


def clean_matafot_hitzoniot(kneset_to_clean):
    matafot_kfolo_yeshuv_sn = [ 875,99999,9999]

    knesett = kneset_to_clean.loc[~
    kneset_to_clean['SN'].isin(matafot_kfolo_yeshuv_sn)]

    return knesett




def _clean_kneset_data_for_task(kneset_to_clean : pd.DataFrame):
    kneset_to_clean = kneset_to_clean.iloc[:, 0:7].copy()
    kneset_to_clean.dropna(inplace=True)
    kneset_to_clean = clean_matafot_hitzoniot(kneset_to_clean)
    kneset_to_clean['vote_percent'] = kneset_to_clean.apply(
        lambda row: 100 * (row.Voters / row.BZB), axis=1)
    add_yeshuv_type_kneset(kneset_to_clean)
    return kneset_to_clean




def _filter_kneset_data_by_query_list(kneset, query_list, threshold ):
    if query_list:
        for query in query_list:
            knesett = filter_df_by_query(kneset, query, threshold)
            kneset = knesett
    else:
        knesett = kneset
    return knesett






    


def bzb_per_kalfi_per_kneset(kneset_data, query_list, bzb_per_kalfi_result : BzbPerKalfiResult, threshold=0) -> None:
    kneset_list = kneset_data.get_kneset_list()
    for kneset_num in kneset_list:

        kneset = kneset_data.get_kneset_df(kneset_num)

        clean_kneset = _clean_kneset_data_for_task(kneset)

        clean_filterd_kneset = _filter_kneset_data_by_query_list(clean_kneset, query_list, threshold )

        stats = stats_population_kneset_df(clean_filterd_kneset)
        bzb_per_kalfi_result.add_kneset(kneset_num, clean_filterd_kneset,
                                        stats)


def bzb_per_kalfi_per_kneset_threshold(kneset_data, query_list,
                                       bzb_per_kalfi_result : BzbPerKalfiResult_AboveBZBRange):
    for threshold in GLOBAL_ABOVE_X_PPK_VAR:
        bzb_per_kalfi_result_per_threshold = BzbPerKalfiResult()
        bzb_per_kalfi_per_kneset(kneset_data,query_list,bzb_per_kalfi_result_per_threshold,threshold)
        bzb_per_kalfi_result.add_threshold_kneset_data(bzb_per_kalfi_result_per_threshold, threshold)


def calc_bzb_per_kalfi_threshold(kneset_data : KnesetData, query_list_of_lists) -> BzbPerKalfiResult_AboveBZBRange:
    bzb_per_kalfi_result  = None    
    for query_list in query_list_of_lists:
            bzb_per_kalfi_result = BzbPerKalfiResult_AboveBZBRange()
            bzb_per_kalfi_per_kneset_threshold(kneset_data, query_list,
                                     bzb_per_kalfi_result)
    return bzb_per_kalfi_result


def calc_bzb_per_kalfi(kneset_data : KnesetData, query_list_of_lists) -> BzbPerKalfiResult:
    bzb_per_kalfi_result  = None
    for query_list in query_list_of_lists:
        bzb_per_kalfi_result = BzbPerKalfiResult()
        bzb_per_kalfi_per_kneset(kneset_data,query_list, bzb_per_kalfi_result)
    return bzb_per_kalfi_result


def set_run() -> BzbPerKalfiResult:
        kneset_data = KnesetData()
        kneset_data.load_kneset_data()

        query_list_of_lists =[]

        query_list1=[]
        query_list_of_lists.append(query_list1)

        bzb_per_kalfi_result = calc_bzb_per_kalfi(kneset_data, query_list_of_lists)

        return bzb_per_kalfi_result