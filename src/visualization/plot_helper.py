from enum import Enum
#all yeshuvs from 2k to 100k of jews // non jews
BIG_YESHUV_LIST = ["150", "160", '170', '180', '190', "250" , "260" , '270' , '280', '290']
# cities above 100k/ 200k / 500k all considered jews
HUGE_YESHUV_LIST = ["120", "130", "140"]
#small under 2k yeshuvs of jews // non jews
OTHER_YESHUV_LIST = ["310", "320", '330', '350', '370', '450', '460']

BIG_NON_JEW_YESHUV_LIST = BIG_YESHUV_LIST[:5]
BIG_JEW_YESHUV_LIST = BIG_YESHUV_LIST[5:]

#all type of non jew yeshuvs:
NON_JEW_YESHUVS = ["250", "260", '270', '280', '290', '450', '460']


#used in BZB pie graph
SMALL_JEW_YESHUV_LIST = ['310', '320', '192', '191',
                                '180', '190', '340', '370', '370', '330',
                                '193']

MAATAFOT_KFOLOT = [875, 99999, 9999]
BIG_YESHUV_INDEX = ['50-100', '20-50', '10-20', '5-10', '2-5']

# HUGE_YESHUV_INDEX = ['500+ (םילשורי)', '200-500', '100-200']

# population sub groups

class PopGroup(Enum):
    Small_Jew_Yeshuv = 1
    Small_Arab_Yeshuv = 2
    Big_Jew_Yeshuv = 3
    Big_Non_Jew_Yeshuv = 4
    Huge_Cities = 5


class YeshuvType(Enum):
    Big = 1
    Others = 2
    Huge = 3


class PlotType(Enum):
    Vote_Percent = 1
    Error = 2
    AvgBzb = 3
    Bzb = 4
    Vote_Percent_Box_Plot = 5
    Error_Percent = 6

# on kneset 19, sn-875 was maatafot kfolot// hitzoniot
