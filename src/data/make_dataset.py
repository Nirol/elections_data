from src.data.clean_data import add_yeshuv_type_kneset, _add_vote_percent, \
    _add_error_percent, clean_initial_kneset_data, _remove_extra_cols

from population_statistics import stats_population_kneset_df
from read_files_helper import KnesetData, MetaData, read_data
import pandas as pd
from constants import  KNESET_DF_NUM_META_COLS
from src.data.data_classes import ResultKnesset
from constants import KNESSETS_LIST

def replace_parties_names_per_kneset(kneset_df, parties_dict):
    list_parties_name = kneset_df.columns[KNESET_DF_NUM_META_COLS:]
    for party in list_parties_name:
        if party in parties_dict:
            party_code = parties_dict[party]
            kneset_df.rename(columns={party: party_code}, inplace=True)

        else:
            print("party {} not in dict".format(party))


def update_parties_codes(kneset_data, parties_dict):
    for kneset_num in KNESSETS_LIST:
        kneset_df = kneset_data.get_kneset_df(kneset_num)
        replace_parties_names_per_kneset(kneset_df, parties_dict)


def _read_input_data():
    pd.options.mode.chained_assignment = None
    kneset_data = KnesetData()
    meta_data = MetaData()
    read_data(kneset_data, meta_data)
    return kneset_data, meta_data



if __name__ == "__main__":
    kneset_data, meta_data = _read_input_data()
    update_parties_codes(kneset_data, meta_data.get_parties_dict())

    # clean knesset voting data:

    result_knesset_data = ResultKnesset()
    for kneset_num in KNESSETS_LIST:
        kneset = kneset_data.get_kneset_df(kneset_num)
        clean_kneset = clean_initial_kneset_data(kneset)
        add_yeshuv_type_kneset(clean_kneset)
        _add_vote_percent(clean_kneset)
        _add_error_percent(clean_kneset)
        _remove_extra_cols(clean_kneset)


        stats = stats_population_kneset_df(clean_kneset)
        result_knesset_data.add_kneset(kneset_num, clean_kneset,
                                       stats)

    result_knesset_data.read_meta()
    result_knesset_data.fill_yeshuv()


    #save result knesset as object as well as csv data cleaned.
    result_knesset_data.save_knesset_data()

    #create clean per yeshuv data for later use:


    # yeshuvim_df = meta_data.get_yeshuvim_data()
    # update_yeshuvim_occurrences(kneset_data, yeshuvim_df)
    # #TODO method change test/debug before another use
    # add_voters_percent_per_knesset(yeshuvim_df)
    # # TODO method change test/debug before another use
    # add_ppk(yeshuvim_df)
    # meta_data.save_df_yeshuvim()

