from src.data.data_classes import ThresholdsResultKnesset
import pandas as pd


# TODO MAKE SURE SELF TO DELETE NOT IN USE
def parse_threshold_knessets_stats(
        results: ThresholdsResultKnesset) -> pd.DataFrame:
    df = pd.DataFrame(
        columns=['knesset', 'threshold', 'bzb', 'Num_Klafi', 'unq_yeshuv',
                 'vovters', 'vote_percent', 'std_vote_percent', 'avgBzb',
                 'pearson_corr', 'pearson_pvalue'])
    from constants import THRESHOLD_LIST
    from constants import KNESSETS_LIST
    for threshold in THRESHOLD_LIST:
        result_per_threshold = results.get_threshold_kneset_dict(threshold)
        for knesset_num in KNESSETS_LIST:
            pop_stats = result_per_threshold.get_kneset_stats(knesset_num)
            row_prefix = [knesset_num, threshold]
            row_suffix = pop_stats.stats_to_row()
            df.loc[len(df)] = row_prefix + row_suffix
    return df



