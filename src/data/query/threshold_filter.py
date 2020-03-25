from read_files_helper import KnesetData
from src.data.data_classes import ThresholdsResultKnesset, ResultKnesset



def bzb_per_kalfi_per_kneset_threshold(kneset_data, query_list,
                                       bzb_per_kalfi_result: ThresholdsResultKnesset):
    from constants import THRESHOLD_LIST
    for threshold in THRESHOLD_LIST:
        bzb_per_kalfi_result_per_threshold = ResultKnesset()
        from src.data.query.filter import initial_clean_and_filtering
        initial_clean_and_filtering(kneset_data, query_list,
                                    bzb_per_kalfi_result_per_threshold, threshold)
        bzb_per_kalfi_result.add_threshold_kneset_data(
            bzb_per_kalfi_result_per_threshold, threshold)


def calc_bzb_per_kalfi_threshold(kneset_data: KnesetData,
                                 query_list_of_lists) -> ThresholdsResultKnesset:
    bzb_per_kalfi_result = None
    for query_list in query_list_of_lists:
        bzb_per_kalfi_result = ThresholdsResultKnesset()
        bzb_per_kalfi_per_kneset_threshold(kneset_data, query_list,
                                           bzb_per_kalfi_result)
    return bzb_per_kalfi_result



def filter_by_query(kneset_data, query_list) -> ThresholdsResultKnesset:

    query_list_of_lists = []
    query_list_of_lists.append(query_list)
    thresholds_knesset = calc_bzb_per_kalfi_threshold(kneset_data, query_list_of_lists)
    return thresholds_knesset






