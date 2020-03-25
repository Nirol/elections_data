

KNESSETS_LIST = ["18", "19", "20", "21", "22"]
THRESHOLD_LIST = [0, 150, 200, 250, 300, 357, 400 ,500]




#  reading original knesset metadata constants for main_parse_input.py:
KNESET_DF_NUM_META_COLS=6

# yeshuvim df col names are set here:
from read_files_helper import KnesetVars
def get_yeshuvim_col_name(kneseet_num : int, knese_enum_var: KnesetVars):
    return kneseet_num + "_" + knese_enum_var.value


