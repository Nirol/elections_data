from IO.read_files_helper import KnesetVars, read_metadata_yeshuv_type_to_dict
import pandas as pd

from constants import KNESSETS_LIST


def _calc_var_dict_from_kneset_df(var_sum_dict, kneset_df, SN_yeshuv):
    for knese_enum_var in KnesetVars:
        if knese_enum_var == KnesetVars.Kalfi_Num:
            kalfi_num = kneset_df.loc[kneset_df[
                                          'SN'] == SN_yeshuv, KnesetVars.Kalfi_Num.value].count()
            var_sum_dict[KnesetVars.Kalfi_Num] = kalfi_num

        else:
            next_var_sum_per_SN = kneset_df.loc[
                kneset_df['SN'] == SN_yeshuv, knese_enum_var.value].sum()
            var_sum_dict[knese_enum_var] = next_var_sum_per_SN


def get_yeshuvim_col_name(Kneset_num, knese_enum_var):
    return Kneset_num + "_" + knese_enum_var.value


def update_yeshuvin_df(var_sum_dict, yeshuvim_df, SN_yeshuv, Kneset_num):
    for knese_enum_var in KnesetVars:
        col_name = get_yeshuvim_col_name(Kneset_num, knese_enum_var)
        yeshuvim_df.at[SN_yeshuv, col_name] = var_sum_dict[knese_enum_var]


def _update_yeshuvim_occurrence_per_kneset(yeshuvim_df, knesset_df, knesset_num,
                                           sn_yeshuv):
    var_sum_dict = {}
    _calc_var_dict_from_kneset_df(var_sum_dict, knesset_df, sn_yeshuv)
    update_yeshuvin_df(var_sum_dict, yeshuvim_df, sn_yeshuv, knesset_num)


def update_yeshuvim_occurences(kneset_data, yeshuvim_df):
    for kneset_num in KNESSETS_LIST:
        kneset_df = kneset_data.get_kneset_df(kneset_num)
        list_unique_yeshuvim_SN = kneset_df['SN'].unique()
        for yeshuv_SN in list_unique_yeshuvim_SN:
            _update_yeshuvim_occurrence_per_kneset(yeshuvim_df, kneset_df,
                                                   kneset_num, yeshuv_SN)


def find_in_dict(yeshuve_type_dict, sn_yeshuv):
    key = str(int(sn_yeshuv))
    if key in yeshuve_type_dict:
        return yeshuve_type_dict[key]
    return ""


def add_yeshuv_type(yeshuvim):
    yeshuve_type_dict = read_metadata_yeshuv_type_to_dict()
    yeshuvim['Yeshuv_Type'] = yeshuvim.apply(
        lambda row: find_in_dict(yeshuve_type_dict, row["SN_yeshuv"]), axis=1)


def find_in_dict(yeshuve_type_dict, sn_yeshuv):
    key = str(int(sn_yeshuv))
    if key in yeshuve_type_dict:
        return yeshuve_type_dict[key]
    return ""


def add_yeshuv_type_kneset(kneset: pd.DataFrame):
    kneset_type_dict = read_metadata_yeshuv_type_to_dict()
    kneset['Yeshuv_Type'] = kneset.apply(
        lambda row: find_in_dict(kneset_type_dict, row["SN"]), axis=1)


def add_voters_percent_per_knesent(yeshuvim):
    yeshuvim['18_vote_percent'] = yeshuvim['18_Voters'] / yeshuvim['18_BZB']
    yeshuvim['19_vote_percent'] = yeshuvim['19_Voters'] / yeshuvim['19_BZB']
    yeshuvim['20_vote_percent'] = yeshuvim['20_Voters'] / yeshuvim['20_BZB']
    yeshuvim['21_vote_percent'] = yeshuvim['21_Voters'] / yeshuvim['21_BZB']
    yeshuvim['22_vote_percent'] = yeshuvim['22_Voters'] / yeshuvim['22_BZB']


def add_PPK(yeshuvim):
    yeshuvim['18_PPK'] = yeshuvim['18_BZB'] / yeshuvim['18_Kalfi_Num']
    yeshuvim['19_PPK'] = yeshuvim['19_BZB'] / yeshuvim[
        '19_Kalfi_Num']
    yeshuvim['20_PPK'] = yeshuvim['20_BZB'] / yeshuvim[
        '20_Kalfi_Num']
    yeshuvim['21_PPK'] = yeshuvim['21_BZB'] / yeshuvim[
        '21_Kalfi_Num']
    yeshuvim['22_PPK'] = yeshuvim['22_BZB'] / yeshuvim[
        '22_Kalfi_Num']
