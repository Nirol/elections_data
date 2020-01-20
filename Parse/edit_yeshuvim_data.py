from typing import Dict

from IO.read_files_helper import KnesetVars, read_metadata_yeshuv_type_to_dict
import pandas as pd
from constants import KNESSETS_LIST, get_yeshuvim_col_name


def _calc_var_dict_from_kneset_df(var_sum_dict: Dict, kneset_df: pd.DataFrame,
                                  sn_yeshuv: int) -> None:
    # all knesset vars are summed except number of kalfis.
    for knesset_enum_var in KnesetVars:
        if knesset_enum_var == KnesetVars.Kalfi_Num:
            kalfi_num = kneset_df.loc[kneset_df[
                                          'SN'] == sn_yeshuv, KnesetVars.Kalfi_Num.value].count()
            var_sum_dict[KnesetVars.Kalfi_Num] = kalfi_num

        else:
            next_var_sum_per_sn = kneset_df.loc[
                kneset_df['SN'] == sn_yeshuv, knesset_enum_var.value].sum()
            var_sum_dict[knesset_enum_var] = next_var_sum_per_sn


def _update_yeshuvim_df(var_sum_dict: Dict, yeshuvim_df: pd.DataFrame,
                        sn_yeshuv: int, knesset_num: int) -> None:
    for knesset_enum_var in KnesetVars:
        col_name = get_yeshuvim_col_name(knesset_num, knesset_enum_var)
        yeshuvim_df.at[sn_yeshuv, col_name] = var_sum_dict[knesset_enum_var]

    # collecting different knesset data parameters in a dict for each knesset
    # list of the different parameters is noted in the KnesetVars enum class


def _update_yeshuvim_occurrence_per_kneset(yeshuvim_df: pd.DataFrame,
                                           knesset_df: pd.DataFrame,
                                           knesset_num: str,
                                           sn_yeshuv: int) -> None:
    knesset_parameters_data_dict = {}
    _calc_var_dict_from_kneset_df(knesset_parameters_data_dict, knesset_df,
                                  sn_yeshuv)
    _update_yeshuvim_df(knesset_parameters_data_dict, yeshuvim_df, sn_yeshuv,
                        knesset_num)


def update_yeshuvim_occurrences(kneset_data: pd.DataFrame,
                                yeshuvim_df: pd.DataFrame) -> None:
    for kneset_num in KNESSETS_LIST:
        kneset_df = kneset_data.get_kneset_df(kneset_num)
        list_unique_yeshuvim_sn = kneset_df['SN'].unique()
        for yeshuv_sn in list_unique_yeshuvim_sn:
            _update_yeshuvim_occurrence_per_kneset(yeshuvim_df, kneset_df,
                                                   kneset_num, yeshuv_sn)


def find_in_dict(yeshuve_type_dict: Dict, sn_yeshuv: int) -> str:
    key = str(int(sn_yeshuv))
    if key in yeshuve_type_dict:
        return yeshuve_type_dict[key]
    return ""


def add_yeshuv_type(yeshuvim: pd.DataFrame) -> None:
    yeshuve_type_dict = read_metadata_yeshuv_type_to_dict()
    yeshuvim['Yeshuv_Type'] = yeshuvim.apply(
        lambda row: find_in_dict(yeshuve_type_dict, row["SN_yeshuv"]), axis=1)


def add_yeshuv_type_kneset(kneeset: pd.DataFrame) -> None:
    knesset_type_dict = read_metadata_yeshuv_type_to_dict()
    kneeset['Yeshuv_Type'] = kneeset.apply(
        lambda row: find_in_dict(knesset_type_dict, row["SN"]), axis=1)


def add_voters_percent_per_knesset(yeshuvim: pd.DataFrame) -> None:
    k_list = KNESSETS_LIST
    for knesset in k_list:
        var_name = knesset + "_vote_percent"
        voters_name = knesset + "_" + KnesetVars.Voters
        bzb_name = knesset + "_" + KnesetVars.BZB
        yeshuvim[var_name] = yeshuvim[voters_name] / yeshuvim[bzb_name]
    # yeshuvim['18_vote_percent'] = yeshuvim['18_Voters'] / yeshuvim['18_BZB']
    # yeshuvim['19_vote_percent'] = yeshuvim['19_Voters'] / yeshuvim['19_BZB']
    # yeshuvim['20_vote_percent'] = yeshuvim['20_Voters'] / yeshuvim['20_BZB']
    # yeshuvim['21_vote_percent'] = yeshuvim['21_Voters'] / yeshuvim['21_BZB']
    # yeshuvim['22_vote_percent'] = yeshuvim['22_Voters'] / yeshuvim['22_BZB']


def add_ppk(yeshuvim):
    k_list = KNESSETS_LIST
    for knesset in k_list:
        ppk_name = knesset + "_PPK"
        kalfi_name = knesset + "_" + KnesetVars.Kalfi_Num
        bzb_name = knesset + "_" + KnesetVars.BZB
        yeshuvim[ppk_name] = yeshuvim[bzb_name] / yeshuvim[kalfi_name]

    # yeshuvim['18_PPK'] = yeshuvim['18_BZB'] / yeshuvim['18_Kalfi_Num']
    # yeshuvim['19_PPK'] = yeshuvim['19_BZB'] / yeshuvim[
    #     '19_Kalfi_Num']
    # yeshuvim['20_PPK'] = yeshuvim['20_BZB'] / yeshuvim[
    #     '20_Kalfi_Num']
    # yeshuvim['21_PPK'] = yeshuvim['21_BZB'] / yeshuvim[
    #     '21_Kalfi_Num']
    # yeshuvim['22_PPK'] = yeshuvim['22_BZB'] / yeshuvim[
    #     '22_Kalfi_Num']
