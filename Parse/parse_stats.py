from Parse.data_classes import ResultKnesset, ThresholdsResultKnesset
import pandas as pd




def parse_threshold_kneseets_stats(results :ThresholdsResultKnesset) -> None:
    df = pd.DataFrame(columns=['knesset','threshold', 'bzb',  'Num_Klafi', 'unq_yeshuv','vovters','vote_percent', 'std_vote_percent' ,'avgBzb','pearson_corr', 'pearson_pvalue'])
    from constants import THRESHOLD_LIST
    from constants import KNESSETS_LIST
    for threshold in THRESHOLD_LIST:
        result_per_threshold = results.get_threshold_kneset_dict(threshold)
        for knesset_num in KNESSETS_LIST:
            pop_stats = result_per_threshold.get_kneset_stats(knesset_num)
            row_prefix = [knesset_num, threshold]
            row_suffix = pop_stats.stats_to_row()
            df.loc[len(df)] = row_prefix + row_suffix

    print(df)
    return df













def validate_all_yeshuvs_in_sries(b : pd.Series):

    bigger_100_list = ["120", "130", "140"]

    between_10_100_jew_list = ["150", "160", '170']

    smaller_yeshuv_jews_list = ['310','320', '192','191',
                                '180','190','340','370','370','330','193']

    non_jew_yeshuvs = ["250", "260",'270', '280', '290',  '450', '460']
    total_list = bigger_100_list + between_10_100_jew_list + smaller_yeshuv_jews_list + non_jew_yeshuvs

    index_list_in_series = b.index.values
    for yeshuv_code in total_list:
        if yeshuv_code not in b:
            print("adding code={}".format(yeshuv_code))
            b[yeshuv_code] = 0