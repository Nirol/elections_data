from enum import Enum
import pandas as pd




class Query(Enum):
    No_Single_Kalfi = 1
    Arabs_Only = 2
    Non_Arabs_Only = 3
    Above_Two_Kalfi = 4
    Kalfi_Above_X = 5


def filter_df_by_query(kneset: pd.DataFrame, query, threshold):
    knesset = None
    if query == Query.No_Single_Kalfi:
        knesset = kneset.groupby("SN").filter(lambda x: len(x) > 1)
    elif query == Query.Above_Two_Kalfi:
        knesset = kneset.groupby("SN").filter(lambda x: len(x) > 2)
    elif query == Query.Arabs_Only:
        from plot_helper import NON_JEW_YESHUVS
        knesset = kneset.loc[kneset['Yeshuv_Type'].isin(NON_JEW_YESHUVS)]
    elif query == Query.Non_Arabs_Only:
        from plot_helper import NON_JEW_YESHUVS
        knesset = kneset.loc[~kneset['Yeshuv_Type'].isin(NON_JEW_YESHUVS)]
    elif query.name ==  Query.Kalfi_Above_X.name:
        knesset = kneset.loc[
            kneset['BZB'] > threshold]
    return knesset


def is_yeshuv_type_arab(yeshuv_type: str):
    from plot_helper import NON_JEW_YESHUVS
    if yeshuv_type in NON_JEW_YESHUVS:
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
