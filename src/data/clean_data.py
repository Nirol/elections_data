from typing import Dict

import pandas as pd

from plot_helper import MAATAFOT_KFOLOT
from read_files_helper import read_metadata_yeshuv_type_to_dict


def __find_in_dict(yeshuve_type_dict: Dict, sn_yeshuv: int) -> str:
    key = str(int(sn_yeshuv))
    if key in yeshuve_type_dict:
        return yeshuve_type_dict[key]
    return ""


def add_yeshuv_type_kneset(kneeset: pd.DataFrame) -> None:
    knesset_type_dict = read_metadata_yeshuv_type_to_dict()
    kneeset['Yeshuv_Type'] = kneeset.apply(
        lambda row: __find_in_dict(knesset_type_dict, row["SN"]), axis=1)


def __clean_matafot_hitzoniot(knesset_to_clean: pd.DataFrame) -> pd.DataFrame:
    matafot_kfolo_yeshuv_sn = MAATAFOT_KFOLOT
    knesset = knesset_to_clean.loc[
        ~knesset_to_clean['SN'].isin(matafot_kfolo_yeshuv_sn)]
    return knesset


def _add_vote_percent(kneset_to_clean: pd.DataFrame) -> None:
    kneset_to_clean['Vote_Percent'] = kneset_to_clean.apply(
        lambda row: 100 * (row.Voters / row.BZB), axis=1)


def _add_error_percent(kneset_to_clean: pd.DataFrame) -> None:
    kneset_to_clean['Error_Vote_Percent'] = 100*kneset_to_clean['Error_Voters'].divide(kneset_to_clean['Voters'])

def _remove_extra_cols(kneset_to_clean: pd.DataFrame) -> None:
    cols_to_remove = [1]
    kneset_to_clean.drop(cols_to_remove, axis=1, inplace=True)




def clean_initial_kneset_data(kneset_to_clean: pd.DataFrame) -> pd.DataFrame:
    kneset_to_clean = kneset_to_clean.iloc[:, 0:7].copy()
    kneset_to_clean.dropna(inplace=True)
    kneset_to_clean = __clean_matafot_hitzoniot(kneset_to_clean)
    return kneset_to_clean