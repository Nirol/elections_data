from enum import Enum
import pandas as pd


_ARABS_YESHUV_TYPES_LIST = ["250", "260", "270", "280", "290", "440", "450", "460"]
_BADUIM = [460]
_GLOBAL_ABOVE_X_PPK_VAR = 250


class Query(Enum):
    No_Single_Kalfi = 1
    Arabs_Only = 2
    Non_Arabs_Only = 3
    Above_Two_Kalfi = 4
    Kalfi_Above_X = 5

def filter_df_by_query(kneset: pd.DataFrame,query):
    if query == Query.No_Single_Kalfi:
        knesett = kneset.groupby("SN").filter(lambda x: len(x) > 1)
    elif query == Query.Above_Two_Kalfi:
        knesett = kneset.groupby("SN").filter(lambda x: len(x) > 2)
    elif query == Query.Arabs_Only:
        knesett = kneset.loc[kneset['Yeshuv_Type'].isin(_ARABS_YESHUV_TYPES_LIST)]
    elif query == Query.Non_Arabs_Only:
        knesett = kneset.loc[~
            kneset['Yeshuv_Type'].isin(_ARABS_YESHUV_TYPES_LIST)]
    elif query == Query.Kalfi_Above_X:
        knesett = kneset.loc[
            kneset['BZB'] > _GLOBAL_ABOVE_X_PPK_VAR]
    return knesett







def is_sn_row_in_query(row, query):
    if query == Query.No_Single_Kalfi:
        if not is_yeshuv_single_kalfi(row) :
            return True
        return False
    elif query == Query.Arabs_Only:
        if is_yeshuv_type_arab(row["Yeshuv_Type"]):
            return True
        return False
    elif query == Query.Non_Arabs_Only:
        if not is_yeshuv_type_arab(row["Yeshuv_Type"]):
            return True
        return False
    elif query == Query.Above_Two_Kalfi:
        if is_yeshuv_above_two_kalfi(row):
            return True
        return False
    elif query == Query.Ppk_Above_X:
        ppk_values = row[['18_PPK', '19_PPK', '20_PPK', '21_PPK',
                          '22_PPK']].values.tolist()
        for ppk in ppk_values:
            if ppk < _GLOBAL_ABOVE_X_PPK_VAR:
                return False
        return True


def is_yeshuv_type_arab(yeshuv_type : str):
    if yeshuv_type in _ARABS_YESHUV_TYPES_LIST:
        return True
    return False


def is_yeshuv_single_kalfi(row):
    if row["18_Kalfi_Num"] == 1 and row["19_Kalfi_Num"] == 1 and row[
        "20_Kalfi_Num"] == 1 and row["21_Kalfi_Num"] == 1 and row[
        "22_Kalfi_Num"] == 1:
        return True
    else:
        return False


def is_yeshuv_above_two_kalfi(row):
    if row["18_Kalfi_Num"] > 2 and row["19_Kalfi_Num"] > 2 and row[
        "20_Kalfi_Num"] > 2 and row["21_Kalfi_Num"] > 2 and row[
        "22_Kalfi_Num"] > 2:
        return True
    else:
        return False
