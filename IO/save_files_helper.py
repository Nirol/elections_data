from typing import List

from Parse.data_classes import ThresholdsResultKnesset
from Questions.query_helper import Query
import pandas as pd
import MySQLdb
from sqlalchemy import create_engine
def save_stats_df(query_list: List[Query], stats_df):
    file_name = "stats_"
    for query in query_list:
        file_name = file_name + query.name + "_"
    stats_df.to_csv(r'Data\output\{}.csv'.format(file_name))


def save_kneset_data_to_my_sql(results: ThresholdsResultKnesset):

    # dbconnect = MySQLdb.connect("localhost", "flask_user", "123456",
    #                             "knesset_flask")


    engine = create_engine('mysql://flask_user:123456@localhost/knesset_flask')
    knessets_dict = results.get_threshold_kneset_dict(0)
    from constants import KNESSETS_LIST
    for knessets_num in KNESSETS_LIST:
        knessets_df = knessets_dict.get_kneset_data(knessets_num)
        knessets_df.drop(['Kosher_Voters', '1'], inplace=True, axis=1)
        table_name = 'knesset_' + str(knessets_num)
        knessets_df.to_sql(con=engine, name=table_name, if_exists='replace')
    print("ASD")


