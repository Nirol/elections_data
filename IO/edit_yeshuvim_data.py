import pandas as pd
from numpy import r_

from IO.read_files_helper import KnesetVars, read_metadata_yeshuv_type_to_dict


def _calc_var_dict_from_kneset_df(var_sum_dict, kneset_df, SN_yeshuv):
    for knese_enum_var in KnesetVars:
        if knese_enum_var == KnesetVars.Kalfi_Num:
            kalfi_num = kneset_df.loc[kneset_df['SN'] == SN_yeshuv, KnesetVars.Kalfi_Num.value].count()
            var_sum_dict[KnesetVars.Kalfi_Num] = kalfi_num

        else:
            next_var_sum_per_SN = kneset_df.loc[kneset_df['SN'] == SN_yeshuv, knese_enum_var.value].sum()
            var_sum_dict[knese_enum_var] =  next_var_sum_per_SN


def get_yeshuvim_col_name(Kneset_num, knese_enum_var):
    return Kneset_num +"_" + knese_enum_var.value


def update_yeshuvin_df(var_sum_dict, yeshuvim_df, SN_yeshuv, Kneset_num):
    for knese_enum_var in KnesetVars:
        col_name = get_yeshuvim_col_name(Kneset_num, knese_enum_var)
        yeshuvim_df.at[SN_yeshuv,col_name]=var_sum_dict[knese_enum_var]




def _update_yeshuvim_occurence_per_kneset(yeshuvim_df, kneset_df,  Kneset_num, SN_yeshuv):
    var_sum_dict = {}
    _calc_var_dict_from_kneset_df(var_sum_dict, kneset_df, SN_yeshuv)
    update_yeshuvin_df(var_sum_dict, yeshuvim_df, SN_yeshuv, Kneset_num)


def update_yeshuvim_occurences(kneset_data, yeshuvim_df):
     KNESETS_LIST =kneset_data.get_kneset_list()

     for kneset_num in KNESETS_LIST:
         kneset_df = kneset_data.get_kneset_df(kneset_num)
         list_unique_yeshuvim_SN = kneset_df['SN'].unique()
         for yeshuv_SN in list_unique_yeshuvim_SN:
             _update_yeshuvim_occurence_per_kneset(yeshuvim_df , kneset_df,kneset_num,yeshuv_SN )









def find_in_dict(yeshuve_type_dict, sn_yeshuv):
    key =  str(int(sn_yeshuv))
    if  key in yeshuve_type_dict:
        return yeshuve_type_dict[key]
    return ""


def add_yeshuv_type(yeshuvim):
    yeshuve_type_dict = read_metadata_yeshuv_type_to_dict()

    yeshuvim['Yeshuv_Type'] = yeshuvim.apply(lambda row: find_in_dict(yeshuve_type_dict, row["SN_yeshuv"]), axis=1)
    print("asd")



