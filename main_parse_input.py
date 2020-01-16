from IO.read_files_helper import KnesetData, MetaData, read_data
from Parse.edit_yeshuvim_data import update_yeshuvim_occurences, \
    add_voters_percent_per_knesent, add_PPK
import pandas as pd

from constants import KNESSETS_LIST, KNESET_DF_NUM_META_COLS


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
    pd.options.display.float_format = '{:,.0f}'.format
    kneset_data = KnesetData()
    meta_data = MetaData()
    read_data(kneset_data, meta_data)
    return kneset_data, meta_data



if __name__ == "__main__":
    kneset_data, meta_data = _read_input_data()
    update_parties_codes(kneset_data, meta_data.get_parties_dict())
    kneset_data.save_clean_knesset_df()

    yeshuvim_df = meta_data.get_yeshuvim_data()

    update_yeshuvim_occurences(kneset_data, yeshuvim_df)
    add_voters_percent_per_knesent(yeshuvim_df)
    add_PPK(yeshuvim_df)
    meta_data.save_dataframe_yesuhvim()

