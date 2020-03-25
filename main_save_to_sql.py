from src.data.query import filter

if __name__ == '__main__':
    from save_files_helper import save_kneset_data_to_my_sql

    query_list = []
    # saving kneset result to sql done at the end:
    results = filter.filter_by_query(query_list)
    save_kneset_data_to_my_sql(results)


