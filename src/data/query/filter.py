from src.data.data_classes import ResultKnesset
from read_files_helper import KnesetData
from src.data.query.query_helper import filter_df_by_query
import pandas as pd


# TODO test/debuf before another use



def __filter_kneset_data_by_query_list(knesset, query_list,
                                      threshold) -> pd.DataFrame:
    knessett = None
    if query_list:
        for query in query_list:
            knessett = filter_df_by_query(knesset, query, threshold)
    return knessett


def initial_clean_and_filtering(kneset_data, query_list,
                                result_knesset_data: ResultKnesset,
                                threshold=0) -> None:
    from constants import KNESSETS_LIST
    kneset_list = KNESSETS_LIST
    for kneset_num in kneset_list:
        kneset = kneset_data.get_kneset_df(kneset_num)
        if query_list:
            kneset = __filter_kneset_data_by_query_list(kneset,
                                                                     query_list,
                                                                     threshold)

        stats = None
        result_knesset_data.add_kneset(kneset_num, kneset,
                                       stats)


def __clean_filter_per_query(kneset_data: KnesetData,
                           query_list_of_lists) -> ResultKnesset:
    knesset_results_clean = None
    for query_list in query_list_of_lists:
        knesset_results_clean = ResultKnesset()
        initial_clean_and_filtering(kneset_data, query_list, knesset_results_clean)

    # add general yeshuv name kalfi address data to ResultKnesset
    knesset_results_clean.read_meta()
    return knesset_results_clean




def filter_by_query(kneset_data: KnesetData, query_list) -> ResultKnesset:

    query_list_of_lists = []
    query_list_of_lists.append(query_list)
    knesset_results_clean_filtered = __clean_filter_per_query(kneset_data, query_list_of_lists)
    return knesset_results_clean_filtered





