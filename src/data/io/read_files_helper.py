import csv
from enum import Enum
import pandas as pd

PROJECT_FOLDER = "C:\\Users\\owner\\PycharmProjects\\Elections\\"
_YESHUVIM_CODE_LIST_FILE_PATH = PROJECT_FOLDER + "Data\\yeshuv\\yeshuvs_list_elections.csv"
_PARTIES_CODE_LIST_FILE_PATH = PROJECT_FOLDER + "Data\\raw\\parties_codes\\parties_codes.csv"
_YESHUVIM_METADATA_TYPE = PROJECT_FOLDER + "Data\\yeshuv\\yeshuv_metadata_type.csv"
_YESHUVIM_METADATA_TYPE_2 = PROJECT_FOLDER + "Data\\yeshuv\\yeshuv_metadata_new.csv"
_KALFI_ADDRESS_FILE = PROJECT_FOLDER + "Data\\clean\\kalfi_address_utf8.csv"

KNESSET_CLEAN_OUTPUT_FOLDER = PROJECT_FOLDER + "Data\\clean\\knesset\\"

_KNESET_18_FILE_PATH = PROJECT_FOLDER + "Data\\raw\\knesset\\18.csv"
_KNESET_19_FILE_PATH = PROJECT_FOLDER + "Data\\raw\\knesset\\19.csv"
_KNESET_20_FILE_PATH = PROJECT_FOLDER + "Data\\raw\\knesset\\20.csv"
_KNESET_21_FILE_PATH = PROJECT_FOLDER + "Data\\raw\\knesset\\21.csv"
_KNESET_22_FILE_PATH = PROJECT_FOLDER + "Data\\raw\\knesset\\22.csv"


class KnesetVars(Enum):
    Kalfi_Num = "Kalfi_Num"
    BZB = "BZB"
    Voters = "Voters"
    Kosher_Voters = "Kosher_Voters"
    Error_Voters = "Error_Voters"
    Yeshuv_Type = "Yeshuv_Type"
    Vote_Percent = "Vote_Percent"
    Error_Vote_Percent = "Error_Vote_Percent"



class KnesetData:
    def __init__(self):
        self.kneset_18 = None
        self.kneset_19 = None
        self.kneset_20 = None
        self.kneset_21 = None
        self.kneset_22 = None
        self.address = None
        self.yeshuvv = None

    def update_kneset_data(self, kneset_18, kneset_19, kneset_20, kneset_21,
                           kneset_22):
        self.kneset_18 = kneset_18
        self.kneset_19 = kneset_19
        self.kneset_20 = kneset_20
        self.kneset_21 = kneset_21
        self.kneset_22 = kneset_22

    def get_kneset_df(self, kneset_num):
        if kneset_num == "18":
            return self.kneset_18
        elif kneset_num == "19":
            return self.kneset_19
        elif kneset_num == "20":
            return self.kneset_20
        elif kneset_num == "21":
            return self.kneset_21
        elif kneset_num == "22":
            return self.kneset_22
        return None



    def load_clean_kneset_data(self):

        self.kneset_18 = pd.read_csv(KNESSET_CLEAN_OUTPUT_FOLDER+"_18.csv")
        self.kneset_19 = pd.read_csv(KNESSET_CLEAN_OUTPUT_FOLDER + "_19.csv")
        self.kneset_20 = pd.read_csv(KNESSET_CLEAN_OUTPUT_FOLDER + "_20.csv")
        self.kneset_21 = pd.read_csv(KNESSET_CLEAN_OUTPUT_FOLDER + "_21.csv")
        self.kneset_22 = pd.read_csv(KNESSET_CLEAN_OUTPUT_FOLDER + "_22.csv")


        self.address = pd.read_csv("Data/clean/kalfi_address_utf8.csv")
        self.yeshuvv = pd.read_csv(_YESHUVIM_METADATA_TYPE_2, encoding = 'ISO-8859-1' )




class MetaData:
    def __init__(self):
        # initializing instance variable
        self.parties = None
        self.yeshuvim = None
        self.parties_dict = None

    def update_meta_data(self, yeshuvim, parties):
        self.parties = parties
        self.yeshuvim = yeshuvim

    def get_yeshuvim_data(self):
        return self.yeshuvim

    def get_parties_data(self):
        return self.parties

    def update_parties_dict(self, parties_dict):
        self.parties_dict = parties_dict

    def get_parties_dict(self):
        return self.parties_dict

    def save_df_yeshuvim(self):
        self.yeshuvim.to_csv(r'Data\yeshovim.csv', index=True)


def read_data(kneset_data, meta_data):
    open_files_list = _open_files()
    _craete_dfs(open_files_list, kneset_data, meta_data)
    parties_code_list_df = meta_data.get_parties_data()
    parties_code_dict = parties_code_list_df.set_index("party")[
        'code'].to_dict()
    meta_data.update_parties_dict(parties_code_dict)


def _open_files():
    try:
        yeshuvim_code_list = open(_YESHUVIM_CODE_LIST_FILE_PATH, "r")
        parties_code_list = open(_PARTIES_CODE_LIST_FILE_PATH, "r")
        elec_18_csv = open(_KNESET_18_FILE_PATH, "r")
        elec_19_csv = open(_KNESET_19_FILE_PATH, "r")
        elec_20_csv = open(_KNESET_20_FILE_PATH, "r")
        elec_21_csv = open(_KNESET_21_FILE_PATH, "r")
        elec_22_csv = open(_KNESET_22_FILE_PATH, "r")

        return [yeshuvim_code_list, parties_code_list, elec_18_csv,
                elec_19_csv, elec_20_csv, elec_21_csv, elec_22_csv]
    except IOError:
        print("asd")



def _create_kneset_data_dfs(opend_files_list, kneset_data):
    elec_18_df = pd.read_csv(opend_files_list[2], delimiter=',', float_precision='round_trip')
    elec_18_df[elec_18_df.columns] = elec_18_df[elec_18_df.columns].astype(int)

    elec_19_df = pd.read_csv(opend_files_list[3], delimiter=',')
    elec_19_df[elec_19_df.columns] = elec_19_df[elec_19_df.columns].astype(int)

    elec_20_df = pd.read_csv(opend_files_list[4], delimiter=',')
    elec_20_df[elec_20_df.columns] = elec_20_df[elec_20_df.columns].astype(int)

    elec_21_df = pd.read_csv(opend_files_list[5], delimiter=',')
    elec_21_df[elec_21_df.columns] = elec_21_df[elec_21_df.columns].astype(int)

    elec_22_df = pd.read_csv(opend_files_list[6], delimiter=',')
    elec_22_df[elec_22_df.columns] = elec_22_df[elec_22_df.columns].astype(int)

    kneset_data.update_kneset_data(elec_18_df, elec_19_df, elec_20_df,
                                   elec_21_df, elec_22_df)


def _create_metadatra_dfs(opend_files_list, meta_data):
    yeshuvim_code_list_df = pd.read_csv(opend_files_list[0], delimiter=',')
    yeshuvim_code_list_df = yeshuvim_code_list_df.set_index('SN_yeshuv')

    parties_code_list_df = pd.read_csv(opend_files_list[1], delimiter=',')
    meta_data.update_meta_data(yeshuvim_code_list_df, parties_code_list_df)


def _craete_dfs(opend_files_list, kneset_data, meta_data):
    _create_kneset_data_dfs(opend_files_list, kneset_data)
    _create_metadatra_dfs(opend_files_list, meta_data)


def read_metadata_yeshuv_type_to_dict():
    with open(_YESHUVIM_METADATA_TYPE, mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]: rows[1] for rows in reader}
        return mydict
