from typing import List
from src.data.data_classes import ResultKnesset
from src.data.query.query_helper import Query
from sqlalchemy import create_engine


def save_stats_df(query_list: List[Query], stats_df):
    file_name = "stats_"
    for query in query_list:
        file_name = file_name + query.name + "_"
    stats_df.to_csv(r'Data\output\{}.csv'.format(file_name))


def save_kneset_data_to_my_sql(results: ResultKnesset):
    engine = create_engine('mysql://flask_user:123456@localhost/knesset_flask')

    from constants import KNESSETS_LIST
    for knessets_num in KNESSETS_LIST:
        if knessets_num == "18":
            knessets_df = results.get_kneset_data(knessets_num)
            knessets_df.drop(['Kosher_Voters', '1', 'Yeshuv_Type'], inplace=True, axis=1)

            table_name = 'knesset_' + str(knessets_num)
            knessets_df.to_sql(con=engine, name=table_name, if_exists='append', index=False)



